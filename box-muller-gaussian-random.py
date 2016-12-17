'''
Box-Muller algorithm to create Gaussian distributed random numbers with uniform RNG.
'''

import numpy as np
from pylab import show,hist,subplot,figure

def gaussian(u1,u2):
  z1 = np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2)
  z2 = np.sqrt(-2*np.log(u1))*np.sin(2*np.pi*u2)
  return z1,z2

u1 = np.random.rand(100000)
u2 = np.random.rand(100000)

z1,z2 = gaussian(u1,u2)

figure()
subplot(221) 
hist(u1)     
subplot(222)
hist(u2)
subplot(223)
hist(z1, bins=100, range=[-5, 5])
subplot(224)
hist(z2, bins=100, range=[-5, 5])
show()
