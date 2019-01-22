from random import randint
from sys import getsizeof
from time import time

def n_oppslag(n, data):
    # Gjør n oppslag i data'ene, som kan være liste, tuppel, mengde...
    # Returnerer tiden som det tar fra funksjonens start til slutt
    antall = len(data)
    start = time() # klokka nå, dvs. starttidspunkt for funksjonen
    for i in range(n):
        if randint(1, antall) in data:
            pass
    return time() - start # diff mellom klokka nå og starttidspunkt

def main():
    ant_oppslag = int(input('Hvor mange oppslag? '))
    ant_data = int(input('Hvor mange data? '))
    r = range(1, ant_data * 2, 2) # oddetall 1, ..., ant_data*2 - 1

    # Oppretter tre variable med samme data; liste, tuppel og mengde:
    liste = list( r )
    tuppel = tuple( r )
    mengde = set( r )

    # Skriver ut plassforbruk
    print('Størrelse av listevariabel :', format(getsizeof(liste), '12d'))
    print('Størrelse av tuppelvariabel:', format(getsizeof(tuppel), '12d'))
    print('Størrelse av mengdevariabel:', format(getsizeof(mengde), '12d'))

    # Gjør oppslag med variablene og måler tid:
    print('Tidsbruk liste :', format(n_oppslag(ant_oppslag, liste),'.2f'))
    print('Tidsbruk tuppel:', format(n_oppslag(ant_oppslag, tuppel),'.2f'))
    print('Tidsbruk mengde:', format(n_oppslag(ant_oppslag, mengde),'.2f'))

main()
    
