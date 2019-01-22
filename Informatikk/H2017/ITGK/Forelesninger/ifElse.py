'''
#Sammenlikne heltall

puls = int(input("Skriv inn din puls "))

if puls >= 80:
    print("Ro deg ned!")
else:
    print("Bare slapp av")
'''
'''
#Sjekke to tekststrenger

navn1 = "Peter"
navn2 = "Pelle"

if (navn1==navn2):
    print("Samme navn!")
else:
    print("Forskjellige navn!")
'''
'''
#Sjekke om strenger er like/hvem som er størst

streng1 = input("Skriv inn en tekststreng ")
streng2 = input("Skriv inn enda en tekststreng ")

if(streng1 == streng2):
    print("Strengene er like!")
else:
    if(streng1>streng2):
        print("Streng1 > Streng2")
    else:
        print("Streng1 < Streng2")
'''
print("Hei, jeg er THE DOORMAN")
navn = input("Hva er ditt navn? ")
alder = int(input("Hva er din alder? "))

if(alder>18):
    print("Du er gammel nok")
    full = input("Er du full (J/N)? ")
    if(full == "n"):
        print("Velkommen inn ",navn)
    else:
        print("Du slipper ikke inn, du er for full!")
else:
    print("Du er for ung",navn)
