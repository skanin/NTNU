# a

dager = int(input("Dager til du skal reise: "))

if dager >= 14:
    print("Du kan få minipris: 199,-")
    print("Denne kan ikke refunderes, ønsker du minipris?")
    svar = input("(J/N): ")
    if svar.lower() == "j":
        print("Takk for pengene, god reise!")
    else:
        print("Da tilbyr vi fullpris: 440,-")
else:
    print("For sent til minipris; fullpris: 440,-")


# Orker ikke gjøre resten