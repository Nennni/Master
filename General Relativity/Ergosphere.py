import numpy as np
import matplotlib.pyplot as plt

r = np.arange(1,6,0.1)
Omega_1 = 1/(r+1)
Omega_2 = (2-r)/((r**2)-r+2)

graph = plt.plot(r,Omega_1,color="violet",linestyle='-',label='$\Omega_{+}$')
graph1 = plt.plot(r,Omega_2,color="blue",linestyle='-',label='$\Omega_{-}$')
plt.xlabel(' r/GM ')
plt.ylabel('GM$\Omega$')
plt.legend(loc='upper right')
plt.ylim(-0.18,0.55)
plt.show()