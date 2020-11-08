#NEWTON-RAPHSON METHOD and Numerical Derivative

import numpy as np

def f(E,F,ecc):
	f = E - F - ecc*np.sin(E)
	return(f)

def df(E,ecc):
	df = 1-ecc*np.cos(E)
	return(df)

def d2f(E,ecc):
	d2f = ecc*np.sin(E)
	return(d2f)

tol = 1e-6
F = np.pi/3.
ecc = float(input("ecc="))
E = float(input("F=pi/3, start with a guess of E="))
Eold = float(input("Old value of E, Eold="))
K=0

h=1e-3

while(abs(E-Eold)>tol):
	E1 = f(E,F,ecc)
	dE1 = df(E,ecc)
	#dE = ((f(E+0.5*h,F,ecc)) - f(E-0.5*h,F,ecc))/h  This is the numerical derivative
	Eold = E
	#E = E - E1/dE   This would be the calculation with numerical derivative switched ON
	E = E - E1/dE1
	K+=1
print("Number of iterations: ",K,"\n")
print("The root is: E=", E,"\n")

F2 = np.pi
E2 = float(input("F=pi, start with a guess of E="))
Eold2 = float(input("Old value of E, Eold="))
N=0
while(abs(E2-Eold2)>tol):
	E1 = f(E2,F2,ecc)
	dE1 = df(E2,ecc)
	Eold2 = E2
	E2 = E2 - E1/dE1
	N+=1
print("Number of iterations: ",N,"\n")
print("The root is: E=", E2 ,"\n")

