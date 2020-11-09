import numpy as np
import matplotlib.pyplot as plt

Mm = 0.1  #Msun
M = 150 #Msun
alfa = 2.3
k = (1.-alfa)/((M**(1.-alfa))-(Mm**(1.-alfa)))
N=1e3
m = np.zeros(int(N),float)
pdf = np.zeros(int(N),float)
np.random.seed(42) #to allow reproducibility
for i in range(int(N)):
    x = np.random.rand()
    m[i] = ( ( (M**(1.-alfa)) - (Mm**(1.-alfa)) )*x +Mm**(1.-alfa) )**(1/(1.-alfa))
    
a = (np.log10(Mm))
b = np.log10(M)

Mt = sum(m)
print(Mt)

mybins = np.logspace(a,b,num=30)

n = plt.hist(m, bins = mybins, density = True , log=True,histtype='step' )
plt.xlabel("M [$M_{\odot}{$]")
plt.xscale('log')
plt.ylabel('PDF')
plt.title("Inverse Random Sampling")
plt.grid(True)
plt.show()
