hemmelig_ord = input("Skriv inn det hemmelige ordet: ")  #Hemmelig ord fra brukeren
antall_liv = int(input("Hvor mange forsøk får brukeren? "))  #Antall liv gitt av brukeren
hemmelig_hint = list(hemmelig_ord)  #Lager en "hint" variabel
hint = None  #Deklarerer hint variablen, uten verdi, så det ikke skal oppstå errorer
gjettede_bokstaver = ""

for i in range (0, len(hemmelig_ord)):
    hemmelig_hint[i] = "*"                  #Setter alle bokstavene i listen "hemmelig_hint" til stjerner

while True:
    bokstav = input("Gjett en bokstav: ")  #Bruker gjetter en bokstav


    if(bokstav in hemmelig_ord):
        print("Riktig, bokstaven er i ordet!")  #Hvis bokstaven er riktig, skal dette printes ut
        gjettede_bokstaver += bokstav  #Legger til den riktige bokstaven i en variabel

        for i in range(0, len(hemmelig_ord)):
            if(hemmelig_ord[i] == bokstav):
                hemmelig_hint[i] = bokstav  #Loopen går igjennom alle bokstavene i "Hemmelig_ord" og hvis når den finner en som er lik
                                            #den gjettede bokstaven, skal * i hemmelig_hint, som er på samme plassen som bokstaven
                                            #byttes ut med den riktige bokstaven
        hint = "".join(hemmelig_hint)   #Hint variablen settes til en string fra listen "hemmelig_hint"
        print("Hint: ", hint)   #Printer hintet, nå med stjerner for bokstaver som ikke er gjettet

    elif(bokstav not in hemmelig_ord):  #Hvis bokstaven ikke finnes i det hemmelige ordet, skal brukeren miste et liv
        print("Bokstaven", bokstav, "er ikke i ordet")
        antall_liv = antall_liv - 1
        print("Du har nå", antall_liv, "liv igjen")

    if ("*" not in hint):   #Hvis det ikke er flere * i hint variablen, har brukeren gjettet alle bokstavene og vunnet. Loopen avsluttes
            print("Du vant! Det hemmelige ordet var \"", hemmelig_ord, "\"")
            break

    if(antall_liv == 0):    #Brukeren taper om liv er 0.
        print("Du tapte!")
        break
