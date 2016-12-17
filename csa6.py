import string
import numpy as np
from matplotlib import pyplot as plt
data = open('titanium.dat').readlines()
data = map(string.strip, data)
data = map(string.split, data)
t, y = zip(*data)
t = map(float, t)
y = map(float, y)
N = len(data)
h = []
b = []
u = []
v = []
z = []
for i in range(0,N-1):
    h.append( t[i+1] - t[i] )
    b.append( ( y[i+1] - y[i] )/h[i] )
u.append(0)
v.append(0)
u.append(2*(h[0]+h[1]))
v.append(6*(b[1]-b[0]))

for j in range(2,N-1):
    u.append( 2*(h[j]+h[j-1]) - ( (h[j-1]*h[j-1])/u[j-1] ) )
    v.append( 6*(b[j]-b[j-1]) - ( (h[j-1]*v[j-1])/u[j-1] ) )
    
for j in range(N-1,-1,-1):   
    z.append(0)
    
for i in range(N-2,0,-1): 
    z[i] = ( v[i] - (h[i]*z[i+1]) )/ u[i]
z[0] = 0


x = np.linspace(600, 1000, num=100)
result = []
for i in x:   
    count = 0
    for count in range(N-1,-1,-1): 
        if (i-t[count]>=0):
            break           
    h1 = t[count+1]-t[count]
    tmp = 0.5*z[count] + (i-t[count])*(z[count+1]-z[count])/(6.0*h1)
    tmp = -(h1/6.0)*(z[count+1]+2.0*z[count])+(y[count+1]-y[count])/h1 + (i-t[count])*tmp
    result.append(y[count] + (i-t[count])*tmp)

plt.plot(x, result)


result1 = []
for i in x:   
    count = 0
    for count in range(N-1,-1,-1): 
        if (i-t[count]>=0):
            break           
    h1 = t[count+1]-t[count]
    tmp = 0.5*z[count] + (i-t[count])*(z[count+1]-z[count])/(6.0*h1)
    tmp1 = -(h1/6.0)*(z[count+1]+2.0*z[count])+(y[count+1]-y[count])/h1 + (i-t[count])*((z[count+1]-z[count])/(6.0*h1))
    tmp1 = tmp1 + tmp
    result1.append(y[count] + (i-t[count])*tmp1)


plt.plot(x, result1)
