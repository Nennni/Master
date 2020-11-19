#BOX-MULLER

import numpy as np
import matplotlib.pyplot as plt


def gaussian(z1,z2):

    x = ((-2*sigma*sigma*np.log(1-z1))**(0.5))*np.cos(2*np.pi*z2)
    y = ((-2*sigma*sigma*np.log(1-z1))**(0.5))*np.sin(2*np.pi*z2)
    return(x,y)

sigma = 2
N = int(1e5)

np.random.seed(42)
z1 = np.random.rand(N)  #random numbers uniform distributed between 0 and 1
np.random.seed(21)
z2 = np.random.rand(N)

x , y = gaussian(z1,z2)

mybins = np.arange(-10,10,0.3)

a = plt.hist(x, bins=mybins, density = True, histtype = 'step')
plt.xlabel('X')
plt.ylabel('PDF(X)')
plt.xlim(-10,10)
plt.title('Box-Muller')
plt.show()


