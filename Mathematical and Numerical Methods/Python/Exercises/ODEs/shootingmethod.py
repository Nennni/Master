import numpy as np
import matplotlib.pyplot as plt

g = 9.81
N = int(1e3)
h = 3./1e3
t_0 = 0.
t_fin = 3.
x_t0 = 0.
xtrue = 10.
epsilon = 1e-3
x = np.zeros(N,float)
v = np.zeros(N,float)
v[0] = 18.0520
xold = 1.
i=0
for i in range(1,N):
	v[i] = v[i-1]+h*(-g)
	x[i] = x[i-1]+h*v[i]
if (abs(x[N-1]-xtrue)>epsilon):
	print("change the initial value of v(0)")
	print(abs(x[N-1]-xtrue))

else:
	t = np.arange(t_0,t_fin,h)
	Xgraph = plt.plot(t,x,"b-",label='x(t)')
	Vgraph = plt.plot(t,v,"r-",label='v(t)')
	plt.xlabel('t [s]')
	plt.legend(loc='lower left')
	plt.tight_layout()
	plt.show()
