from math import sqrt as rot

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

d = (b**2 - 4*a*c)

likning = "Andregradsligningen " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " har "


if d < 0:
    print(likning + "to imaginære løsninger")
else:
    likningPluss = (-b + rot(d)) / (2 * a)
    likningMinus = (-b - rot(d)) / (2 * a)
    if d > 0:
        print(likning + "de to reelle løsningene " + str(likningPluss) + " og " + str(likningMinus))
    else:
        print(likning + "en reell dobbelrot " + str(likningPluss))

