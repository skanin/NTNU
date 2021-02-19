def lag_mengde(streng):
    # INN: en streng med elementer separert med blankt tegn
    # UT: returnerer ei mengde med elementene
    # TBD: skriv koden din her...
    liste = streng.split()
    return set(liste)

def finn_mistenkte(v, m, a):
    # INN: tre mengder, v - de som hadde våpen, m - de som hadde motiv, a - de som hadde alibi
    # UT: returnerer ei mengde av mulige mistenkte,
    #     dvs. som hadde våpen OG motiv, men IKKE alibi
    # TBD: skriv koden din her...

def main():
    print('Dette programmet tester noen mengdeoperasjoner')
    print('På hvert spørsmål, skriv inn navnet på noen personer')
    print('med mellomrom mellom, f.eks. Ole Nina Per Anne')
    print('Det bør være noen navn felles mellom listene og noen ulike')
    vaapen = input('Hvem kan ha hatt tilgang til våpnet? ')
    v = lag_mengde(vaapen)
    motiv = input('Hvem hadde motiv for forbrytelsen? ')
    m = lag_mengde(motiv)
    alibi = input('Hvem har alibi? ')
    a = lag_mengde(alibi)
    mist = finn_mistenkte(v, m, a)
    print('Mulige mistenkte:')
    for navn in mist:
        print(navn)

main()
