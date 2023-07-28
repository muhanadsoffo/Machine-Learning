import numpy as np 

feature = np.arange(6,21)


label= (3*feature)+4


noise = (np.random.random([15]) * 4) - 2
print(noise)
label = label + noise 
print(label)