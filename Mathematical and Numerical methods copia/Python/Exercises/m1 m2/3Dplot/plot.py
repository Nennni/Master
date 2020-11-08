import numpy as np
import matplotlib.pyplot as plt
import time
#from Read import *

plt.rcParams.update({'font.size':15})

N=10000 #file lines number
fname="time_Bhillustris1_30.txt"

#metall,m1,m2,t = read(fname,N)
metallicity,m1,m2,t = np.genfromtxt(fname , usecols=(3,6,7,8) , unpack=True , comments = "#" , max_rows=10000)

plus = m1 + m2
chirpm = (m1**(3./5.))*(m2**(3./5.))*((m1+m2)**(-1./5.))

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1, projection='3d')

ax.grid(b=True, color='grey', linestile='-', linewidth=2)

p = ax.scatter(plus, metallicity, t, c=chirpm ,  marker="o", label = " Chirp Mass [$M_{\odot}$] ")
fig.colorbar(p)
ax.set_xlabel("$ m_1 + m_2 [M_{\odot}] $")
ax.set_ylabel(" Progenitor's metallicity ")
ax.set_zlabel( " Delay time [Gyr] " )


plt.show()
