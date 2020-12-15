import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy.fft import fft2,ifft2,fftshift

fname='AVG_Stack1.jpg'
im = cv2.imread(fname,0)
imgf0 = np.fft.fft2(im)
imgf1 = np.fft.fftshift(imgf0)

Acf = np.fft.ifft2(np.abs(imgf1)**2)
Acf = np.fft.fftshift(Acf)

plt.imshow(abs(Acf),cmap='magma')
plt.show()