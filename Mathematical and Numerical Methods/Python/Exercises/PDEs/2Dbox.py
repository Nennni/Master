import numpy as np
import matplotlib.pyplot as plt
import time

start = time.time()
M = 100 #(M+1)x(M+1) will be my matrix
V = 1. #volt
phi = np.zeros([M+1,M+1],float)
phi[0,:]=V
delta = 1e-2
phi_old = np.zeros([M+1,M+1],float)
norma = 10.

k=0 #counter
while(norma>delta):
	for i in range(1,M): #rows
		for j in range(1,M): #columns
			phi[i,j] = 0.25*( phi[i+1,j]+phi[i-1,j]+phi[i,j+1]+phi[i,j-1] )
	norma = np.linalg.norm(phi_old-phi)
	phi_old = np.copy(phi)
	k+=1
end=time.time()
print('Running time:',end-start,'s')
a = plt.imshow(phi)
plt.show()
