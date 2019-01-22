filnavn = input("Oppgi navn på fila: ")
f = open(filnavn, "r")

innhold = f.read()
f.close()
print(innhold)


filnavn = input("Oppgi navn på fila: ")
try:
    f = open(filnavn, "r")
    teller = 1
    linje = f.readline()
    while linje:
        ren_linje = linje.strip()
        print(teller, ren_linje)
        teller += 1
        linje = f.readline()

except FileNotFoundError:
    print("Fant ikke fil med navn " + filnavn)
    filnavn = input("Oppgi et gyldig filnavn: ")
    f = open(filnavn, "r")
    teller = 1
    linje = f.readline()
    while linje:
        ren_linje = linje.strip()
        print(teller, ren_linje)
        teller += 1
        linje = f.readline()

f.close()
