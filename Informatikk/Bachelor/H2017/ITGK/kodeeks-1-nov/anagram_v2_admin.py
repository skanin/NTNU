# Dette programmet er ment for administratoren. Det leser tekstfila
# med ordlista og genererer ei binærfil med en dictionary som er
# spesialtilpasset anagramfinning. Programmet trenger kun kjøres hver
# gang ordlista blir oppdatert med nye ord. Vanlige brukere kan i stedet
# forholde seg til binærfila, som går mye raskere å laste inn.
import pickle
from anagram_v2_felles import string_2_key
# importerer funksjon for å regne ut nøkler fra ord

def file_2_list(ordfil):
    # INN: navn på ei fil som antas å inneholde ei ordliste,
    #      ett ord per linje i fila
    # UT: returnerer samme ordliste som ei liste
    # Dropper unntaksbehandling for at programmet ikke skal bli for langt
    fil = open(ordfil, 'r', encoding='utf-8-sig')
    ordliste = [ ]
    for linje in fil:
        ordliste.append(linje.strip())
    fil.close()
    return ordliste

def list_2_dic(liste):
    # INN: Ei liste med ord
    # UT: dictionary hvor ordene er samlet på hver sin anagramnøkkel
    #     f.eks. {6:['et','te'], 10:['er','re'], 14: ['es', 'se'], ...}
    #     fordi e, t, r og s har verdier hhv. 2, 3, 5 og 7 som ganges sammen
    dic = { } # oppretter en tom dictionary
    for w in liste: # ser på ett og ett ord (w) i lista
        key = string_2_key(w) # finner tallnøkkel for ordet
        if key in dic: # har allerede andre ord m samme nøkkel
            dic[key].append(w)
        else: # ordet er det første vi finner med denne nøkkelen
            dic[key] = [w]
    return dic

def dic_2_binfile(dic, filnavn):
    #dumper dictionary til binærfil
    f = open(filnavn, 'wb')
    pickle.dump(dic, f)
    f.close()

def main():
    print('Leser tekstfil...')
    liste = file_2_list('nsf2016.txt') #fil fra Norges Scrabbleforbund
    print('Lager dictionary')
    dic = list_2_dic(liste)
    print('Ferdig med å lage dictionary')
    dic_2_binfile(dic, 'anagramordliste.dat')
    print('Ferdig med å skrive fil')
    
main()



