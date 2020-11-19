import numpy as np
from numpy import random
import matplotlib.pyplot as plt

def f(r):
	f = 4*np.pi*r*rho_0/( (1/rs)*(1+r/rs)**2 )
	f1 = (4*np.pi*r*rho_0*rs**3)/((r+rs)**2)
	return(f1)

rho_0 = 1e8 #Msun kpc^-3
rs = 10 #kpc
r_max = 100*rs #kpc
r_min = 0.
pc = 3.0856778570831e16 #m

I = 0.0
N = 4000
h = r_max/N
k = 1
for k in range(N):
	I += h * f(k*h)
I += h*(1/2*f(r_min)+1/2*f(r_max)) # Msun
print("Integral with trapezoidal rule:",I)

# -------- MONTE CARLO INTEGRATION --------

random.seed(42)

N1 = [1e3 , 5e3 , 1e4 , 5e4 , 1e5 , 5e5 , 1e6 , 5e6]
N1 = np.array(N1)
fmedio = np.zeros(len(N1),float)
I1 = np.zeros(len(N1),float)

for i in range(len(N1)):
	r = []
	x = np.random.rand(int(N1[i]))
	x1 = x*(r_max)
	for j in range(int(N1[i])):
		r.append(f(x1[j]))
	I1[i] = sum(r)
	I1[i] *= r_max/N1[i]
print('Itegrals results:' , I1)

a = plt.plot(N1,I1,'r.')
b = plt.plot(N1,I1,'b-')
plt.xlabel('N')
plt.ylabel('I')
plt.xlim(1e2,1e6)

plt.tight_layout()
plt.show()