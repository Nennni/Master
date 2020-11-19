#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:56:30 2020

@author: FrancescoIraci
"""

from Read_chirpmass_tmerg.py import *
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 15})

fname1="chirpmass_bin.txt"
N1=201

fname2="tmerg_bin.txt"
N2=1402

chirpm=readchirpmass(fname1,N1)
tmerg=readtmerg(fname2,N2)

Z,xedges,yedges=np.histogram2d(tmerg,chirpm,bins=25,density=False) 
x=np.zeros(len(xedges)-1)
y=np.zeros(len(xedges)-1)
for i in range(len(xedges)-1):
    x[i]=(xedges[i]+xedges[i+1])/2. 
    y[i]=(yedges[i]+yedges[i+1])/2.

Z=np.transpose(Z)

cs=plt.contourf(x,y, Z, levels=10)
cbar = plt.colorbar(cs,orientation='vertical')
cbar.solids.set_edgecolor("face") 
cbar.set_label('$N_{merg}$') 
plt.xlabel("$t_{merg} [Gyr]$") 
plt.ylabel("m_{chirp} M_{\odot}")
plt.tight_layout()
plt.show()
