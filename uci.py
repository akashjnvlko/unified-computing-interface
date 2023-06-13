# Author : Akash Yadav PHD232006
#        : akashyadav23@iisertvm.ac.in

# Generalized version of the distributed computation approach for parameter scanning
# For general usage this script can be imported as a module



import paramiko
import numpy as np 
import multiprocessing as mp 
import os 
import time 
import subprocess
from tqdm import tqdm

# configuration of the cluster 
select=[0,1,2,4] # this part can be automated by cheaking the online systems

 # list down the system details along with the ip address and login information
users = []
pwds  = []
hosts =   []
#

users =[users[i] for i in select]
hosts =[hosts[i] for i in select]
pwds = [pwds[i] for i in select]


def commandV(usr,pwd,host,command):
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host,username=usr,password=pwd)
    (stdin, stdout, stderr) =ssh_client.exec_command(command) 
    cmd_output = stdout.read()
    print(cmd_output)
    ssh_client.close()
    del ssh_client, stdin, stdout, stderr

def command(usr,pwd,host,command):
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host,username=usr,password=pwd)
    (stdin, stdout, stderr) =ssh_client.exec_command(command+' > /dev/null 2>&1') 
    # cmd_output = stdout.read()
    # print(cmd_output)
    ssh_client.close()
    del ssh_client, stdin, stdout, stderr



def get_sysconfig(usr,pwd,host):  
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host,username=usr,password=pwd)
    command = 'nproc --all'
    (stdin, stdout, stderr) = ssh_client.exec_command(command) 
    cmd_output = stdout.read()
    ssh_client.close()
    del ssh_client, stdin, stdout, stderr
    print('getting cpu counts for host ',host)
    return cmd_output.decode('utf-8').strip()
    

def send_file(usr,pwd,host,src,dst):
    dst_path = '/home/'+ str(usr) +'/CLUSTER/'+ str(dst)
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host,username=usr,password=pwd)
    sftp_client = ssh_client.open_sftp()
    sftp_client.put(src,dst_path)
    sftp_client.close()
    del ssh_client,sftp_client


def get_file(usr,pwd,host):
    src_path = '/home/'+ str(usr) +'/CLUSTER/DATA/'
    dst_path = os.getcwd()+'/DATA_MERGED/'
    os.system('mkdir -p '+dst_path)
    os.system('sshpass -p ' +pwd +' rsync -a ' + usr +'@' + host+':'+src_path + ' '+ dst_path )
    # print("Getting files from host : ",host)
    dst_path = os.getcwd()+'/DATA_MERGED/'
    output=subprocess.check_output("ls "+ dst_path+" -1 | wc -l",shell=True)
    no_of_files=int(output.decode().strip())
    # print("Successfully transferred ",no_of_files," files.")


def cpu_counts():
    cpus = []
    for i in range(len(hosts)):  
        cpus.append(get_sysconfig(users[i],pwds[i],hosts[i]))
    return np.array(cpus,dtype='int64')

# pass the file name of the program to be executed
def allocate_tasks(code_file_name):
    cpu_array = cpu_counts()
    dpack = np.load('index.npy')
    # np.save('dpack',dpack)
    total_tasks = len(dpack)
    total_cpus = sum(cpu_array)
    print('################################################################')
    print("\nTotal ",total_cpus, " CPUs found. Enjoy!")
    print('################################################################')
    # dividing the task among machines
    sys_count = len(cpu_array)
    alloc_factor = total_tasks*cpu_array/total_cpus
    alloc_factor = np.floor(alloc_factor)
    alloc_factor[-1] = total_tasks- sum(alloc_factor[0:-1])
    # print(alloc_factor)
    # print(sum(alloc_factor))
    index_arr = np.zeros(sys_count+1,dtype=int)
    for i in range(sys_count):
        index_arr[i+1] = index_arr[i] + alloc_factor[i]
    index_arr = index_arr
    print('\ntasks divided. Sending the tasks ...')
    

    for i in range(sys_count):
        task = dpack[index_arr[i]:index_arr[i+1],:]
        np.save('task'+str(round(i+1)),task)
        print('clearing old CLUSTER path in remote systems')
        command(users[i],pwds[i],hosts[i],'cd /home/'+ users[i]+ ' && rm -r CLUSTER')
        command(users[i],pwds[i],hosts[i],'cd /home/'+ users[i]+ ' && mkdir -p CLUSTER')
        print('send packet to ', users[i]+'@'+hosts[i])
        send_file(users[i],pwds[i],hosts[i],'task'+str(round(i+1))+'.npy','task.npy')
        send_file(users[i],pwds[i],hosts[i],code_file_name,code_file_name)
        print('SUCCESSFUL! essential packets deployed to node : '+str(i+1))
        command(users[i],pwds[i],hosts[i],'cd /home/'+users[i]+'/CLUSTER/ && python3 ' +str(code_file_name) + ' > /dev/null 2>&1')
        
    return sys_count,total_tasks


