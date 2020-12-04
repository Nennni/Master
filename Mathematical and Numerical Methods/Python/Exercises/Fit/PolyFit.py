import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg

fname1 = "120a300.txt"
fname2 = "evol_120msun_scattered.txt"

def data_set():
	Time,Mass = np.genfromtxt(fname1,dtype='float',usecols=(0,7) ,comments = '#', unpack=True)
	x,y = np.genfromtxt(fname2,dtype='float',usecols=(0,1),comments='#',unpack=True)

	return x,y

def third_order():
	x,y = data_set()
	m3 = 3
	N = len(x)
	A = np.zeros([m3+1,m3+1],'float')
	b = np.zeros(m3+1,'float')
	for j in range(0,m3+1):
		for k in range(0,m3+1):
			b[k] = sum((x**k)*y)
			A[j,k] = sum((x)**(j+k))
	a = linalg.solve(A,b)
	return a,x,y,m3

def seventh_order():
	x,y = data_set()
	m7=7
	N=len(x)
	A = np.zeros([m7+1,m7+1],'float')
	b = np.zeros(m7+1,'float')
	for j in range(0,m7+1):
		for k in range(0,m7+1):
			A[j,k] = sum(x**(j+k))
			b[k] = sum(x**k *y)
	a = linalg.solve(A,b)
	return a,m7

a3,x,y,m3 = third_order()
f3 = np.zeros(len(x),'float')
for i in range(len(x)-1):
	for j in range(m3+1):
		f3[i] += a3[j]*(x[i])**j

a7,m7 = seventh_order()
f7 = np.zeros(len(x),'float')
for i in range(len(x)-1):
	for j in range(m7+1):
		f7[i] += a7[j]*(x[i])**j

graph1 = plt.scatter(x,y,marker='*',color='blue',label = 'Data')
fit3 = plt.plot(x,f3,"r-",label='Poly Fit m=3')
fit7 = plt.plot(x,f7,"k-",label='Poly Fit m=7')
plt.xlabel('time [Myr]')
plt.ylabel('Mass $M_{\odot}$')
plt.legend(loc='upper right')
plt.show()

