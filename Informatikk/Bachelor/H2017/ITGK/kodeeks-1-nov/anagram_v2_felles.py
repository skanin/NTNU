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
