import math
'''
h = 10**-3
x = 3.14
f1 = math.sin(x)
f2 = math.sin(x+h)

derivert = (f2 - f1)/(h)
print(derivert)
'''
h = float(input("Skriv inn et tall H: "))
x = float(input("Skriv inn et tall X: "))
f1 = math.sin(x)
f2 = math.sin(x+h)
derivert = (f2 - f1)/(h)
print("Derivert:", format(derivert, '.2f'))
