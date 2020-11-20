import numpy as np
import matplotlib.pyplot as plt

def f(x,t):
	f = -x**3 + np.sin(t) 
	return f

t_0 = 0.0
t_fin = 200.
x_t0 = 0.0
h = 0.01
N = (t_fin - t_0)/h
H = int(t_fin-t_0)
t = np.arange(t_0,t_fin,h)
x = np.zeros(int(N),float) #integer multiple of h
x[0] = x_t0
y = np.zeros(int(N),float) #fractionary multiple of h
y[0] = x_t0

for i in range(1,int(N)-1):
	y[i] = y[i-1] + 0.5*h*f(x[i-1],t[i-1]+(i-1)*h)
	x[i] = x[i-1] + h*f(y[i],t[i-1]+(i-1+0.5)*h)
X =0.0
X1 = np.zeros(len(t),float)
T=0.
i=0
while (abs(T-t_fin)>1e-10):
	X = 0.5*(x[int(N)-1]+y[int(N)-1]+0.5*h*f(x[int(N)-1],T+H))
	X1[i] = X
	T+=h
	i+=1

graph = plt.plot(t,X1,"b-")
plt.xlabel('t')
plt.ylabel('x(t)')
plt.tight_layout()
plt.show()