import numpy as np
import matplotlib.pyplot as plt
import time
from read_m1m2 import *

plt.rcParams.update({'font.size':15})

N=2330575 #file lines number
fname="time_Bhillustris1_30.txt"

start1=time.time()

m1,m2 = readm1m2(fname,N) #from the reading file I get the teo arrays for the masses

for i in range(len(m1)):
    if(m1[i]<m2[i]):
        m1[i],m2[i]=m2[i],m1[i]

dm=1
index1=np.zeros(len(m1),int)
index2=np.zeros(len(m2),int)

binx = np.arange(0,int(max(m1))+1,1) #Number of bins. It's necessary to add +1 because of
biny = np.arange(0,int(max(m2))+1,1) #the ticks on the axis are one more than the bins

Z=np.zeros([len(binx),len(biny)],int)
for i in range(len(m2)):
    index1[i]=int(m1[i]/dm)
    index2[i]=int(m2[i]/dm)
    Z[index1[i]][index2[i]]+=1  #filling the Z matrix

Z=np.transpose(Z) #transpose the Z because contourf needs it in this way
end1=time.time()
print("Tempo totale di esecuzione del programma:", end1-start1,"s")

cs=plt.contourf(binx,biny, Z, levels=10)
cbar = plt.colorbar(cs,orientation='vertical', )
cbar.solids.set_edgecolor("face")
cbar.set_label("$N_{merg}$")
plt.xlim(0,int(max(m1)))
plt.ylim(0,int(max(m2)))
plt.xlabel("$m_1 [M_{\odot}]$")
plt.ylabel("$m_2 [M_{\odot}]$")
plt.tight_layout()
plt.show()
