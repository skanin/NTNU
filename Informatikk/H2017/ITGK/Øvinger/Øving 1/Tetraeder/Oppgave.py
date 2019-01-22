import math
'''
Oppgave a og b
h = 3
a = (3/(math.sqrt(6))) * h
A = math.sqrt(3)*math.pow(a,2)
V = (math.sqrt(2)*math.pow(a, 3))/12
print("Overflatearealet av tetraederet er: ", A)
print("Volumet til tetraederet er: ", V)     
'''

h = int(input("Skriv inn en sidelengde: "))
a = (3/(math.sqrt(6))) * h
A = math.sqrt(3)*math.pow(a,2)
V = (math.sqrt(2)*math.pow(a, 3))/12
print("Et tetraheder med høyde",h,"har volum",V,"og areal",A)