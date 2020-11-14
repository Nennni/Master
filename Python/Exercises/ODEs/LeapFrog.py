import numpy as np 
from numpy import linalg
import matplotlib.pyplot as plt

def a(x1,x2,m):
	f = -G*m*(x1-x2)/((abs(linalg.norm(x1-x2)))**3)
	return f



G = 1. #Gravity constant
t_0 = 0.0
t_fin = 300.
h = 0.01
N = (t_fin-t_0)/h
m = np.array([1.,1.],float)

X = np.zeros([2,2,int(N)],float)
V = np.zeros([2,2,int(N)],float)

X[0,0,0], X[0,1,0] = 1.,1.
X[1,0,0], X[1,1,0] = -1.,-1.

V[0,0,0],V[0,1,0] = -0.5,0.
V[1,0,0],V[1,1,0] = 0.5,0.



for k in range(int(N)):
	for i in range(2):
		for j in range(2):
			if (j!=i):
				X[i,:,k] = X[i,:,k-1]+h*V[i,:,k-1] +0.5*h*h*(a(X[i,:,k-1],X[j,:,k-1],m[j]))
				V[i,:,k] = V[i,:,k-1]+0.5*h*(a(X[i,:,k-1],X[j,:,k-1],m[j]) + a(X[i,:,k],X[j,:,k],m[j]))

grafic = plt.plot(X[0,0,:],X[0,1,:],"r-",label='Leap Frog')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.tight_layout()
plt.show()