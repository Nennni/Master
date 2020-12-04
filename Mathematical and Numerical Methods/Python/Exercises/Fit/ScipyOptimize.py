import numpy as np
from numpy.linalg import solve
from numpy import random as rnd
import matplotlib.pyplot as plt
import scipy as scipy
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
def fit_params(a,x,y):	
	x,y = data_set()
	f = a[2]*np.exp(-((x-a[0])**2)/(2.*a[1]**2)) -y
	return f

x,y = data_set()
a = np.zeros(3,'float')
a[0],a[1],a[2] = 0. , 2. , 1.
Isq = scipy.optimize.least_squares((fit_params,a, args=(x,y)))

