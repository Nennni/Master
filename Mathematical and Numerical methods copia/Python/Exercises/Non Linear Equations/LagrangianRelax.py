#LAGRANGIAN POINT EARTH-MOON

import numpy as np


#------------------ RELAXATION --------------------
print("------------ Relaxation ------------")
G = 6.674e-8 #cm^3 g^−1 s^−2
Me = 5.974e27 #g
Mm = 7.348e25 #g
R = 3.844e10 #cm Distance Earth-Moon
w = (G*Me/(R*R*R))**(0.5) #angular frequency of satellite and Moon
rold = 1e10
r = 100.
tol = 1e2
K=0
while (abs(r-rold)>tol):
	if (abs(r-R)<tol):
		continue
	else:
		rold = r
		r = (1/(w*w))*(G*Me/(r*r)-(G*Mm)/((R-r)*(R-r)))
		print(r)
		K+=1
print("The lagrangiant poin is at r=", r)










