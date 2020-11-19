#examples/python/subplots.py

import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))   # gaussian distributed white noise 1
nse2 = np.random.randn(len(t))   # gaussian distributed white noise 2

# Signal that evolves as a sinusoid with time
s0s = np.sin(2 * np.pi * 10. * t)

# Signal that evolves as a cosinusoid with time
s0c = np.cos(2 * np.pi * 10. * t)


# Adding white noise to the sinusoidal signal
s1 = s0s + nse1
s2 = s0s + nse2


# Adding white noise to the cosinusoidal signal
s3 = s0c + nse1
s4 = s0c + nse2


fig, axs = plt.subplots(3, 2)
#print(axs)
#print(fig)
axs[0][0].plot(t, s0s, color="black")
axs[0][0].set_xlim(0, 2)
axs[0][0].set_xlabel('time')
axs[0][0].set_ylabel('Sinusoidal signal')
axs[0][0].grid(True)


axs[1][0].plot(t, s1)
axs[1][0].plot(t, s2)
axs[1][0].legend(["s1","s2"],ncol=2)
axs[1][0].set_xlim(0, 2)
axs[1][0].set_xlabel('time')
axs[1][0].set_ylabel('Signal+Noise')
axs[1][0].grid(True)


axs[2][0].plot(t, s1-s2)
axs[2][0].set_xlim(0, 2)
axs[2][0].legend(["s1-s2"],ncol=2)
axs[2][0].set_xlabel('time')
axs[2][0].set_ylabel('Residuals')
axs[2][0].grid(True)

axs[0][1].plot(t, s0c, color="black")
axs[0][1].set_xlim(0, 2)
axs[0][1].set_xlabel('time')
axs[0][1].set_ylabel('Co-sinusoidal signal')
axs[0][1].grid(True)

axs[1][1].plot(t, s3)
axs[1][1].plot(t, s4)
axs[1][1].legend(["s3","s4"],ncol=2)
axs[1][1].set_xlim(0, 2)
axs[1][1].set_xlabel('time')
axs[1][1].set_ylabel('Signal+Noise')
axs[1][1].grid(True)



axs[2][1].plot(t, s3-s4)
axs[2][1].set_xlim(0, 2)
axs[2][1].legend(["s3-s4"],ncol=2)
axs[2][1].set_xlabel('time')
axs[2][1].set_ylabel('Residuals')
axs[2][1].grid(True)




fig.tight_layout()
plt.show()

