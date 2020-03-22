import math


def f(x):
    y = (x-12)*math.e**(5*x)-8*(x+2)**2
    return y


def derivate(h, x, func):
    dydx = (func(x+(h/2))-func(x-(h/2)))/h
    return float(dydx)


print(derivate(0.000001, -2, f))