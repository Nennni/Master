import numpy as np 
import matplotlib.pyplot as plt

#def a(x,i,j):
#	for k in range(Np):
#		if(j!=k):
#			A=np.zeros([i,j],float)
				#ax = np.array([N,2],float)
				#ay = np.array([N,2],float)
				#a = np.array([ax],[ay],float)
#			A[i,j]-= G*(m[k]*(x[i,j]-x[i,k]))/(abs(x[i,j]-x[i,k]))**3
#	A=sum(A)
#	return A

Np=2
m1,m2 = 1.,1.
m=[]
m.append(m1)
m.append(m1)
m = np.array(m)
G = 1. #Gravity constant
t_0 = 0.0
t_fin = 300
h = 0.01
N = (t_fin-t_0)/h
t = np.arange(t_0,t_fin,h)


xx = np.zeros(int(N),float)
xy = np.zeros(int(N),float)
x = []
x.append(xx)
x.append(xy)
x = np.array(x)
x[0,0] = 1.
x[1,0] = -1.
print(x)

yx = np.zeros(int(N),float)
yy = np.zeros(int(N),float)
y = []
y.append(yx)
y.append(yy)
y = np.array(y)
y[0,0] = 1.
y[1,0] = -1.
print(y)

vxx = np.zeros(int(N),float)					
vxy = np.zeros(int(N),float)			
vx=[]
vx.append(vxx)
vx.append(vxy)
vx = np.array(vx) 
vx[0,0] = -0.5
vx[1,0] = 0.5				

vyx = np.zeros(int(N),float)					
vyy = np.zeros(int(N),float)			
vy=[]
vy.append(vyx)
vy.append(vyy)
vy = np.array(vy) 
vy[0,0] = 0.
vy[1,0] = 0.		

X = []
X.append(x)
X.append(y)
X=np.array(X)
print("Matrice posizioni", X[0,0,int(N)-1] )
V = []
V.append(vx)
V.append(vy)
V=np.array(V)
print("Matrice velocità",V[0,1,0],V[1,0,0]) # V [ particella, coordinata, tempo ]

# -------- EULER -------- x(t+h) = x(t) + h f(x,t)
for i in range(1,int(N)):
	for k in range(Np):
		for j in range(Np):
			if(j!=k):
				V[:,:,i] = V[:,:,i-1]
				V[:,:,i] += h*( (X[k,:,i-1] - X[j,:,i-1])/(((np.linalg.norm(X[k,:,i-1] - X[j,:,i-1]))**3)) ) 
	X[:,:,i] = X[:,:,i-1] + h*V[:,:,i-1]

x = []
x.append(X[0,:,:])
print(x)
grafic = plt.plot(X[0,:,:],X[1,:,:],"b-")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.show()