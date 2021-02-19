# Dette programmet er ment for brukeren. Ved å laste dictionary
# fra binærfil, får man en mye raskere oppstart på programmet enn
# om man hver gang skulle ha lest tekstfila og konvertert denne
# til en dictionary.

import pickle # modul for å lese og skrive binærfiler
from anagram_v2_felles import string_2_key # funksjon for anagramnøkler

def binfile_2_dic(filnavn):
    # leser dictionary fra binærfil
    f = open(filnavn, 'rb')
    dic = pickle.load(f)
    f.close()
    return dic

def finn_anagram(dic, streng):
    # INPUT (param.) en dictionary (dic) og en tallverdi (verdi)
    # PROS.: ser om det fins et oppslag med nøkkel=verdi i dictionary
    # OUTPUT: returerer lista av ord for nøkkelen, tom liste hvis ingen match
    verdi = string_2_key(streng.lower()) # må ha små bokst for å regne verdi
    if verdi in dic.keys():
        return dic[verdi]
    else:
        return []
    
def main():
    print('Dette er et program som kan finne anagram for strenger,')
    print('for eksempel fra ditt eget eller andres navn.')
    dic = binfile_2_dic('anagramordliste.dat')
    while True:
        print('Skriv inn ordet / strengen du ønsker anagram for')
        navn = input('eller ENTER (tom streng) for å slutte: ')
        if navn == '':
            break
        else:
            anagrammer = finn_anagram(dic, navn)
            if anagrammer != []:
                print('Anagrammer funnet:', anagrammer)
            else:
                print('Ingen match')
    print('Takk for nå')

main()
