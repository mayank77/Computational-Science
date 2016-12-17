import math as mt
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
x = symbols('x')


def evaluate(n, x, a, t):
    result = []
    for b in range(0,101):
        pt = a[n]
        for i in range(n-1,-1,-1):
            pt = pt*(t[b]-x[i])+a[i]
        result.append(pt)
    return result


def coefficients(n, x, y):
    a = []
    for i in range(0, n+1):
        a.append(y[i])
    for j in range(1, n+1):
        for i in range(n,j-1,-1):
            a[i] = (a[i]-a[i-1])/(x[i]-x[i-j])
    return a

x = np.linspace(-2.02857, 2.02857, num=13)
t = np.linspace(-2.02857, 2.02857, num=101)
y = []
n = 12
p_x = []

#Calculating the values of 'y' to get coefficiants.
for i in range(0, 13):
    y.append(x[i] / (0.25+mt.pow(x[i], 2)))

coeff = coefficients(n, x, y)

#Generating the polynomial function, p(x)
for i in range(0, 101):
    p_x.append(t[i] / (0.25+mt.pow(t[i], 2)))

#Predict the function f(x)
f_x = evaluate(n, x, coeff, t)

#Calculating Mean Square Error
error = 0
e_x = []
for i in range(0, 101):
    error = error + mt.pow((f_x[i] - p_x[i]),2)/101
    e_x.append(mt.fabs(p_x[i] - f_x[i]))

plt.plot(t,p_x, color = 'red', label='p(x)')
plt.plot(t,f_x, color = 'blue', label='f(x)')
legend = plt.legend(loc='best', shadow=True)
plt.ylabel('Function Value')
plt.xlabel('X')
plt.show()
plt.plot(t,e_x, color = 'green', label='|p(x) - f(x)|')
legend = plt.legend(loc='best', shadow=True)
plt.ylabel('Error Value')
plt.xlabel('X')
plt.show()

print("Error with Uniform Distribution is : ", error)

c_node = []
for i in range(0, n+1):
    c_node.append((0.5*(-2.02857 + 2.02857)) + (0.5*(2.02857 - (-2.02857))*mt.cos((i*mt.pi/n))))
c_y = []
for i in range(0, 13):
    c_y.append(c_node[i] / (0.25+mt.pow(c_node[i], 2)))

c_coeff = coefficients(n, c_node, c_y)

#Predict the Chebyshev function f(x)
c_f_x = evaluate(n, c_node, c_coeff, t)

#Calculating Mean Square Error for Chebyshev
c_error = 0
c_e_x = []
for i in range(0, 101):
    c_error = c_error + mt.pow((c_f_x[i] - p_x[i]),2)/101
    c_e_x.append(mt.fabs(p_x[i] - c_f_x[i]))

plt.plot(t,p_x, color = 'red', label='p(x)')
plt.plot(t,c_f_x, color = 'blue', label='Chebyshev f(x)')
legend = plt.legend(loc='best', shadow=True)
plt.ylabel('Function Value')
plt.xlabel('X')
plt.show()
plt.plot(t,c_e_x, color = 'green', label='|p(x) - f(x)|')
legend = plt.legend(loc='best', shadow=True)
plt.ylabel('Error Value')
plt.xlabel('X')
plt.show()

print("Error with Chebyshev nodes is : ", c_error)