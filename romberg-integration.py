'''
Romberg Integration
'''

import math as mt
from sympy import *
x = symbols('x')
function1 = 1/(1+x)
function2 = exp(x)
function3 = pow(x, 0.5)


def f(y, function):
    return function.evalf(subs={x: y})


def romberg(function, lower, upper, iterations):
    R = [[0 for x in range(iterations+1)] for y in range(iterations+1)]
    h = upper - lower
    R[0][0] = (h/2)*(f(lower,function)+f(upper,function))
    kmax = 1
    for i in range(1,iterations+1):
        h = h/2
        summ = 0
        kmax = kmax*2;

        for k in range(1,kmax,2):
            summ += f(lower+k*h,function)
        R[i][0] = 0.5*R[i-1][0]+summ*h

        for j in range(1,i+1):
            R[i][j] = R[i][j-1] +(R[i][j-1]-R[i-1][j-1])/(mt.pow(4,j)-1)
    return R

print(romberg(function1,0,2,10))
print(romberg(function2,0,1,10))
print(romberg(function3,0,1,10))
