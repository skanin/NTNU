import math


def f(x):
    y = (x-12)*math.e**(5*x)-8*(x+2)**2
    return y


def g(x):
    y = -x-2*x**2-5*x**3+6*x**4
    return y


print("f(0) = " + str(f(0)))
print("g(1) = " + str(g(1)))
