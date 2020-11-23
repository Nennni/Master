import numpy as np
import matplotlib.pyplot as plt

def f(x,t):
	f = np.exp(-x) + np.sin(t) 
	return f

t_0 = 0.0
t_fin = 200.
x_t0 = 0.0
h = 0.01
N = int((t_fin - t_0)/h)
H = int(t_fin-t_0)
t = np.arange(t_0,t_fin,h)

x = np.zeros(N,float) #integer multiple of h
x[0] = x_t0
y = np.zeros(N,float) #fractionary multiple of h
y[1] = x[0] + 0.5*h*f(x[0],t_0)
x[1] = x[0] +h*f(y[1],0.5*h)

for i in range(1,N-1): #index of x,y
	y[i+1] = y[i] + h*f(x[i],i*h)	
	x[i+1] = x[i] + h*f(y[i+1],(i+0.5)*h)
x[N-1] = 0.5*(x[N-1]+y[N-1]+0.5*h*f(x[N-1],t_fin))

graph = plt.plot(t,x,"b-")
plt.xlabel('t')
plt.ylabel('x(t)')
plt.tight_layout()
plt.show()