# Hovedmodulen main

# Importer modulerer som skal brukes av main

import bruker  # Brukergrensesnitt (bruker.py)
import fil  # Filbehandling (fil.py)

# Opprette variabler og initier dem (gi dem verdier)

db = {}  # Oppretter en tom dictionary som skal lagre regnskap.
dbid = 0  # id til dictionarin som settes til 0

# Gi en varm velkomst til bruker
bruker.velkommen()  # Skriver ut velkomst til bruker

# Gi en valgmeny til bruker
valg = bruker.valgmeny()  # Lar bruker velge hva han/hun vil gjøre


while valg != "avslutt":
    if valg == "utgift" or valg == "inntekt":
        dbid += 1
        db = bruker.registrer(db, dbid, valg)
    elif valg == "vis":
        bruker.vis(db)
    elif valg == "fjern":
        db = bruker.fjern(db)  # Fjerner innslag i ditionarien
    elif valg == "save":
        filnavn = bruker.velgFilnavn()  # Spør bruker om filnavn
        fil.save(db, filnavn)  # Lagrer dictionary til fil
    elif valg == "load":
        filnavn = bruker.velgFilnavn()
        db = fil.load(filnavn)  # Laster inn dictionary fra fil
        dbid = max(db)  # Finner største id
        bruker.melding(filnavn + " er lastet inn")
    else:
        bruker.melding("Feil kommando")

    valg = bruker.valgmeny()
