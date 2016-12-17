'''
Estimate of π using the "hit-or-miss" Monte Carlo method with error approximation
'''

import numpy
from decimal import *
import matplotlib.pyplot as plt

numpy.random.seed(23455) ;
n = 1000
N = []
ratio = []
error = []
allv = []
for i in range(0,30):
    N.append( numpy.log(1000 + (i*1000)) )
    for measurement in range(0,10):
        n_circle = 0
        val = []     
        for j in range(0,n):
            x = 2*numpy.random.rand(1) - 1.0
            y = 2*numpy.random.rand(1) - 1.0
            if (x*x + y*y < 1):
                n_circle = n_circle + 1
        val.append(( 1.0*n_circle/n ) * 4)
        allv.append(val)
    ratio.append(numpy.mean(val))
    error.append(numpy.log(abs(numpy.mean(val) - 3.141592654)))
    n = n + 1000
plt.plot( N , error ) 
