import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rnd

def data_set():
	x=np.logspace(0,4,num=10000) #x data
	b=-2.0
	a=3.0
	y=10.**a * x**b #intrinsic relation y=10**a * x**b 
	x=np.log10(x)
	y=np.log10(y)
	sigma=1.
	y=rnd.normal(y,sigma) #add gaussian noise 
	return x,y

def fit_params():
	x,y = data_set()
	mean_x = np.sum(x)/(len(x)-1)
	mean_y = np.sum(y)/(len(y)-1)
	A,B=0.,0.
	sx,sy=0.,0.
	x2 = np.zeros(len(x),float)
	for i in range(len(x)-1):
		sy += y[i]*(x[i]-mean_x)
		sx += x[i]*(x[i]-mean_x)
		x2[i] = x[i]*x[i]


	B = (sy/sx)
	A = mean_y - mean_x*B
	
	delta = (len(x)-1)*np.sum(x2) - (np.sum(x))**2
	return A,B,delta

def errorParams():
	x,y=data_set()
	A,B,delta=fit_params()
	s=0.
	for i in range(len(x)-2):
		s += (y[i]-A-B*x[i])**2
	sigma_y = ( (s/(len(x)-1)) )**(0.5)
	sigma_A =  sigma_y*((np.sum(x**2))/(delta))**0.5
	sigma_B = sigma_y*((len(x)-1)/delta)**0.5
	return A,B,sigma_A,sigma_B,sigma_y

# ------- MAIN --------

x,y=data_set()
A,B,sigma_A,sigma_B,sigma_y = errorParams()
print("A =",A,"+/-",sigma_A)
print("B =",B,"+/-",sigma_B)
print("sigma y = ",sigma_y)

yfit = np.zeros(len(x)-1,'float')
yfit = A+B*x
Chi2=0.
for i in range(len(x)-1):
	Chi2 += ((y[i] - A - B*x[i])/(sigma_y))**2
print("Chi^2=",Chi2)

# -------- PLOTS --------

graph=plt.scatter(x,y,marker='*',color='blue',label='Data')
graph1=plt.plot(x,yfit,'r-',label='Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()