import numpy as np
import matplotlib.pyplot as plt

# ------ NEWTON POLYNOMIAL ------

def coeff(xData,yData):
	n = len(xData)
	a=np.copy(yData)
	for k in range(1,n):
		for j in range(k,n):
			a[j] = (a[j]-a[k-1])/(xData[j]-xData[k-1])
	return a

def evalPoly(a,xData,x):
	n = len(xData)-1
	p = a[n]
	for k in range(1,n+1):
		p = a[n-k]+(x-xData[n-k])*p # forse è solo p[k] alla fine
	return p

def NewtonPoly(xData,yData,x):
	a = coeff(xData,yData)
	p = evalPoly(a,xData,x)
	return p
Ndata = 10
xData = np.zeros(Ndata,float)
yData = np.zeros(Ndata,float)
x = np.zeros(100,float)
for i in range (len(xData)):
	xData[i] = float(i*0.5)
	yData = xData*xData
for i in range(len(x)):
	x[i] = float(i*0.5/float(Ndata+1))

y = NewtonPoly(xData,yData,x)

graph = plt.plot(xData,yData,'k.')
graph1 = plt.plot(x,y,'g-.')
plt.tight_layout()
plt.show()


