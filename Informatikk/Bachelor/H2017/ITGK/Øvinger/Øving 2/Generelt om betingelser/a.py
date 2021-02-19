a = int(input("Skriv inn et tall a: "))
b = int(input("Skriv inn et tall b: "))

gange = a * b
addere = a + b

if gange < addere:
    print(a,"*",b,"=",gange)
elif addere < gange:
    print(a,"+",b,"=",addere)
