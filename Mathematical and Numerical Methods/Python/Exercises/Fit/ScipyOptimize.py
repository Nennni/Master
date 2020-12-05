import numpy as np
from numpy.linalg import solve
from numpy import random as rnd
import matplotlib.pyplot as plt
from scipy import optimize as opt
#from scipy import optimize as opt

def data_set(): 
	a=0.0
	s=2.0
	h=1.0
	x=np.linspace(-5.,5.,num=500) #x data 
	y=h*np.exp(-(x-a)**2/(2.*s**2))
	sigma=np.zeros(len(x),float) 
	for i in range(len(y)):
		sigma[i]=0.1*rnd.random() 
		y[i]=rnd.normal(y[i],sigma[i]) #add gaussian noise
	return x,y

def gauss_res(a,x,y):
	gauss_res=a[2]*np.exp(-(x-a[0])**2/2./a[1]**2)-y
	return gauss_res
def gauss(a,x):
	f = a[2]*np.exp(-(x-a[0])**2/2./a[1]**2)
	return f


x,y = data_set()
a = np.zeros(3,'float')
a[0],a[1],a[2] = 2. , 2. , 2.

lsq=opt.least_squares(gauss_res,a,args=(x,y),xtol=1e-07,loss='cauchy')
a = lsq.x

f = gauss(a,x)

graph = plt.scatter(x,y,marker='*',label='Data')
graph1 = plt.plot(x,f,"r-",label='Scipy Fit')
plt.xlabel('$x_{i}$')
plt.ylabel('$y_{i}$')
plt.legend(loc = 'upper right')
plt.show()








