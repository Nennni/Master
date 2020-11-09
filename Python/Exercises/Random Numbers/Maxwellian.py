# MAXWELLIAN 

import numpy as np
import matplotlib.pyplot as plt


def gaussian(z1,z2,z3,z4):

    x = ((-2*sigma*sigma*np.log(1-z1))**(0.5))*np.cos(2*np.pi*z2)
    y = ((-2*sigma*sigma*np.log(1-z1))**(0.5))*np.sin(2*np.pi*z2)
    z = ((-2*sigma*sigma*np.log(1-z3))**(0.5))*np.cos(2*np.pi*z4)
    return(x,y,z)

sigma = 265. # km / s

N = int(1e5)

np.random.seed(42)
z1 = np.random.rand(N)  #random numbers uniform distributed between 0 and 1
np.random.seed(21)
z2 = np.random.rand(N)
np.random.seed(10)
z3 = np.random.rand(N)
np.random.seed(12)
z4 = np.random.rand(N)

x , y , z = gaussian(z1,z2,z3,z4)

v = (x*x + y*y + z*z)**(0.5)

maxi = np.log10(1000)
mybins = np.logspace(0,maxi,70)

a = plt.hist(v, bins=mybins, density = True, histtype = 'step')
plt.xlabel('3-D speed [Km/s]')
plt.xscale('log')
plt.ylabel('Probability density')
plt.xlim(0,1000)
plt.title('Maxwell')
plt.grid()
plt.show()