'''
def weather():
    sted = input("Skriv inn et sted: ")
    temperatur = int(input("Skriv inn temperatuen: "))
    if temperatur < 0:
        print("I " + sted + " er det kaldt vintervær")
    elif 1 <= temperatur <= 9:
        print("I " + sted + " er det typisk Trønder-vær")
    else:
        print("i " + sted + " er det sommervær")

weather()
'''
'''
def c2f():
    celsius = float(input("Celsius: "))
    fahrenheit = (celsius * (9/5)) + 32

    print("Fahrenheit: " + str(fahrenheit))


def f2c():
    fahrenheit = float(input("Farhernheit: "))
    celsius = (fahrenheit -32) * (5/9)

    print("Celsius: " + str(celsius))


def main():
    c2f()
    f2c()

main()
'''
import math


def areal_sirkel(raduis, pi):
    a = pi * (raduis**2)
    print("En sirkel med radius lik " + str(raduis) + " er " + str(a))


areal_sirkel(5, math.pi)