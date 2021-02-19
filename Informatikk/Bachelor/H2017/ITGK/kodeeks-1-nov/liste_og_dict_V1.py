def les_tekst():
    print('\nSkriv inn et uregelrett adjektiv m. gradbøying')
    print('mellomrom mellom ordene, f.eks god bedre best')
    print('eller bare ENTER for å avslutte')
    tekst = input('Adjektiv m. gradbøying? ')
    if tekst == '':
        return ''
    else:
        return tekst.strip().split()

def lag_2D_liste():
    liste = []
    print('Foreløpig liste:', liste)
    ordene = les_tekst()
    while ordene != '':
        liste.append(ordene)
        print('Foreløpig liste:', liste)
        ordene = les_tekst()
    return liste

def lag_dictionary():
    dic = { }
    print('Foreløpig dictionary:', dic)
    ordene = les_tekst()
    while ordene != '':
        dic[ordene[0]] = ordene[1:]
        print('Foreløpig dictionary:', dic)
        ordene = les_tekst()
    return dic
        
def main():
    liste = lag_2D_liste()
    print('Ferdig liste', liste)
    print()
    dic = lag_dictionary()
    print('Ferdig dictionary', dic)

main()
        
