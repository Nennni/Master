import numpy as np
from numpy.linalg import solve

a = [[2. ,1. ,4. ,1.],[3. , 4. , -1. ,-1],[1. ,-4. ,1 ,5.],[2. ,-2. ,1. ,3.]]

b = [-4. , 3. , 9. , 7.]
N=4
A = np.array(a,float)
b = np.array(b,float)
x = np.zeros(N,float)

x=solve(A,b)

print(x)
