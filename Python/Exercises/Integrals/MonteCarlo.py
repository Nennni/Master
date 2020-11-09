import numpy as np
from numpy import random
import matplotlib.pyplot as plt

def f(x):
	f = (np.sin(1/(x*(2-x))))**2
	return(f)

N = [1e3 , 5e3 , 1e4 , 5e4 , 1e5 , 5e5 , 1e6 , 5e6]
np.random.seed(42)
s = np.zeros(len(N),float)
#k = [[],[],[],[],[],[],[],[]]
for n in range(len(N)):
	k=[]
	x = np.random.rand(int(N[n]))
	y = np.random.rand(int(N[n]))
	x1 = 2*x
	#z = (x1*x1 + y*y)**(0.5)
	p = [ x , y ]
	for j in range(int(N[n])):
		if (y[j] < f(x1[j])):
			k.append(x1[j])
			s[n] = len(k)
print(s)
A = 2.
I = np.zeros(8,float)
i=0
for i in range(8):
	I[i] = A*s[i]/N[i]
print(I)

a = plt.plot(N,I,'b.')
b = plt.plot(N,I,'r-')
plt.xlim(8e2,2e6)
plt.xlabel("N")
plt.ylabel("I")
plt.show()
