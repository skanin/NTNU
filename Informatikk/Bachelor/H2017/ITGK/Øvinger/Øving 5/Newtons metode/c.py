import math


def f(x):
    y = (x-12)*math.e**(5*x)-8*(x+2)**2
    return y


def derivate(h, x, func):
    dydx = (func(x+(h/2))-func(x-(h/2)))/h
    return float(dydx)


def g(x):
    y = -x-2*(x**2)-5*(x**3)+6*(x**4)
    return y


def newtons_method(h, x, func, tol):

    while True:
        x_ny = x - f(x)/derivate(h, x, func)
        if abs(x_ny-x) < tol:
            return x_ny
        else:
            x -= f(x)/derivate(h, x, func)


toleranse = float(input("Skriv inn en toleransegrense: "))

print("Funksjonen nærmer seg et nullpunkt når x = " + str(newtons_method(0.00000001, -2, f, toleranse)) + " da er y = ",
      f(newtons_method(0.00000001, -2, f, toleranse)))
print("Funksjonen nærmer seg et nullpunkt når x = " + str(newtons_method(0.00000001, -2, f, toleranse)) + " da er y = ",
      f(newtons_method(0.00000001, 1, g, toleranse)))
print("Funksjonen nærmer seg et nullpunkt når x = " + str(newtons_method(0.00000001, -2, f, 0.0000000001)) + " da er y = " +
      str(f(newtons_method(0.00001, -1, g, 0.00001))))