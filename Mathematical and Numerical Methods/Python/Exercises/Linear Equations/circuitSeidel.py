import numpy as np

a = [[4.,-1.,-1.,-1.] , [-1.,3.,0.,-1.],[-1.,0,3.,-1.],[-1.,-1.,-1.,4.]]
b = np.array([5.,0.,5.,0.],float)
x = np.zeros(len(b),float)
a = np.array(a,float)
xold = np.zeros(len(b),float)
epsilon=np.array([1e-5,1e-5,1e-5,1e-5],float)

x[:]=2
xold[:]=10
K=0
while (np.any(abs(x[:]-xold[:])>epsilon[:])):
	xold = np.copy(x)
	for i in range(len(b)):
		x[i] = (1/(a[i,i]))*(b[i])
		for j in range(len(b)):
			if (j!=i):
				x[i] += (1/a[i,i])*(-a[i,j]*x[j])
	K+=1
	print(x)
print(K)
	
