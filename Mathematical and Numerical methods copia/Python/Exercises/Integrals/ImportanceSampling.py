import numpy as np
from numpy import random
import matplotlib.pyplot as plt

def f(x):
	f = (x**(-0.5))/(np.exp(x)+1)
	return(f)

def w(x):
	w = x**(-0.5)
	return(w)

def p(x):
	p = 0.5 * x**(-0.5)
	return(p)

def fw(x): # g = f/w
	g = (np.exp(x)+1)**(-1)
	return(g)

random.seed(42)

# ------ MEAN VALUE METHOD ------

N = [1e3 , 5e3 , 1e4 , 5e4 , 1e5 , 5e5 , 1e6 , 5e6]
N = np.array(N)
fmedio = np.zeros(len(N),float)
I = np.zeros(len(N),float)

for i in range(len(N)):
	r = []
	x = np.random.rand(int(N[i]))
	x1 = 1*x
	for j in range(int(N[i])):
		r.append(f(x1[j]))
	I[i] = sum(r) *1/N[i]
print('Integrals with mean value method:' , I)

# ------ IMPORTANCE SAMPLING METHOD ------

I1 = np.zeros(len(N),float)
for i in range(len(N)):
	g=[]
	y = np.random.rand(int(N[i]))
	x = y**2
	for j in range(int(N[i])):
		g.append(fw(x[j]))
	I1[i] = 2*sum(g)/N[i]

print('Integrals with importance sampling method:',I1)


# ------ PLOTS ------

#I = np.log10(I)
#I1 = np.log10(I1)
#myrange = np.logspace(1e3,6e6)
a = plt.plot(N,I,'r.',label='Mean Value method')
b = plt.plot(N,I,'b-')
c = plt.plot(N,I1, color='#cc7722' , marker='1',label='Importance Sampling')
d = plt.plot(N,I1,'g-')
plt.xlabel('N')
plt.ylabel('I')
plt.xscale('log')
plt.xlim(1e3,5e6)
plt.legend(loc='upper right')


plt.tight_layout()
plt.show()