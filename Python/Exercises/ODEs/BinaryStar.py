import numpy as np 
import matplotlib.pyplot as plt
from numpy import linalg

def a(x1,x2,m):
	a = -G*m*(x1-x2)/((linalg.norm(x1-x2))**3)

Np=2
m1,m2 = 1.,1.
m=[]
m.append(m1)
m.append(m1)
m = np.array(m)
G = 1. #Gravity constant
t_0 = 0.0
t_fin = 300.
h = 0.01
N = (t_fin-t_0)/h

X = np.zeros([2,Np,int(N)],float)
V = np.zeros([2,Np,int(N)],float)

X[0,0,0], X[0,1,0] = 1.,1.
X[1,0,0], X[1,1,0] = -1.,-1.

V[0,0,0],V[0,1,0] = -0.5,0.
V[1,0,0],V[1,1,0] = 0.5,0.

# -------- EULER -------- x(t+h) = x(t) + h f(x,t)
for i in range(1,int(N)):
	for k in range(Np):
		for j in range(Np):
			if(j!=k):
				V[k,:,i] = V[k,:,i-1]+h*( -(X[k,:,i-1] - X[j,:,i-1])/((linalg.norm(X[k,:,i-1] - X[j,:,i-1]))**3) ) 
				X[k,:,i] = X[k,:,i-1] + h*V[k,:,i-1]

# -------- MIDPOINT --------
t = np.arange(t_0,t_fin,0.5*h)

X1 = np.zeros([2,Np,int(N)],float)
V1 = np.zeros([2,Np,int(N)],float)

X1[0,0,0], X1[0,1,0] = 1.,1.
X1[1,0,0], X1[1,1,0] = -1.,-1.

V1[0,0,0],V1[0,1,0] = -0.5,0.
V1[1,0,0],V1[1,1,0] =  0.5,0.

k1x = np.zeros([2,Np,int(N)],float)
k1v = np.zeros([2,Np,int(N)],float)
xth2 = np.zeros([2,Np,int(N)],float)
k2x = np.zeros([2,Np,int(N)],float)
k2v = np.zeros([2,Np,int(N)],float)

for k in range(1,int(N)):
	for i in range(2):
		for j in range(2):
			if(j!=i):
				k1x[i,:,k]=0.5*h*V1[i,:,k-1]
				k1x[j,:,k]=0.5*h*V1[j,:,k-1]
				k1v[i,:,k]=0.5*h*(-(X1[i,:,k-1] - X1[j,:,k-1])/((linalg.norm(X1[i,:,k-1] - X1[j,:,k-1]))**3))
				xth2[i,:,k-1] = X1[i,:,k-1] + k1x[i,:,k]
				xth2[j,:,k-1] = X1[j,:,k-1] + k1x[j,:,k]
				k2x[i,:,k] = h*(V1[i,:,k-1]+k1v[i,:,k])
				k2v[i,:,k] = h*(-(xth2[i,:,k-1] - xth2[j,:,k-1])/((linalg.norm(xth2[i,:,k-1] - xth2[j,:,k-1]))**3))
				X1[i,:,k]=X1[i,:,k-1]+k2x[i,:,k]
				V1[i,:,k] = V1[i,:,k-1]+k2v[i,:,k]

# ------- GRAFICS -------
grafic = plt.plot(X[0,0,:],X[0,1,:],"b-",label='m1, Euler')
grafic1 =plt.plot(X[1,0,:],X[1,1,:],"g-",label='m2, Euler')
grafic2 = plt.plot(X1[0,0,:],X1[0,1,:],"r-",label='m1, Midpoint')
grafic3 = plt.plot(X1[1,0,:],X1[1,1,:],"r-",label='m2, Midpoint')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.tight_layout()
plt.show()