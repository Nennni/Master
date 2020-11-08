#------------ NEWTON - RAPHSON ------------

import numpy as np

def f(r):
	G = 6.674e-8 #cm^3 g^−1 s^−2
	Me = 5.974e27 #g
	Mm = 7.348e25 #g
	R = 3.844e10 #cm Distance Earth-Moon
	w = (G*Me/(R*R*R))**(0.5) #angular frequency of satellite and Moon
	f = G * ( Me/(r*r) - Mm/((R-r)*(R-r)) ) - w*w*r
	return(f)

def df(r):
	G = 6.674e-8 #cm^3 g^−1 s^−2
	Me = 5.974e27 #g
	Mm = 7.348e25 #g
	R = 3.844e10 #cm Distance Earth-Moon
	w = (G*Me/(R*R*R))**(0.5) #angular frequency of satellite and Moon
	df = 2*G*(-Me/(r*r*r) + Mm/((R-r)**3))-(w*w)
	return(df)

def d2f(r):
	G = 6.674e-8 #cm^3 g^−1 s^−2
	Me = 5.974e27 #g
	Mm = 7.348e25 #g
	R = 3.844e10 #cm Distance Earth-Moon
	d2f = 6*G*(-Me/(r*r*r*r) + Mm/((R-r)**4))
	return(d2f)

tol = 1e5
r = float(input("start with a guess of r="))
rold = float(input("Old value of r, rold="))
h = 1e-3
K=0
while(abs(r-rold)>tol):
	r1 = f(r)
	dr = ((f(r+0.5*h)) - f(r-0.5*h))/h  #This is the numerical derivative
	rold = r
	r = r - r1/dr
	K+=1
print("Number of iterations: ",K,"\n")
print("The Lagrangian point is at r=", r,"\n")