import math as mt
import numpy
import matplotlib.pyplot as plt
n = 1000
N = []
error_imp = []
error_sample = []
va = []
va1 = []
for n in range(100,100000,1000):
    N.append(n)
    C =  9 / (mt.pow(2,9) - 1)
    y = numpy.random.uniform(low=0.0, high=1.0, size=n)
    x = []
    for i in range(0,len(y)):
        x.append( mt.pow( ((mt.pow(2,9)-1)*y[i] + 1),1.0/9.0 ) )
    sum_imp = 0
    for i in range(0,len(y)):
        sum_imp = sum_imp + ( 2*mt.pow(x[i],8) - 1 ) / (C*mt.pow(x[i],8))
    avg = sum_imp / len(y)
    va.append(avg)
    error_imp.append(numpy.abs(avg - (1013.0/9.0)))
    
    x_sample = numpy.random.uniform(low=1.0, high=2.0, size=1000)
    sum_sample = 0
    for i in range(0,len(x_sample)):
        sum_sample = sum_sample + 2*mt.pow(x_sample[i],8) - 1
    avg_sample = sum_sample/ len(x_sample)
    va1.append(avg_sample)
    error_sample.append(numpy.abs(avg_sample - (1013.0/9.0)))
    
plt.loglog(N,error_imp)
plt.loglog(N,error_sample)
