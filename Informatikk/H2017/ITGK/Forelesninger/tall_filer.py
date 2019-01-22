filnavn = input("Oppggi navn på filen: ")
f = open(filnavn, "w")

print("Skriv inn positive tall og tallet opphøyd i andre blir lagret")
print("Avslutt med å skrive -1")

tall = 0
while tall != -1:
    tall = int(input("> "))
    if tall != -1:
        tall = tall**2
        f.write(str(tall) + " \n")

f.close()
print("Tallene har blitt lagret til " + filnavn)
