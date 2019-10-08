import numpy as np
from io import StringIO
import time
## 1 million samples
#n_samples=1000000

## Write random floating point numbers as string on a local CSV file
#with open('fdata.txt', 'w') as fdata:
#    for _ in range(n_samples):
#        fdata.write(str(10*np.random.random())+',')
        
## Read the CSV in a list, convert to ndarray (reshape just for fun) and time it
t1=time.time()
#with open('BA.csv','r') as fdata:
#    datastr=fdata.read()
#lst = datastr.split(',')
#lst.pop()
#array_lst=np.array(lst,dtype=float).reshape(1000,1000)
#t2=time.time()

import pandas as pd
df=pd.read_csv('BA.csv', sep=',',header=None)
df.values
array([[ 1. ,  2. ,  3. ],
       [ 4. ,  5.5,  6. ]])

from numpy import genfromtxt
numpy_lst = genfromtxt('BA.csv', delimiter=',')


print(numpy_lst)
print('\nShape: ',numpy_lst.shape)
print(f"Time took to read: {t2-t1} seconds.")

np.save('fnumpy2.npy', array_lst)
