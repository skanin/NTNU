# Modul fil - filfunksjoner for lagring og innlasting

import pickle


def save (db, filnavn):
    f = open(filnavn, "bw")  # Åpner fil for skriving binært
    pickle.dump(db, f)
    f.close()


def load(filnavn):
    f = open(filnavn, "br")
    db = pickle.load(f)  # Laster dictionary fra fil
    f.close()
    return db
