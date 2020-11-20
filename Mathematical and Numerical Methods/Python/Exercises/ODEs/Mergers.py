import numpy as np
import matplotlib.pyplot as plt

def euler(e0,a0,h):
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
t=0

# -------- EULER -------- x(t+h) = x(t) + h f(x,t)    CONSTANT h
while (abs(a-aLSO)/aLSO>tol and iterate<1e5):
		anew,enew=euler(e,a,h)
		agraph.append(anew/au)
		egraph.append(enew)
		a=anew
		e=enew
		iterate+=1
		t+=h
t = np.arange(0,t+1,h)
t*=3.17e-8
# ------ EULER -------  ADAPTIVE h
a1 = 0.1*au
e1 = 0.7
agraph1=[a1/au]
egraph1=[e1]
t1=0
tgraph1=[t1]
iterate1 = 0

while (abs(a1-aLSO)/aLSO>tol and iterate1<1e5):
	anew1,enew1=euler(e1,a1,h)
	if (abs(anew1-a1)/a1 < 0.1*1e-2):
		h = 2*h
		anew1,enew1=euler(e1,a1,h)			
	elif (abs(anew1-a1)/a1 > 1e-2):
		while(abs(anew1-a1)/a1 > 1e-2):
			h=h/10.
			anew1,enew1=euler(e1,a1,h)
	agraph1.append(anew1/au)
	egraph1.append(enew1)
	a1=anew1
	e1=enew1
	iterate1+=1
	t1+=h
	tgraph1.append(t1)
tgraph1=np.array(tgraph1)
tgraph1*=3.17e-8

# ----- PLOTS -----
fig, axs = plt.subplots(2)
axs[0].plot(t,agraph,'b-',label='Constant h')
axs[0].plot(tgraph1,agraph1,'r.',label='Adaptive h')
axs[0].set_xscale('log')
axs[0].set_xlim(1e2,1e9)
axs[0].set_ylim(-0.1,0.15)
axs[0].set_xlabel('time [yr]')
axs[0].set_ylabel('a [AU]')
axs[0].legend(loc='lower left')
axs[1].plot(t,egraph,'b-',label='Constant h')
axs[1].plot(tgraph1,egraph1,'r.',label='Adaptive h')
axs[1].set_xlim(1e2,1e9)
axs[1].set_ylim(-0.2,0.8)
axs[1].set_xscale('log')
axs[1].set_xlabel('time [yr]')
axs[1].set_ylabel('e')
axs[1].legend(loc='lower left')

fig.tight_layout()
plt.show()