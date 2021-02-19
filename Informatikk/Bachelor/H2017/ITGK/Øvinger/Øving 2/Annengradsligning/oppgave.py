print("Her skal jeg fortelle deg om du får 1, 2 eller imaginær løsning på en annengradslikning på formen ax^2+bx+c")
a = int(input("Skriv inn a: "))
b = int(input("Skriv inn b: "))
c = int(input("Skriv inn c: "))

d = (b**2)-(4*a*c)

if d < 0:
    print("Du vil få 2 imaginære løsninger")
elif d > 0:
    print("Du vil få 2 reelle løsninger")
else:
    print("Du vil få 1 reell løsning")
