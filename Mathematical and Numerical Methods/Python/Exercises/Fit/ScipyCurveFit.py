import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rnd
from scipy import optimize as opt

def data_set(): 
	a=0.
	s=1. 
	h=10.
	x=np.linspace(-10.,10.,num=500) #x data 
	y=h*np.exp(-(x-a)**2/2./s**2)
	sigma=np.zeros(len(x),float) 
	for i in range(len(y)):
		sigma[i]=4.*rnd.random() 
		y[i]=rnd.normal(y[i],sigma[i]) #add gaussian noise
	return x,y

def gauss(x,a,s,h):
	gauss=h*np.exp(-(x-a)**2/2./s**2)
	return gauss

x,y = data_set()
a = np.zeros(3,'float')
a[0],a[1],a[2] = 2. , 2. , 2.

popt,pcov = opt.curve_fit(gauss,x,y,p0=(a[0],a[1],a[2]))
print(popt)

f = gauss(x,popt[0],popt[1],popt[2])

graph = plt.scatter(x,y,marker='*',color='#2ca02c',label = 'Data')
graph1 = plt.plot(x,f,"r-",label="Scipy Curve Fit")
plt.xlabel('$x_i$')
plt.ylabel('$y_i$')
plt.legend(loc='upper right')
plt.show()
