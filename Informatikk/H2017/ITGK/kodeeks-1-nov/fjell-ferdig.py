def alle_deltagere(lister):
    # INPUT: en liste av lister, hvor hver indre liste inneholder navn
    #        på deltagere som har besøkt et visst punkt av interesse
    # PROS.: gjør om de indre listene til mengder og tar snittet av dem
    #        for å finne mengden av deltagere som har vært på minst ett sted
    # OUTPUT: returnerer mengden av deltagere som har vært på minst ett sted
    deltagermengde = set() # initialiserer til tom mengde
    for i in range(len(lister)):
        deltagermengde = deltagermengde.union(set(lister[i]))
    return deltagermengde

def ivrigste_deltagere(lister):
    # INPUT: en liste av lister, hvor hver indre liste inneholder navn
    #        på deltagere som har besøkt et visst punkt av interesse
    # PROS.: gjør om de indre listene til mengder og tar snittet av dem
    #        for å finne mengden av deltagere som har vært på alle stedene
    # OUTPUT: returnerer mengden av deltagere som har vært på alle stedene
    resultat = set(lister[0]) # initialiserer til mengden for første fjelltopp
    for i in range(1, len(lister)):
        resultat = resultat.intersection(set(lister[i]))
    return resultat

def main():
    fjell_lister =  [['Jo', 'Ine', 'Eli', 'Bo', 'Ron', 'Sam', 'Una', 'Ron'],
                     ['Eli', 'Ada', 'Oda', 'Jo', 'Dag', 'Una', 'Ron'],
                     ['Bo', 'Ada', 'Tor', 'Dag', 'Jo', 'Eli', 'Frank']]
    print('Alle deltagere (vært på minst ett fjell):',
          alle_deltagere(fjell_lister) )
    antall_fjell = len(fjell_lister)
    print('Vært på alle', antall_fjell, 'fjell:',
          ivrigste_deltagere(fjell_lister) )

main()
