import numpy as np
import matplotlib.pyplot as plt

def F(alpha):
	F = np.exp(-alpha*alpha)
	return F

z = np.arange(-5.,15.,0.1)
t = np.array([0.,1.,2.],float)
alpha = np.zeros([len(t),len(z)],float)

for j in range(len(t)):
	for i in range(len(z)):
		alpha[j,i] = z[i] - 6*t[j]

graph = plt.plot(z[:],F(alpha[0,:]),linestyle='-',linewidth=1,label='t = 0s')
graph1 = plt.plot(z[:],F(alpha[1,:]),linestyle='-',linewidth=1,label='t = 1s')
graph2 = plt.plot(z[:],F(alpha[2,:]),linestyle='-',linewidth=1,label='t = 2s')
plt.xlabel('x')
plt.ylabel('F(z-6t)')
plt.tight_layout()
plt.grid()
plt.legend(loc='upper right')
plt.show()