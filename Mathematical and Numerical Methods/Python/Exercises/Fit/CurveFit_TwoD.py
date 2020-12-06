import numpy as np
from numpy import random as rnd
import matplotlib.pyplot as plt
from scipy import optimize as opt

plt.rcParams.update({'font.size':15})

def TwoD_gauss(xy,x0,y0,sx,sy,h):
	z = h*np.exp(-((xy[0]-x0)**2./(2.*sx*sx) + (xy[1]-y0)**2./(2.*sy*sy)))
	return z.ravel()

def data_set(): #create a mock of data set
	x = np.linspace(-5.,5.,num=500) #x data
	y = np.linspace(-5.,5.,num=500) #y data
	x,y = np.meshgrid(x,y)
	z = np.zeros([len(x),len(y)],float)

	x0 = 0.
	y0 = 0.
	sx = 1.
	sy = 0.7
	h = 1.

	xy = (x,y)
	z = TwoD_gauss(xy,x0,y0,sx,sy,h)
	z +=1e-1*rnd.normal(size=z.shape)
	return x,y,z

def sci_fit(x,y,z,x0,y0,sx,sy,h):
	xy=(x,y)
	popt,pcov = opt.curve_fit(TwoD_gauss,xy,z,p0=(x0,y0,sx,sy,h))
	return popt,pcov

x,y,z = data_set()

x0 = 0.
y0 = 0.
sx = 1.
sy = 0.7
h = 1.

popt,pcov = sci_fit(x,y,z,x0,y0,sx,sy,h)

perr = np.sqrt(np.diag(pcov)) #gives me the errors on the parameters

xy=(x,y)

print("x0=",popt[0],"+/-",perr[0])
print("y0=",popt[1],"+/-",perr[1])
print("sx=",popt[2],"+/-",perr[2])
print("sy=",popt[3],"+/-",perr[3])
print("h=",popt[4],"+/-",perr[4])

data_fitted=TwoD_gauss(xy, *popt) #fitted data with the caécuéated parameters

# --------PLOTS--------

figsize = plt.figaspect(1.0)
fig,ax = plt.subplots(1,1,figsize=figsize)
ax.set_xlim(-3,3)
ax.set_ylim(-3,3)

ax.contourf(x,y,z.reshape(len(x),len(y)),100,cmap=plt.cm.jet)
ax.contour(x,y,data_fitted.reshape(len(x),len(y)),8,colors='k')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.tight_layout()
plt.show()







