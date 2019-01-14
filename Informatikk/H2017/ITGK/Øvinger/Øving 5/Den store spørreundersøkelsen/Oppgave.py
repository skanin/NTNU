print("Velkommen til den store spørreundersøkelsen! Skriv 'hade' når som helst for å avslutte")
ANTALL_MENN, ANTALL_KVINNER, ANTALL_ITGK, ANTALL_FAG, ANTALL_TIMER_LEKSER = 0, 0, 0, 0, 0


class ExitLoop (Exception):
    pass


class ContinueLoop (Exception):
    pass


def sjekk_kjonn(reply):
    global ANTALL_KVINNER, ANTALL_MENN
    while True:
        if reply == "k":
            ANTALL_KVINNER += 1
            return
        elif reply == "m":
            ANTALL_MENN += 1
            return
        elif reply == "hade":
            raise ExitLoop
        else:
            print("Venligst svar M eller K")
            reply = input("Er du mann eller kvinne (M/K)? ").lower()


def sjekk_alder(reply):
    global ANTALL_MENN, ANTALL_KVINNER
    if reply == "hade":
        if kjonn == "m":
            ANTALL_MENN -= 1
        else:
            ANTALL_KVINNER -= 1
        raise ExitLoop
    elif not 16 <= int(reply) <= 25:
        print("Du er desverre ikke innenfor målgruppen")
        if kjonn == "m":
            ANTALL_MENN -= 1
        else:
            ANTALL_KVINNER -= 1
        raise ContinueLoop
    return True


def sjekk_ja_nei(reply):
    global ANTALL_ITGK, ANTALL_FAG, ANTALL_MENN, ANTALL_KVINNER
    if reply == "hade":
        if kjonn == "m":
            ANTALL_MENN -= 1
        else:
            ANTALL_KVINNER -= 1

        raise ExitLoop

    while not (reply == "j" or reply == "n"):
        if medlem_ITGK is None:
            reply = input("Tar du et fag (j/n)? ").lower()
        else:
            if int(alder) < 22:
                reply = input("Tar du ITGK? ")
            else:
                reply = input("Tar du virkelig ITGK? ")

    if medlem_ITGK == "j":
        ANTALL_ITGK += 1
    if fag == "j" and medlem_ITGK is None:
        ANTALL_FAG += 1
    elif fag == "n":
        print("Takk for at du tok deg tid til denne undersøkelsen!")
        raise ExitLoop


def sjekk_timer(reply):
    global ANTALL_TIMER_LEKSER, ANTALL_MENN, ANTALL_KVINNER, ANTALL_FAG, ANTALL_ITGK
    if reply == "hade":
        if kjonn == "m":
            ANTALL_MENN -= 1
        else:
            ANTALL_KVINNER -= 1

        ANTALL_FAG -= 1
        ANTALL_ITGK -= 1
        raise ExitLoop

    ANTALL_TIMER_LEKSER += float(reply)


def skriv_statistikk():
    global ANTALL_TIMER_LEKSER, ANTALL_MENN, ANTALL_KVINNER, ANTALL_FAG, ANTALL_ITGK
    print("Antall kvinner: " + str(ANTALL_KVINNER))
    print("Antall menn: " + str(ANTALL_MENN))
    print("Antall fag: " + str(ANTALL_FAG))
    print("Antall ITGK: " + str(ANTALL_ITGK))
    print("Antall timer med lekser: " + str(ANTALL_TIMER_LEKSER))


while True:
    try:
        kjonn = input("Er du mann eller kvinne (M/K)? ").lower()
        sjekk_kjonn(kjonn)

        alder = input("Hvor gammel er du? ").lower()
        inrange = sjekk_alder(alder)

        fag = input("Tar du et fag (j/n)? ").lower()
        medlem_ITGK = None
        sjekk_ja_nei(fag)

        if int(alder) < 22:
            medlem_ITGK = input("Tar du ITGK? ")
            sjekk_ja_nei(medlem_ITGK)
        else:
            medlem_ITGK = input("Tar du virkelig ITGK? ")
            sjekk_ja_nei(medlem_ITGK)

        timer_lekser = input("Hvor mange timer bruker du i snitt på lekser pr dag? ")
        sjekk_timer(timer_lekser)
    except ExitLoop:
        skriv_statistikk()
        break
    except ContinueLoop:
        continue
