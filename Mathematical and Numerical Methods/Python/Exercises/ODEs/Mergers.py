import numpy as np
import matplotlib.pyplot as plt

def euler(e0,a0):
	a = a0+h*((-64./5.)*((G**3*m1*m2*(m1+m2))/(c**5 * a0*a0*a0 *(1-e0*e0)**(3.5)))*(1+(73./24.)*e0*e0 + (37./96.)*e0*e0*e0*e0))
	e = e0+h*((-304./15.)*e0*((G**3*m1*m2*(m1+m2))/(c**5 * a0**4 *(1-e0*e0)**(2.5)))*(1+(121./304.)*e0*e0))
	return (a,e)

G = 6.67e-11 #m^3/s^2
c = 3e8 #m/s
Msun = 1.989e30 #Kg
m1 , m2 = 30.*Msun , 30.*Msun #Msun
au = 1.496e11 #m
a = 0.1*au #m
e = 0.7 #eccentricity
h = 3.1536e10 #1e3 yr
rsc = 2*G*(m1+m2)/c**2
aLSO = 3*rsc
tol = 1e-1
iterate = 0
agraph=[a/au]
egraph=[e]


# -------- EULER -------- x(t+h) = x(t) + h f(x,t)
while (abs(a-aLSO)/aLSO>tol and iterate<1e5):
		anew,enew=euler(e,a)
		agraph.append(anew/au)
		egraph.append(enew)
		a=anew
		e=enew
		iterate+=1
t = np.arange(1,len(agraph)+1,1)
t=t*1e3

# ----- PLOTS -----
fig, axs = plt.subplots(2)
axs[0].plot(t,agraph,'b-',label='Constant h')
axs[0].set_xscale('log')
axs[0].set_xlabel('time [yr]')
axs[0].set_ylabel('a [AU]')
axs[0].legend()
axs[1].plot(t,egraph,'b-',label='Constant h')
axs[1].set_xscale('log')
axs[1].set_xlabel('time [yr]')
axs[1].set_ylabel('e')
axs[1].legend()

fig.tight_layout()
plt.show()