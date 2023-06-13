import numpy as np 
from multiprocessing import Pool
import os 

# load task file
task = np.load('task.npy')

# specify the folder to save data 
path = 'DATA/'
if os.path.exists(path) is True:
    os.system('rm -r ' + str(path))
    os.mkdir(path)
else:
    os.mkdir(path)
    
    
def simulate(params):
    sigma,q = params
    .
    .
    .
    save_path = path + str(sigma) + "_" + str(q)
    np.save(save_path, sync_vals)\
    
    
# # using multiprocessing to process the assigned task
pool = Pool() # cpus can be assigned here 
pool.map(simulate,task)
pool.close()
