import math


#A
def f(x):
    return (x - 12) * math.exp(x/2) - 8 * (x + 2) ** 2


def g(x):
    return -x - 2 * x ** 2 - 5 * x ** 3 + 6 * x ** 4


#b
def differentiate(x_k, x_k1, func):
    return (func(x_k) - func(x_k1))/(x_k - x_k1)


#c
def secant_method(x0, x1, func, tol):
    x = differentiate(x0, x1, func)

    while