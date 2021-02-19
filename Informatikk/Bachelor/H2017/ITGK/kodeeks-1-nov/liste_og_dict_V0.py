def les_tekst():
    print('\nSkriv inn et uregelrett adjektiv m. gradbøying')
    print('mellomrom mellom ordene, f.eks god bedre best')
    print('eller bare ENTER for å avslutte')
    tekst = input('Adjektiv m. gradbøying? ')
    if tekst == '':
        return ''
    else:
god bedre best        return tekst.strip().split()

def lag_2D_liste():
    liste = [ ]
    print('Foreløpig liste:', liste)
    ordene = les_tekst()
    while ordene != '':
        liste.append(ordene)
        print('Foreløpig liste:', liste)
        ordene = les_tekst()
    return liste

def lag_dictionary():
    # Lager en dictionary hvor nøklene er adjektiv i positiv form,
    # og hver av disse viser til tilsvarende i komparativ, superlativ
    # Skriv inn din kode i stedet for print-setningen
    print('TO BE DONE: Funksjonen gjør ikke noe ennå')
        
def main():
    liste = lag_2D_liste()
    print('Ferdig liste', liste)
    print()
    dic = lag_dictionary()
    print('Ferdig dictionary', dic)

main()
        
