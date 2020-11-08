import numpy as np
from numpy import random
import matplotlib.pyplot as plt

#Constants and convert.
G=6.67430e-11 #gravitational constant in m^3 kg^-1 s^-2
msun=1.989e33
kms = 1e3 #m/s
pc = 3.0856778570831e16 #m
pcCGS = 3.0856778570831e18 #cm
kmsCGS = 1e5 #cm/s

#salpeter
a = 1. #pc

#Gaussian
sigma = 0.5 #km/s

# SPATIAL DISTRIBUTIONS
def Phi(z):
	phi = 2*np.pi*z
	return(phi)
def Theta(z):
	theta = np.arccos(1.- 2.*z)
	return(theta)
def R(z):
	r = a/((z**(-2./3.) -1)**(0.5))
	return(r)

# VELOCITY
def gaussian(z1,z2,z3,z4):
    x = ((-2*sigma*sigma*np.log(1-t1))**(0.5))*np.cos(2*np.pi*t2)
    y = ((-2*sigma*sigma*np.log(1-t1))**(0.5))*np.sin(2*np.pi*t2)
    z = ((-2*sigma*sigma*np.log(1-t3))**(0.5))*np.cos(2*np.pi*t4)
    return(x,y,z)

# ENERGY
def E(m,x,v):
	Ek = 0.0
	Ep = 0.0
	m = m*msun
	for i in range(len(m)):
		vv = v[:,0]**2 + v[:,1]**2 + v[:,2]**2
		#vv=(np.linalg.norm(v[i,:]))**2
		vv=vv*kms*kms
		Ek = Ek + 0.5*m*vv
		for j in range(i+1,N):
			r=np.linalg.norm(x[i,:]-x[j,:])
			r=r*pc
			Ep = Ep - G*m[i]*m[j]/r
	return(Ek,Ep) 

N = int(1e3)

np.random.seed(42)
z1 = np.random.rand(N)
z2 = np.random.rand(N)
z3 = np.random.rand(N)

phi = Phi(z1)
theta = Theta(z2)
r = R(z3)

x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(phi)

pos = np.zeros((N,3),float)
pos[:,0] = x
pos[:,1] = y
pos[:,2] = z 

r = (pos[:,0]**2 + pos[:,1]**2 + pos[:,2]**2)**(0.5)

# ------ SALPETER ------

Mm = 0.1  #Msun
M = 150 #Msun
alfa = 2.3
m = np.zeros(int(N),float)
for i in range(int(N)):
    x1 = np.random.rand()
    m[i] = ( ( (M**(1.-alfa)) - (Mm**(1.-alfa)) )*x1 +Mm**(1.-alfa) )**(1/(1.-alfa))
Mt = sum(m)
print("Total mass =",Mt)

Mr = Mt *(r/a)**3 * (1 + (r/a)**2)**(-3./2.)

# ----------------------

# --- VELOCITY DISTRIBUTION---

t1 = np.random.rand(N) 
t2 = np.random.rand(N)
t3 = np.random.rand(N)
t4 = np.random.rand(N) 

vx , vy , vz = gaussian(t1,t2,t3,t4)

V = np.zeros((N,3),float)
V[:,0]= vx 
V[:,1] = vy 
V[:,2] =  vz
v = (V[:,0]**2 + V[:,1]**2 + V[:,2]**2)**(0.5)


# ----------------------------------

# --- CLUSTER AND VIRIAL EQUILIBRIUM 2K/|W| = 1

K=0.0
W=0.0

K,W = E(m,pos,V)

Q = 2.*K/abs(W)
print("Ek,W,Q =",K,W,Q)
rQ = Q**0.5
for i in range(3):
	V[:,i]=V[:,i]/(Q**0.5)
v = (V[:,0]**2 + V[:,1]**2 + V[:,2]**2)**(0.5)
K1,W1 = E(m,pos,V)
Q1 = 2.*K1/abs(W1)

print("new values of Ek,W,Q =",K1,W1,Q1) 

# ---------------------------------------------


# SUBPLOTS

fig, axs = plt.subplots(2, 2)

# TOP LEFT: PDF(r)
a = np.log10(0.1)
b = np.log10(30)
mybins0 = np.logspace(a,b,num=100)
axs[0][0].hist(r, bins=mybins0, density = True, histtype = 'step',log = 'True')
#axs[0][0].set_xlim(0,20)
axs[0][0].set_xscale('log')
axs[0][0].set_xlabel('r [pc]')
axs[0][0].set_ylabel('PDF')
axs[0][0].grid(True)

#TOP RIGHT: PDF(v)
a1 = np.log10(0.05)
b1 = np.log10(200)
mybins1 = np.logspace(a1,b1,num=50)
axs[0][1].hist(v, bins=mybins1, density = True, histtype = 'step', log = 'True')
axs[0][1].set_xscale('log')
#axs[0][1].set_ylim(0.001,0.1)
axs[0][1].set_xlabel('v [Km/s]')
axs[0][1].set_ylabel('PDF')
axs[0][1].grid(True)

#BOTTOM LEFT: M(r)
axs[1][0].plot(r,Mr,'r,')
axs[1][0].set_xlabel('r [pc]')
axs[1][0].set_xlim(0,20)
axs[1][0].set_ylabel('M(r) [$M_{\odot}$]')
axs[1][0].grid(True)

#BOTTOM RIGHT: y(x)
axs[1][1].plot(x,y,'r,')
axs[1][1].set_xlabel('x [pc]')
axs[1][1].set_xlim(-20,20)
axs[1][1].set_ylim(-20,20)
axs[1][1].set_ylabel('y [pc]')
axs[1][1].grid(True)

plt.tight_layout()
plt.show()