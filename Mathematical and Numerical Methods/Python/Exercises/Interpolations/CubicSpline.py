import numpy as np
import matplotlib.pyplot as plt

def f(x,xi,xi1,yi,yi1,ki,ki1):
	a = ki/6. * ( ((x-xi1)**3)/(xi-xi1) - (xi-xi1)*(x-xi1) )
	b = ki1/6. * (  ((x-xi)**3)/(xi-xi1) -(xi-xi1)*(x-xi) )
	f = a-b
	return f  

N = 18
x = np.arange(0,18,1.)
y = np.sin(x)
k = np.zeros(N,float)
A = np.zeros([N-2,N-2],float)
A[0,0] = 2*(x[0]-x[2])
A[0,1] = x[1]-x[2]

for i in range(1,N-2): #rows
	for j in range(0,N-2): #columns
		if ((i-j)==1):
			A[i,j]=x[i]-x[i+1]
		if i==j:
			A[i,j] = 2*(x[i]-x[i+2])
		if (i-j)==(-1):
			A[i,j] = x[i+1]-x[i+2]
print(A)
y1 = np.zeros(N-2,float)
for i in range(len(y)):
	if i < len(y)-2:
		y1[i] = 6*( (y[i]-y[i+1])/(x[i]-x[i+1]) - ((y[i+1])-y[i+2])/(x[i+1]-x[i+2])  )   
print(y1)

K = np.linalg.solve(A,y1)
for i in range(len(K)):
	k[i+1] = K[i]

# Calculate the interpolation line
x1 = np.arange(0,18,0.2)
fun=np.zeros(len(x1),float)
for i in range (len(x1)-1):
	for j in range(0,len(k)-1):
		#for n in range(len(y)-1):
		fun[i] = f(x1[i],x[j],x[j+1],y[j],y[j+1],k[j],k[j+1])+(y[j]*(x1[i]-x[j+1]) - y[j+1]*(x1[i]-x[j]))/(x1[j] - x[j+1])
		#fun[0] = 

graph = plt.plot(x,y,"bo",label='Data')
graph1 = plt.plot(x1,fun,"r.",label='Interpolation')
plt.xlabel(" $x$ ")
plt.ylabel("$f(x)$")
plt.legend(loc='lower left')
plt.show()





