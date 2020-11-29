import numpy as np
import matplotlib.pyplot as plt

T0 = 293. #Kelvin
Tbath = 273. #K
Thot = 323. #K
D = 4.23e-2 #cm^2 s^-1
M=100. #for the spatial grid
h=0.001 #time step
L = 1. #cm Length of the steel
a = L/M #spatial step
const = D*h/(a*a)
x=np.arange(0,1,a) #cm
T = np.zeros(int(M),float) # at time t=0+h
T[1:int(M)]=T0
T[0] = Thot
T[int(M)-1] = Tbath
Tnew = np.zeros(int(M),float)
Tnew[0]=Thot
Tnew[int(M)-1]=Tbath

for j in range(1,1001):
	for i in range(1,int(M)-1):
		Tnew[i] = T[i]+const*(T[i+1]+T[i-1]-2*T[i])
	T = Tnew
	if ((j==1) or (j==10) or (j==100) or (j==1000)): #plot at t=0.01,0.1,1.0,10.0
		q = j*0.01
		Tgraph=plt.plot(x,Tnew,label= q )

plt.legend(loc='upper right')
plt.tight_layout()
plt.show()