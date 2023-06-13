import numpy as np 
import uci 

index = []
################# generate the index file ######################
# parameter sigma values to scan 
sigma_vals = np.arange(0,10.5,0.5)
# parameter sigma values to scan 
q_vals = np.arange(0,1.1,0.1)

# also saving both arrays for reference

np.save('sigma_vals',sigma_vals)
np.save('q_vals',q_vals)

for s_val in sigma_vals:
    for q_val in q_vals:
        index.append([s_val,q_val])

np.save('index',index)
print('No of runs = ',len(index))
fname = "simulation.py"

uci.deploy(fname)






