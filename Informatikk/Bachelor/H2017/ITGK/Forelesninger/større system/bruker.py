# Modulen bruker (bruker.py) som har ansvar for bruker interaskjon


def velkommen():
    print("Velkommen til Hybelregnskapsprogram v3.0")
    print("=========================================")


def valgmeny():
    print("\nVelg kommando [utgift, inntekt, vis, load, save, fjern, avslutt]")
    valg = input("Kommando: ")
    return valg


def registrer(db, dbid, valg):
    dato = input("Dato [yyy-mm-dd]: ")
    belop = float(input("Beløp: "))
    beskrivelse = input("Beskrivelse: ")
    if valg.lower() == "utgift":
        belop = belop * -1
    db[dbid] = [dato, belop, beskrivelse]
    melding("Data er registert")
    return db


def melding(tekst):
    print(">>> " + tekst)


def vis(db):
    balanse = 0
    header = "ID".rjust(4) + " Dato".ljust(11) + " Besrkivelse".ljust(30) + " Sum"
    print(header)
    print("=====================================================")
    for x in db:
        liste = db[x]
        s = str(x).rjust(4) + liste[0].rjust(11)  # Streng med ID og Dato
        s += "  " + liste[2].ljust(30)  # Berskrivelse
        s += str(liste[1]).rjust(8)  # Beløp
        print(s)
        balanse += liste[1]
    print("Balanse: " + str(balanse))


def fjern(db):
    print("IDer i databasen:", db.keys())
    dbid = int(input("ID på innslag som skal fjernes: "))
    if db in db:
        del db[dbid]
        melding("Innslag med ID " + str(dbid) + " er fjernet")
    else:
        melding("ID " + srt(dbid) + " finnes ikke i databasen")
    return db


def velgFilnavn():
    filnavn = input("Velg filnavn: ")
    return filnavn
