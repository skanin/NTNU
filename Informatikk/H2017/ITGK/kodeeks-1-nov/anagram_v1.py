def file_2_list(ordfil):
    # INN: navn på ei fil som antas å inneholde ei ordliste,
    #      ett ord per linje i fila
    # UT: returnerer samme ordliste som ei liste
    # Dropper unntaksbehandling for at programmet ikke skal bli for langt
    fil = open(ordfil, 'r', encoding='utf-8-sig')
    ordliste =[ ]
    for linje in fil:
        ordliste.append(linje.strip())
    fil.close()
    return ordliste
        
def string_2_key(streng):
    # INN: en streng av små bokstaver (et ord på norsk)
    # UT: returnerer et heltall som er et produkt av primtall for,
    #     bokstavene som inngår i ordet, som gitt i dictionary primes
    primes = {'e':2, 't':3, 'r':5, 's':7, 'n':11, 'a':13, 'i':17,
             'l':19, 'o':23, 'g':29, 'k':31, 'd':37, 'm':41, 'å':43,
             'v':47, 'f':53, 'b':59, 'u':61, 'p':67, 'h': 71, 'j':73,
             'ø':79, 'y':83, 'æ':89, 'c':97, 'q':101, 'w': 103,
             'x':107, 'z':109, 'ü': 113} # et par ord med ü i nsf-fila
    produkt = 1
    for tegn in streng: # går i løkke tegn for tegn i ordet
        if tegn in primes.keys():
            produkt *= primes[tegn] # og ganger inn primtall for hvert tegn
    return produkt

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

def finn_anagram(dic, streng):
    # INPUT (param.) en dictionary (dic) og en tallverdi (verdi)
    # PROS.: ser om det fins et oppslag med nøkkel=verdi i dictionary
    # OUTPUT: returerer lista av ord for nøkkelen, tom liste hvis ingen match
    verdi = string_2_key(streng.lower()) # må ha små bokst for å regne verdi
    if verdi in dic.keys():
        return dic[verdi]
    else:
        return [ ]

def main():
    print('Dette er et program som kan finne anagram for strenger,')
    print('for eksempel fra ditt eget eller andres navn.')
    ordliste = file_2_list('nsf2016.txt')
    dic = list_2_dic(ordliste)
    while True:
        print('Skriv inn ordet / strengen du ønsker anagram for')
        navn = input('eller ENTER (tom streng) for å slutte: ')
        if navn == '':
            break
        else:
            anagrammer = finn_anagram(dic, navn)
            if anagrammer != [ ]:
                print('Anagrammer funnet:', anagrammer)
            else:
                print('Ingen match')
    print('Takk for nå')

main()

# EKSTRA FORKLARING:
# Dictionary primes gir en unik primtallsverdi for hver bokstav.
# De er ordnet etter frekvens, dvs. mest vanlige bokstav i norsk (E) først,
# dette for at produktene skal bli minst mulig. Ved å multiplisere sammen tall
# for alle bokstavene i et ord vil ord ende med samme verdi hvis og bare hvis de
# består av akkurat de samme bokstavene: TRE = 3*5*2 og ERT = 2*5*3 blir 30, og
# det er er umulig for et ord som inneholder noe annet enn akkurat disse tegnene
# å få samme verdi. Dette fordi vi kun har brukt primtall. Hadde vi brukt andre
# tall enn primtall, f.eks. I=15 i stedet for 17, kunne man ha fått 30 også for
# ordet "EI" som inneholder andre bokstaver enn TRE, ERT, ...
