import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft,irfft
from cmath import exp,pi
import time as time

fname = 'sunspots.txt'
month,spots = np.genfromtxt(fname,dtype='float',comments='#',usecols=(0,1), unpack = True)

#plot spots vs months
graph=plt.plot(month,spots)
plt.xlabel('Month')
plt.ylabel('Sunspot number')
plt.xlim(0,len(month))
plt.show()
N = len(spots)

# ------- FFT --------
start = time.time()
print('--------FFT--------')
c = rfft(spots)
k = []
cabs = abs(c)
maxc=0.
frequency = 0.
for i in range(N//2+1): #calculate the highest |ck|
	if(cabs[i]>maxc and i>0):
		maxc=cabs[i]
		frequency = i/float(N)
		period = 1./(12*frequency) # in years
	k.append(i)


print('|ck|max:',maxc,'\n','frequency:',frequency,"month^-1","\n","Period:",period,"yrs")

#plot |ck| vs k
graph2 = plt.plot(k,cabs)
plt.xlabel('k',fontsize=20)
plt.ylabel('|c$_k$|',fontsize=20)
plt.xlim(0,len(k))
plt.ylim(0,50000)
plt.show()

#denoise data
threshold = 2000.
for i in range(len(cabs)):
	if cabs[i]<threshold :
		c[i] = 0.0

y = irfft(c)
m = range(len(y))

#-------PLOT with denoise
a = plt.plot(month,spots,color='navy',linewidth=1.5,label="Signal")
b = plt.plot(m,y,linewidth=2,color='coral',label="De-noised signal")
plt.xlabel("Month")
plt.ylabel("Sunspots Number")
plt.legend(loc = 'upper right',fontsize=15)
plt.show()

end = time.time()
print("time fft=",end-start,"seconds")
print("--------DFT--------")
ck = np.zeros(N,float)
#for i in range(len(ck)):
#	ck[i] =  


