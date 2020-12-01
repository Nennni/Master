import numpy as np
import matplotlib.pyplot as plt

def f (ti,ti1,t,mi,mi1):
	f = ((ti1-t)*mi + (t-ti)*mi1)/(ti1-ti)
	return f

t,m = np.genfromtxt("evol_120msun_scattered.txt",dtype='float',comments='#',usecols=(0,1), unpack=True)
T,M = np.genfromtxt("120a300.txt",dtype='float',comments='#',usecols=(0,7),unpack=True)

T/=1e6
tol=1e-4
m1=np.zeros(len(T),float)
j=0
for i in range(len(T)): 
	if (abs(t[j+1]-T[i])<tol and j<len(t)-2): #if the time values ar the same i need to go to the next t[j]
		j+=1
	m1[i]=f(t[j],t[j+1],T[i],m[j],m[j+1])

# ----- PLOTS -------
graph2 = plt.plot(T,m1,'r.',label='interpolation')
graph1 = plt.plot(T,M,"k,",label='Original Data')
graph = plt.plot(t,m,"bo",label='Scattered Data')
plt.xlabel('t [Myr]')
plt.ylabel('Mass [$M_{\odot}$]')
plt.legend(loc='lower left')
plt.tight_layout()
plt.show()