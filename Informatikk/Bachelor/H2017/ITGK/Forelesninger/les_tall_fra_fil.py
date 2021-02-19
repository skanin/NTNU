filnavn = input("Oppgi et filnavn: ")
f = open(filnavn, "r")

teller = 1
for linje in f:
    print(str(teller) + ".", int(linje)**3)
    teller += 1

f.close()