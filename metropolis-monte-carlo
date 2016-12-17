'''
Metropolis Monte Carlo simulation of the 2D Ising model in zero field (H = 0) and on a square L x L lattice
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

L = 32
lattice = [[ np.round(np.random.uniform(0.0, 1.0)) for x in range(L)] for y in range(L)] 
X = []
Y = []
for x in range(L):
    X.append(x)
    Y.append(x)
    for y in range (L):
        if lattice[x][y] == 0:
            lattice[x][y] = -1.0

spin = lattice
T = 2.265
M = np.sum(lattice)
def energy(spin):
    e = 0
    for x in range(L):
        for y in range (L):
            if x == L-1:
                nn1 = spin[0][y]
            else:
                nn1 = spin[x+1][y]
            if y == L-1:
                nn2 = spin[x][0]
            else:
                nn2 = spin[x][y+1]
            e = e + nn1 + nn2
    return e

E = energy(spin)
internal = [E/(L*L)]
energies = [E]
magnetization = [M/(L*L)]

def nn(x,y):
    
    if x == 0:
        nn0 = spin[L-1][y]
    else:
        nn0 = spin[x-1][y]
        
    if x == L-1:
        nn1 = spin[0][y]
    else:
        nn1 = spin[x+1][y] 
        
    if y == L-1:
        nn2 = spin[x][0]
    else:
        nn2 = spin[x][y+1]
    
    if y == 0:
        nn3 = spin[x][L-1]
    else:
        nn3 = spin[x][y-1]
        
    return  nn0 + nn1 + nn2 + nn3   
    
    
def deltaE(x, y, spin, L):
    dE = 2.0 * spin[x][y] * nn(x,y) 
    return dE

MCS = [0]

for mcs in range(10000):
    MCS.append(mcs+1)
    x = []
    y = []
    
    for i in range(L*L):
        x.append(int(np.random.uniform(0.0, 1.0)*L))
        y.append(int(np.random.uniform(0.0, 1.0)*L))
        
    for i in range(L*L):
        dE = deltaE(x[i],y[i],spin,L);
        wij = [ np.exp(-4.0/T), np.exp(-8.0/T) ]    
            
        if dE <= 0:
            accept=1;
        elif np.random.uniform(0.0, 1.0) <= wij[int(dE/4) - 1]:
            accept=1;
        else:
            accept=0;
            
        if accept==1:
            spin[x[i]][y[i]] = -1*spin[x[i]][y[i]]
            M = M + 2*spin[x[i]][y[i]]
            E = E + dE*1.0
    energies.append(E)
    internal.append(E/(L*L))
    magnetization.append(M/(L*L))
'''
plt.plot(MCS,internal)
plt.plot(MCS,magnetization)
plt.xlabel('time (MCS)')
plt.ylabel('internal energy / magnetization')

for x in range(L):
    for y in range (L):
        if spin[x][y] == -1:
            print u'\xb0'.encode('utf8'),
        else:
            print u'\x95'.encode('utf8'),
    print ""
 '''   
print np.mean(magnetization)
print np.mean(np.abs(magnetization))
