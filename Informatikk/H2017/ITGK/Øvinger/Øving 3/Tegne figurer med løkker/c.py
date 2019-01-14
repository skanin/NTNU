from turtle import *

x = 250
for i in range(36):
    forward(x)
    left(90)
    x = x - 7
done()

'''
While løkke:

lengde = 250
minskeMed = 7

while lengde > minskeMed:
    forward(lengde)
    left(90)
    lengde = lengde - minskeMed
done()
'''