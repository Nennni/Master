#Finding the eccentricity anomaly E: F=E-ecc*sin(E) 
#BISECTION METHOD
import numpy as np

def f(E,F,ecc):
	f = E - F - ecc*np.sin(E)  #f(x)=0
	return(f)

tol = 1e-6
F1 = np.pi/3.
ecc1 = float(input("ecc="))

#input the xrange
x1 = float(input("x1 ="))
x2 = float(input("x2 ="))

if (np.sign(f(x1,F1,ecc1))<0 and np.sign(f(x2,F1,ecc1))>0):	#opposite signs at the extremes
	while (abs(x1-x2)>tol): #accuracy
		xnew = 0.5*(x1+x2)
		if (np.sign(f(xnew,F1,ecc1))>0):
			print("The new interval is [",x1,",",xnew,"]")
			x2=xnew
		else:
			print("The new interval is [",xnew,",",x2,"]")
			x1=xnew

	print ("the final value of the root is:", xnew)
else:
		print("f(x3)=",f(x1,F1,ecc1),"\n","f(x4)=",f(x2,F1,ecc1),"\n","You need to choose another interval.")

F2 = np.pi
x3=float(input("x3="))
x4=float(input("x4="))

if (np.sign(f(x3,F2,ecc1))<0 and np.sign(f(x4,F2,ecc1))>0):
	while (abs(x3-x4)>tol):
		xnew2 = 0.5*(x3+x4)
		if (np.sign(f(xnew2,F2,ecc1))>0):
			print("The new interval is [",x3,",",xnew2,"]")
			x4=xnew2
		else:
			print("The new interval is [",xnew2,",",x4,"]")
			x3=xnew2
	
	print ("the final value of the root is:", xnew2)
else:
	print("f(x3)=",f(x3,F2,ecc1),"\n","f(x4)=",f(x4,F2,ecc1),"\n","You need to choose another interval.")

