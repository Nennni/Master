import numpy as np

a = [[2. ,1. ,4. ,1.],[3. , 4. , -1. ,-1],[1. ,-4. ,1 ,5.],[2. ,-2. ,1. ,3.]]

b = [-4. , 3. , 9. , 7.]
N=4
A = np.array(a,float)
b = np.array(b,float)
x = np.zeros(N,float)

print("The linear equation system is Ax=B")
print("A =",A)
print("b=",b)
print("\n")

# all the diagonal element becomes 1
for i in range(N):
	temp=A[i,i]
	for j in range(N):
		A[i,j] /= temp
	b[i]/=temp
# subtract the lines to obtain an upper triangular matrix
	for k in range(i+1,N):
		temp = A[k,i]
		for j in range(N):
			A[k,j] -= temp*A[i,j]
		b[k] -= temp*b[i]		
		
print("After Gauss elimination: A =",A)
print("and b=",b)
print("\n")

#backsubstitution
for i in range(N-1 , -1 , -1):
	x[i] += b[i]
	for j in range (N-1,i,-1):
		x[i] -=  A[i,j]*x[j]

print("The solution is: ", x)
print("\n")
