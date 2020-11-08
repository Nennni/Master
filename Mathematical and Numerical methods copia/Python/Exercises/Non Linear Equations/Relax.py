#RELAXATION METHOD

import numpy as np

tol = 1e-6
x1 = 1.0
xold1 = 10.
F1=np.pi/3.
ecc1=0.1
while(abs(x1-xold1) > tol):
	xold1 = x1
	x1 = F1 + ecc1*np.sin(x1)
print("converged to: E1=", x1)

x2=1.
xold2=10.
F2=np.pi/3.
ecc2=0.7
while(abs(x2-xold2) > tol):
	xold2 = x2
	x2 = F2 + ecc2*np.sin(x2)
print("converged to: E2=", x2)
							
x3=1.	             
xold3=10.
F3=np.pi/3.
ecc3=0.9			
while(abs(x3-xold3) > tol):
	xold3 = x3
	x3 = F3 + ecc3*np.sin(x3)
print("converged to: E3=", x3)
