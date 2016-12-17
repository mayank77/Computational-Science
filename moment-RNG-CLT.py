'''
kth moment analysis for LCG/SRGL. Central Limit Theorm Verification
'''

import numpy as np
from pylab import show,hist,subplot,figure

a = 128
b = 0
m = 509
x = np.random.rand(1) #for the initialization of the first value of 'x'
N = [10,100,1000,10000,100000,1000000,10000000]

def seed(x):
    global xi
    xi = x

def lcg():
    global xi
    xi = (a*xi + b)%m
    return xi/509
    
def moment(y,k,N):
    return ( sum(np.power(y,k)) / N)
  

for n in N:
    seed(x)
    y1 = []
    for i in range(n):
        y1.append(lcg())
    y2 = ( np.random.uniform(low=0, high=1, size=(n,)) )
    print "FOR", n
    for k in range(1,4):
        print "K =",k,"-> LCG : ", moment(y1,k,n)[0], " \& SRGL :", moment(y2,k,n), " \& Exact : ",1.0/(1+k)
    print "\n"    


def moment(y,k,N):
    return ( sum(np.power(y,k)) / N)
m = []
for i in range(0,10000):
    y2 = ( np.random.uniform(low=0, high=1, size=(100,)) )
    m.append(moment(y2,2,100))
    
hist(m, bins=100, range=[0.2, 0.5])




