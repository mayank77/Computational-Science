import math as mt
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
x = symbols('x')
z = []
function1 = 4/(1+pow(x, 2))
function2 = cos(2*x)/exp(x)
line = []
space = np.linspace(0, 1, num=100)


def f(y, function):
    line.append(y)
    return function.evalf(subs={x: y})


def simpson(a, b, eps, level, level_max, function):
    #result = 0
    #kmax = 1
    h = b - a
    c = (a+b)/2
    one_simpson = h*(f(a, function)+4.0*f(c, function)+f(b, function))/6.0
    d = 0.5*(a+c)
    e = 0.5*(c+b)
    two_simpson = h*(f(a, function)+4.0*f(d, function)+2.0*f(c, function)+4.0*f(e, function)+f(b, function))/12.0
    if level+1 >= level_max:
        result = two_simpson
    else:
        if mt.fabs(two_simpson-one_simpson) < 15.0*eps:
            result = two_simpson + (two_simpson-one_simpson)/15.0
        else:
            left_simpson = simpson(a,c,eps/2.0,level+1,level_max,function)
            right_simpson = simpson(c,b,eps/2.0,level+1,level_max,function)
            result = left_simpson + right_simpson
    return result

print(simpson(0, 1, 0.00005, 1, 30, function1))


for i in range(0,100):
    z.append(f(space[i], function1))
for j in range(0,len(line)):
    plt.axvline(x=line[j])
plt.plot(space,z)
plt.show()

print(simpson(0, 2*mt.pi, 0.00005, 1, 30, function2))

z = []
line = []

for i in range(0,100):
    z.append(f(space[i], function2))
for j in range(0,len(line)):
    plt.axvline(x=line[j])
plt.plot(space,z)
plt.show()