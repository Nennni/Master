import numpy as np

#------------------ BISECTION --------------------
print("------------ Bisection ------------")

def f(r):
	G = 6.674e-8 #cm^3 g^−1 s^−2
	Me = 5.974e27 #g
	Mm = 7.348e25 #g
	R = 3.844e10 #cm Distance Earth-Moon
	w = (G*Me/(R*R*R))**(0.5) #angular frequency of satellite and Moon
	f = G * ( Me/(r*r) - Mm/((R-r)*(R-r)) ) - w*w*r
	return(f)

tol = 1e5
#input the xrange
r1 = float(input("r1 ="))
r2 = float(input("r2 ="))

if (np.sign(f(r1))<0 and np.sign(f(r2))>0):	#opposite signs at the extremes
	while (abs(r1-r2)>tol): #accuracy
		rnew = 0.5*(r1+r2)
		if (np.sign(f(rnew))>0):
			#print("The new interval is [",r1,",",rnew,"]")
			r2=rnew
		else:
			#print("The new interval is [",rnew,",",r2,"]")
			r1=rnew

	print ("The lagrangian point is at r=", rnew)
else:
		print("f(r1)=",f(r1),"\n","f(r2)=",f(r2),"\n","You need to choose another interval.")
