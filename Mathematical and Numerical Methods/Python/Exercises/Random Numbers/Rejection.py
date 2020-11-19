# --- REJECTION ---

import numpy as np
from numpy import random
import matplotlib.pyplot as plt

def gaussian(x):
    p = (1/(2*np.pi*sigma)**(0.5))*np.exp(-(x*x)/(2*sigma*sigma)) 
    return(p)
def f(x):
    f = 1.
    return(f)

N=int(1e6)
sigma = 2

massimo = 50
minimo = -50
np.random.seed(42)
a = np.random.rand(N)
y = a*(100)
x = y + minimo
x1 = []
np.random.seed(21)
m1 = np.random.rand(N)


for i in range(N):
    if (m1[i]<=gaussian(x[i])):
       x1.append(x[i])
        
mybins = np.arange(-10,10,0.3)

a = plt.hist(x1, bins=mybins, density = True, histtype = 'step')
plt.xlabel('X')
plt.ylabel('PDF(X)')
plt.xlim(-10,10)
plt.title('Rejection')
plt.show()