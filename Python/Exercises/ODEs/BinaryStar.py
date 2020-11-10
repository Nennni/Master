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

x = np.zeros(int(N),float)			#PARTICELLA 1
x[0] = (1.+1.)**0.5
y = np.zeros(int(N),float)			#PARTICELLA 2
y[0] = (1.+1.)**0.5

X=[]
X.append(x)
X.append(y)
X = np.array(X) 	#MATRICE DELLE PARTICELLE

vx = np.zeros(int(N),float)			#VELOCITA PARTICELLA 1
vx[0] = (0.25+0.25)**0.5		
vy = np.zeros(int(N),float)			#VELOCITA PARTICELLA 2
vy[0] = 0.
V=[]
V.append(vx)
V.append(vy)
V = np.array(V) 				#MATRICE DELLE VELOCITA

X=np.transpose(X)
V=np.transpose(V)

# -------- EULER -------- x(t+h) = x(t) + h f(x,t)
for i in range(1,int(N)):
	for j in range(len(m)):	
		X[i,j]=X[i-1,j]+h*V[i-1,j]
		for k in range(len(m)):
			if (k!=j):
				V[i,j]=V[i-1,j]+h*(-(X[i-1,k]-X[i-1,j])/(np.any((abs(X[i-1,k]-X[i-1,j]))**3)))
X=np.transpose(X)
print(X)

grafic = plt.plot(X[0,:],X[1,:],"b-")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.show()