#from Readchirpmasstmerg import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import matplotlib.colors as colors

plt.rcParams.update({'font.size': 15})

#fname1="chripmass_bin.txt"
#N1=201

#fname2="tmerg_bin.txt"
#N2=1402

#chirpm=readchirpmass(fname1,N1)
#tmerg=readtmerg(fname2,N2)

chirpm=np.genfromtxt("chripmass_bin.txt", comments="#")
tmerg=np.genfromtxt("tmerg_bin.txt", comments="#")
Z=np.genfromtxt("chirpmass_tmerg_tot.txt", comments="#")

L = int(100)
# -------- PLOTS --------
#norm=colors.LogNorm(), cmap='Reds'
cs=plt.contourf(tmerg, chirpm , Z, levels=L)
cs1 = plt.contour(tmerg, chirpm , Z, levels=100, norm = colors.LogNorm(),cmap='summer')
cbar = plt.colorbar(cs,orientation='vertical')
cbar.solids.set_edgecolor("face") 
cbar.set_label('$N_{merg}$') 
plt.xlabel("$t_{merg} [Gyr]$") 
plt.ylabel("$m_{chirp} [M_{\odot}]$")
plt.xlim(0,14)
plt.ylim(0,40)
plt.tight_layout()
plt.show()