def deploy(code_file_name):
    logo()
    print("The cluster is configured with systems = ",users)
    print("The ip addressess of configured nodes are = ",hosts)
    print("")
    print("\nPlease make sure index file is present in the working directory.")
    
    if input("Do you want to deploy ? (y/n) ") =='y':
        if os.path.exists('DATA_MERGED'):
            print("Old data found. Deleting...")
            os.system('rm -r DATA_MERGED')
        sys_count,total_tasks = allocate_tasks(code_file_name)

        # create a progress bar to monitor overall progress
        print('\n........... OVERALL PROGRESS .............')
        pbar = tqdm(total = total_tasks,colour='green')

        
    
        flag = True 
        while flag:
            for i in range(len(hosts)):
                get_file(users[i],pwds[i],hosts[i])
            time.sleep(10)
            dst_path = os.getcwd()+'/DATA_MERGED/'
            output=subprocess.check_output("ls "+ dst_path+" -1 | wc -l",shell=True)
            no_of_files=int(output.decode().strip())

            # update the progress bar
            pbar.n = no_of_files
            pbar.refresh()

            if no_of_files == total_tasks:
                time.sleep(3)
                flag = False
                for i in range(len(hosts)):
                    get_file(users[i],pwds[i],hosts[i])
                    time.sleep(3)
                    # close the progress bar
                    pbar.close()
                    print('\nclearing CLUSTER path in remote system:',hosts[i])
                    command(users[i],pwds[i],hosts[i],'cd /home/'+ users[i]+ ' && rm -r CLUSTER')
        print('\n************************** JOB COMPLETE *******************************')
        print('________________________________________________________________________')
        
    else:
        pass

                    
                    
    # for killing all the active python processes in the cluster

def kill_all():
    print("Executing the kill command !")
    for i in range(len(hosts)):
        print("Python Process on "+hosts[i]+ " is killed.!")
        command(users[i],pwds[i],hosts[i],'pkill python3')




# kill all processes if called from main file
if __name__ == "__main__":
    kill_all()

           

    

def logo():
    print('''
\033[96m    
________________________________________________________________________                     
                    Unified Computing Interface  
------------------------------------------------------------------------                     
\033[0m\033[95mUUU    UUU   \033[94mCCCCCC     \033[95m\033[96mIII         |\033[0m \033[91mParameter Scanning Utility  \033[0m
\033[95mUUU    UUU  \033[94mCCC       \033[95m  \033[96mIII         |
\033[95mUUU    UUU  \033[94mCCC       \033[95m  \033[96mIII         |\033[0m \033[92mDesigned and Maintained by:\033[0m
\033[95mUUU    UUU  \033[94mCCC       \033[95m  \033[96mIII         |\033[0m \033[92m -Akash Yadav PHD232006 \033[0m
\033[95m  UUUUUU    \033[94m CCCCCC\033[95m     \033[96mIII         |\033[0m \033[92m -akashyadav@iisertvm.ac.in\033[0m
\033[96m------------------------------------------------------------------------\n\033[0m''')
