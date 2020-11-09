import numpy as np


a = [[4.,-1.,-1.,-1.] , [-1.,3.,0.,-1.],[-1.,0,3.,-1.],[-1.,-1.,-1.,4.]]
b = np.array([5.,0.,5.,0.],float)
A = np.array(a,float)
x = np.zeros(len(b),float)

print("The linear equation system is Ax=B")
print("A =",A)
print("b=",b)
print("\n")

# all the diagonal element becomes 1
for i in range(len(b)):
	temp=A[i,i]
	for j in range(len(b)):
		A[i,j] /= temp
	b[i]/=temp
# subtract the lines to obtain an upper triangular matrix
	for k in range(i+1,len(b)):
		temp = A[k,i]
		for j in range(len(b)):
			A[k,j] -= temp*A[i,j]
		b[k] -= temp*b[i]		
		
print("After Gauss elimination: A =",A, "\n")
print("and b=",b)
print("\n")

#backsubstitution
for i in range(len(b)-1 , -1 , -1):
	x[i] += b[i]
	for j in range (len(b)-1,i,-1):
		x[i] -=  A[i,j]*x[j]

print("The solution is: ", x)
print("\n")
