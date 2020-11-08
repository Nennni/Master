#examples/plummer_new.py
#same as plummer.py but with less loops
import numpy as np
import matplotlib.pyplot as plt
import math


#constants
G=6.674e-8
pc=3.086e18
msun=1.989e33
kms=1.0e5

#parameters for salpeter
mini=0.1 
maxi=150.
asalp=2.3
#parameters for salpeter

#number of particles
N=1000
a=1.0 #scale of plummer/pc
sigma=0.5 #initial guess for 1d rms of the maxwellian / km/s



def salpeter(y,a,mini,maxi): #generate masses
    x=y*(maxi**(1.-a)-mini**(1.-a))+mini**(1.-a)
    x=x**(1./(1.-a))
    #print(x)
    return x

def set_phi(x): #generate phi
    phi=x*2.*math.pi
    return phi 
def set_theta(x): #generate theta
    theta=1.0-x*2.
    theta=np.arccos(theta)
    return theta

def set_radius(a,x): #generate radius
    radius=a/(x**(-2./3.)-1.)**0.5
    return radius

def gocart(r,theta,phi): #change from spherical to cartesian coord.
    x=r*np.sin(theta)*np.cos(phi)
    y=r*np.sin(theta)*np.sin(phi)
    z=r*np.cos(theta)
    return x,y,z



def gauss_r(x,sigma): #gaussian random numbers
    r=(-2.*sigma**2*np.log(1.-x))**0.5
    return r
def gauss_theta(x): #gaussian random numbers
    theta=2.*math.pi*x
    return theta

def coord(r,theta): #gaussian from r,theta to x,y
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    return x,y

def maxwell(vel): #maxwellian random numbers
    v=(vel[0]*vel[0]+vel[1]*vel[1]+vel[2]*vel[2])**0.5
    return v


def energy(m,x,v): #energy calculation (for the virial ratio)
    Ek=0.0
    Ep=0.0
    m=m*msun
    #m*=msun
    for i in range(len(m)):
        #vv=v[i,0]**2+v[i,1]**2+v[i,2]**2
        vv=(np.linalg.norm(v[i,:]))**2
        vv=vv*kms*kms
        Ek+=0.5*m[i]*vv
        for j in range(i+1,N):
            #r=((x[i,0]-x[j,0])**2+(x[i,1]-x[j,1])**2+(x[i,2]-x[j,2])**2)**0.5
            r=np.linalg.norm(x[i,:]-x[j,:])
            r=r*pc
            Ep-=G*m[i]*m[j]/r
    return(Ek,Ep)





np.random.seed(19)

#initialize masses [Msun], positions [pc], velocities [km/s]
m=np.zeros(N,float)

x=np.zeros((N,3),float)

vx=np.zeros((N,3),float)


f=open("plummer.dat","w") #plummer in phys units

f.write("# col.0: masses/msun, col.1: x/pc, col.2: y/pc, col.3: z/pc, col. 4:vx/kms, col. 5:vy/kms, col.6: vz/kms\n")


#calculate mass
y=np.random.rand(N)
m=salpeter(y,asalp,mini,maxi) #mass of particles Msun
mtot=sum(m) #total mass star cluster /Msun
print(mtot)



#calculate pos
x1=np.random.rand(N)
x2=np.random.rand(N)
x3=np.random.rand(N)
phi=set_phi(x1)
theta=set_theta(x2)
radius=set_radius(a,x3)
x[:,0],x[:,1],x[:,2]=gocart(radius,theta,phi)


#calculate vel
vel=np.zeros([3,N],float)
for j in range(len(vel)):
    x1=np.random.rand(N)
    x2=np.random.rand(N)
    temp1=gauss_r(x1,sigma)
    temp2=gauss_theta(x2)
    vel[j],temp=coord(temp1,temp2)
v=maxwell(vel)
x1=np.random.rand(N)
x2=np.random.rand(N)
phi=set_phi(x1)
theta=set_theta(x2)
vx[:,0],vx[:,1],vx[:,2]=gocart(v,theta,phi)



#################calculate virial ratio to rescale vel #########################
#print(m)
Ek,Ep=energy(m,x,vx)
#print(m)
Qvir=abs(2.*Ek/Ep)
print(Ek,Ep,Qvir)
sQvir=(Qvir)**0.5
for i in range(len(vx)):
    vx[i,0]/=sQvir
    vx[i,1]/=sQvir
    vx[i,2]/=sQvir
    ##### write output in phys units 
    f.write(str(m[i])+" "+str(x[i,0])+" "+str(x[i,1])+" "+str(x[i,2])+" "+str(vx[i,0])+" "+str(vx[i,1])+" "+str(vx[i,2])+"\n")

Ek,Ep=energy(m,x,vx)
Qvir=abs(2.*Ek/Ep)
print(Ek,Ep,Qvir)


#####PLOTS###############    
fig,axs=plt.subplots(2,2)
r=np.zeros(N,float)
binno=100
rho=np.zeros(binno,float)
rbin=np.zeros(binno,float)
rbin[0]=0.0
delta=20./binno
for i in range(1,binno,1):
    rbin[i]=rbin[i-1]+delta

r=(x[:,0]**2+x[:,1]**2+x[:,2]**2)**0.5


for i in range(N):
    for j in range(1,binno,1):
        if(r[i]<rbin[j]):
            rho[j]+=m[i]

#for j in range(1,binno,1):
#    rho[j]=rho[j]/(4./3.*math.pi*(rbin[j]**3-rbin[j-1]**3))

xx=np.zeros(N,float)
yy=np.zeros(N,float)
xx[0]=0.0
yy[0]=mtot*(xx[0]/a)**3 * (1.+(xx[0]/a)**2)**(-1.5)
delta=20./N
for i in range(1,N,1):
    xx[i]=xx[i-1]+delta
    yy[i]=mtot*(xx[i]/a)**3 * (1.+(xx[i]/a)**2)**(-1.5)

    
binning=np.logspace(np.log10(min(r)),np.log10(max(r)),num=20)
    
axs[0,0].hist(r,bins=binning,linewidth=2,density=True,histtype="step",log=True)
axs[0,0].set_xscale("log")
axs[0,0].set_xlabel("r (pc)")
axs[0,0].set_ylabel("PDF")



v=np.zeros(N,float)
v=(vx[:,0]**2+vx[:,1]**2+vx[:,2]**2)**0.5

binning=np.logspace(np.log10(min(v)),np.log10(max(v)),num=20)

axs[0,1].hist(v,bins=binning,range=(0.,25.),linewidth=2,density=True,log=True,histtype="step")
axs[0,1].set_xscale("log")
axs[0,1].set_xlabel("v (km/s)")
axs[0,1].set_ylabel("PDF")


axs[1,0].step(rbin,rho,linewidth=3)
axs[1,0].plot(xx,yy,color="red",linestyle="--")
axs[1,0].set_xlabel("r (pc)")
axs[1,0].set_ylabel("M(r) (M$_\odot$)")

axs[1,1].scatter(x[:,0],x[:,1],s=2,edgecolor="None",facecolor="blue")
axs[1,1].set_xlabel("x (pc)")
axs[1,1].set_ylabel("y (pc)")
axs[1,1].set_xlim(-10,10)
axs[1,1].set_ylim(-10,10)
#axs[1,1].scatter(y,z)
#axs[1,1].set_xlabel("y (pc)")
#axs[1,1].set_ylabel("z (pc)")


fig.tight_layout()
plt.show()
