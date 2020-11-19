import numpy as np 
from numpy import random
import matplotlib.pyplot as plt
import time

begin = time.time()
def f(x):
	f = (np.sin(1/(x*(2-x))))**2
	return f

random.seed(42)

N = [1e3 , 5e3 , 1e4 , 5e4 , 1e5 , 5e5 , 1e6 , 5e6]
N = np.array(N)
fmedio = np.zeros(len(N),float)
I = np.zeros(len(N),float)

for i in range(len(N)):
	r = []
	x = np.random.rand(int(N[i]))
	x1 = 2*x
	for j in range(int(N[i])):
		r.append(f(x1[j]))
	I[i] = sum(r) *2/N[i]
print('I risultati degli integrali sono:' , I)

end = time.time()
print("Per sto cazzo di programma ci metto addirittura:", end-begin,"secondi")

a = plt.plot(N,I,'r.')
b = plt.plot(N,I,'b-')
plt.xlabel('N')
plt.ylabel('I')
plt.ylim(1.40,1.48)
plt.xlim(1e3,5e6)

plt.tight_layout()
plt.show()