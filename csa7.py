import numpy as np
import matplotlib.pyplot as plt

x_train = [-9.7 ,-7.3 ,-5.4 ,-5 ,-3.01 ,-2.13 ,-1.2 ,-0.56 ,0 ,1.2 ,4.5 ,6.7 ,9.9 ,10 , 12.3]
y_train = [3.76 ,1.78 ,1.52 ,1.31 ,0.31 ,0.23 ,0.45 ,0.29 ,0 ,0.45 ,0.28 ,2.12 ,3.91 ,3.47 ,5.59]

x_test = [1000 ,1650 ,1800 ,1900 ,1950 ,1960 , 1970 , 1980 , 1990]
y_test = [0.34, 0.545, 0.907,1.61, 2.51, 3.15, 3.65, 4.2, 5.3]

def calc(x,y):
    n = len(x)
    
    def innerproduct(f, g):
        sum = 0
        for i in range ( 0,len(f) ):
            sum = sum + f[i]*g[i]
        return sum
    
    q = [[1 for d in range(n)] for e in range(n)]     
    
    a = []
    b = []
    c = []
    a.append( innerproduct([d*e for d,e in zip(x,q[0])],q[0]) / innerproduct(q[0],q[0]) )
    b.append(0)
    
    xqn = [d*e for d,e in zip(x,q[1])]
    a.append( innerproduct(xqn,q[1]) / innerproduct(q[1],q[1]) )
    b.append( innerproduct(xqn,q[0]) / innerproduct(q[0],q[0])  )
    q[1] = [d - a[0] for d in x]
    
    for i in range ( 2,n-1 ):
        xqn = [d*e for d,e in zip(x,q[i-1])]
        val1 = [j * a[i-1] for j in (q[i-1])]
        val2 = [j * b[i-1] for j in (q[i-2])]
        q[i] = [d-e-f for d,e,f in zip(xqn,val1,val2)]       
        xqn = [d*e for d,e in zip(x,q[i])]
        a.append( innerproduct(xqn,q[i]) / innerproduct(q[i],q[i]) )
        b.append( innerproduct(xqn,q[i-1]) / innerproduct(q[i-1],q[i-1])  )
        
    for i in range (0,n):
        c.append( innerproduct(y,q[i]) / innerproduct(q[i],q[i])  )
    
    p = []
    p.append( innerproduct(y,y) - ( ( innerproduct(y,q[0]) * innerproduct(y,q[0]) ) / innerproduct(q[0],q[0]) ) ) 
    
    for i in range (1,n):
        p.append( p[i-1] - ( ( innerproduct(y,q[i]) * innerproduct(y,q[i]) ) / innerproduct(q[i],q[i]) ) )   
        
    sigma = []
    for i in range (0,n):
        sigma.append(p[i]/(n - i))
    
    plt.scatter(x,y, color = 'g')
    y_res = []
    for i in range (0,n):
        sum = 0
        for j in range(0,4):
            sum = sum + ( np.power(x[i],j) * c[j] )
        y_res.append(sum)
    plt.plot(x,y_res, color = 'r')   
    print sigma

calc(x_train,y_train)
calc(x_test,y_test)