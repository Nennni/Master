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
y[0] = x_t0

for i in range(1,N): #index of x,y
	y[i] = y[i-1] + 0.5*h*f(x[i-1],(i-1)*h)	
	x[i] = x[i-1] + h*f(y[i],(i-1+0.5)*h)
	X.append(y[i])
	X.append(x[i])
x[N-1] = 0.5*(x[N-1]+y[N-1]+0.5*h*f(x[N-1],t_fin))

graph = plt.plot(t,X,"b-")
plt.xlabel('t')
plt.ylabel('x(t)')
plt.tight_layout()
plt.show()