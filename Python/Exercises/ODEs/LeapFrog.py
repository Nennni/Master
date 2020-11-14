import numpy as np 
from numpy import linalg
import matplotlib.pyplot as plt

def a(x,y):
	f = -(x-y)/(np.linalg.norm(x-y))**3
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

b = a(X[0,:,0],X[1,:,0])

print(b)
for k in range(1,int(N)):
	for i in range(2):
		for j in range(2):
			if (j!=i):
				X[i,:,k] = X[i,:,k-1]+h*V[i,:,k-1] +0.5*h*h*(a(X[i,:,k-1],X[j,:,k-1]))
				X[j,:,k] = X[j,:,k-1]+h*V[j,:,k-1] +0.5*h*h*(a(X[j,:,k-1],X[i,:,k-1]))
				V[i,:,k] = V[i,:,k-1]+0.5*h*(a(X[i,:,k-1],X[j,:,k-1]) + a(X[i,:,k],X[j,:,k]))

grafic = plt.plot(X[0,0,:],X[0,1,:],"r-",label='m1, Leap Frog')
grafic1 = plt.plot(X[1,0,:],X[1,1,:],"r-",label='m2, Leap Frog')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.tight_layout()
plt.show()