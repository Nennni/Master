#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:56:30 2020

@author: FrancescoIraci
"""

#from Readchirpmasstmerg import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

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



cs=plt.contourf(tmerg, chirpm , Z, levels=100, locator=ticker.LogLocator() , cmap='Reds')
cbar = plt.colorbar(cs,orientation='vertical')
cbar.solids.set_edgecolor("face") 
cbar.set_label('$N_{merg}$') 
plt.xlabel("$t_{merg} [Gyr]$") 
plt.ylabel("$m_{chirp} [M_{\odot}]$")
plt.xlim(0,14)
plt.ylim(0,40)
plt.tight_layout()
plt.show()
