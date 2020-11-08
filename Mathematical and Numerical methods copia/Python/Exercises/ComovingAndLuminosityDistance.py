#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def integrand(x):
    OmegaM=0.2726 #Omega matter
    OmegaL=0.7274 #Omega Lambda
    c=300000000 #Velocità della luce
    f = c/((OmegaM*(1+z)**3 + OmegaL)**0.5 )
    return f

def comoving(z):
    H0=67.2 #Hubble constant in Km/s/Mpc
    convert=1e5/3.086e24*3.1536e7*1e9 #converts from Km/s/Mpc to Gyr
    comov=integrate.quad(integrand, 0.0, z)
    
    Cdistance=comov[0]
    Cdistance/=(H0*convert)
    return Cdistance

#MAIN

z=10
ComovingDistance = []
Redshift =[]
while(z>0.0):
    ComovingDistance.append(comoving(z))
    Redshift.append(z)
    z-=0.1
print("Here is the list of Comoving distance with respect to the Redshift")
for n in range(len(ComovingDistance)):
    print(ComovingDistance[n], "    ", Redshift[n])

  
def luminosityD(y):
    l=(1+y)*comoving(y)
    return l

#MAIN

y=10
LuminosityDistance = []
while(y>0.0):
    LuminosityDistance.append(luminosityD(y))
    y-=0.1
print("Here is the Luminosity distance with respect to the Redsfift")
for n in range(len(LuminosityDistance)):
    print(LuminosityDistance[n], "    " , Redshift[n])
    
    
x=np.array(Redshift)
y=np.array(ComovingDistance)
y2=np.array(LuminosityDistance)

a=plt.plot(x, y,'r.')
b=plt.plot(x,y2,'b.')
plt.xlabel('Redshift', fontsize=15)
plt.ylabel('$D_C, D_L (Gpc)$', fontsize=15)
plt.axis([0,10,0,3e10])
plt.legend(['Comoving Distance', 'Luminosity Distance'], fontsize=15, loc='upper right')
plt.show()


    
    
    

