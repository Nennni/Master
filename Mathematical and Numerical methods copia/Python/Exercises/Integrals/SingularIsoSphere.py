import numpy as np
from numpy import random
import matplotlib.pyplot as plt

def f(r):
	 f = 2*sigma*sigma/G
	 return(f)

sigma = 10. #km/s
r_max = 10. #pc
r_min = 0.
G = 4.3009e-3 #pc (Km/s)^2 Msun^-1
k = 1
N = 1000 #number of division of the interval
h = r_max/N
I=0.0
for k in range(N):
	I += h*f(k*h)
I += h*(1/2*f(r_min)+1/2*f(r_max)) # Msun
print('Trapezoidal integral',I)

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
print('Monte Carlo Itegrals:' , I1)

a = plt.plot(N1,I1,'r.')
b = plt.plot(N1,I1,'b-')
plt.xlabel('N')
plt.ylabel('I')
plt.xlim(1e2,1e6)
plt.ylim(465018.94951437,465018.94956355)

plt.tight_layout()
plt.show()