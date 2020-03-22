# a

import math
h = float(input("Høyden til tetraedet: "))
a = (3/math.sqrt(6))*h
o = math.sqrt(3)*(a**2)
print("Overflatearealet til et tetraeder med høyde " + str(h) + " er: " + str(o))


# b

v = (math.sqrt(2)*(a**3))/(12)
print("Volumet er: " + str(v))

# c
# Gjort i a og b
