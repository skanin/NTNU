svar = input("Vil du lese eller endre en fil? (r/w): ")
filnavn = input("Oppgi navn på filen: ")

if svar == "w":
    f = open(filnavn, "w")

    print("Skriv inn tekst som lagres til filen")
    print("Avslutt med å trykke enter (uten tekst)")


    tekst = " "
    while tekst != "":
        tekst = input("> ")
        if tekst != "":
            f.write(tekst + "\n")

    f.close()
    print("Teksten er lagret i " + filnavn)
elif svar == "r":
    f = open(filnavn, "r+")
    print(f.read())
