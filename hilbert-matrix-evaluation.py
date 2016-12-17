'''
Evaluation of Hilbert Matrix Gaussian elimination with scaled partial pivoting with RMS error analysis.
'''

import numpy as np
import matplotlib.pyplot as plt
vals = [2,5,8,12,15]

error = []
for cnt in vals:
    N = cnt
    total = 0
    a = np.ndarray((N, N))
    b = []
    l = []
    s = []
    x=[0]*(N)
    
    for i in range(0,N):
        su = 0
        for j in range(0,N):
            a[i][j] = 1.0/(i+j+1);
            su = su + a[i][j]
        b.append(su)
        
        
    for i in range(0,N):
        l.append(i)
        smax = 0
        for j in range(0,N):
            aa = np.abs(a[i][j])
            if aa > smax:
                smax = aa
        s.append(smax)
    
    for k in range(0,N-1):
        rmax = 0;
        j=k
        for i in range(k,N):
            r = np.abs(a[l[i]][k]/s[l[i]])
            if r > rmax:
                rmax = r;
                j = i;
        temp = l[j];
        l[j] = l[k];
        l[k] = temp;
        for i in range(k+1,N):
            xmult = a[l[i]][k]/a[l[k]][k];
            a[l[i]][k] = xmult;
            for j in range(k+1,N):
                a[l[i]][j] = a[l[i]][j] - xmult*a[l[k]][j];
    
    #################
    
    for k in range(0,N-1):
        for i in range(k+1,N):
            b[l[i]] = b[l[i]]-a[l[i]][k]*b[l[k]]
    
    x[N-1]= b[l[N-1]]/a[l[N-1]][N-1]
    
    for i in range(N-2,-1,-1):
        sum = b[l[i]]
        for j in range(i+1,N):
            sum = sum - a[l[i]][j]*x[j]
        x[i] = sum/a[l[i]][i];
        total = total + np.abs(x[i] - np.round(x[i]))
    total = (1.0/N)*np.sqrt(total)
    error.append(total)
plt.plot(vals, error)
