import numpy as np 
from numpy import random
import matplotlib.pyplot as plt

def f(x,t):
	f = -x**3 + np.sin(t) 
	return f

t_0 = 0.0
t_fin = 100.
x_t0 = 0.0
h = 0.4
N = (t_fin - t_0)/h
t = np.arange(t_0,t_fin,h)
x = np.zeros(N,float)
x[0] = x_t0


# -------- EULER -------- x(t+h) = x(t) + h f(x,t)
for i in range(1,int(N)):
	x[i] = x[i-1] + h*f(x[i-1],t[i-1])

# -------- MIDPOINT -------- x(t+h) = x(t) + k2
x1 = np.zeros(N,float)
t1 = np.arange(t_0,t_fin,h)
k1 = np.zeros(N,float)
k2 = np.zeros(N,float)
for i in range(1,int(N)):
	k1[i-1] = 0.5*h*f(x1[i-1],t1[i-1])
	k2[i-1] = h*f(x1[i-1]+k1[i-1],t1[i-1]+(0.5*h))
	x1[i] = x1[i-1] + k2[i-1]

# ------ RUNGE-KUTTA 4-TH ORDER ------
x2 = np.zeros(N,float)
t2 = np.arange(t_0,t_fin,h)
k21 = np.zeros(N,float)
k22 = np.zeros(N,float)
k23 = np.zeros(N,float)
k24 = np.zeros(N,float)
for i in range(1,int(N)):
	k21[i-1] = 0.5*h*f(x2[i-1],t2[i-1])
	k22[i-1] = 0.5*h*f(x2[i-1]+k21[i-1],t2[i-1]+(0.5*h))	
	k23[i-1] = h*f(x2[i-1]+k22[i-1],t2[i-1]+(0.5*h))
	k23[i-1] = h*f(x2[i-1]+k23[i-1],t2[i-1]+h)
	x2[i] = x2[i-1] + (1./6.)*(2*k21[i-1]+4*k22[i-1]+2*k23[i-1]+k24[i-1])

# ---- PLOTS ----
a = plt.plot(t,x,"b-",label='Euler')
b = plt.plot(t1,x1,"g-",label='Midpoint')
c = plt.plot(t2,x2,"r-",label='Runge-Kutta 4')
plt.xlabel('t')
plt.ylabel("x")
plt.ylim(-1,1)
plt.xlim(0,100)
plt.legend(loc='upper right')
plt.show()