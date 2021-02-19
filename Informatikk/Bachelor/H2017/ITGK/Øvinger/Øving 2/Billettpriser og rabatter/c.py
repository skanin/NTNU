print("Velkommen til TravelatoR!\nVi tilbyr reiser fra Trondheim til Pythonville.\n"
      "Ved bestilling minst 14 dager før avreise, kan du få minipris til 199kr.")
dager = int(input("Hvor mange dager er det til du reiser? "))
svar = ""
minipris = 199
fullpris = 440

if dager <= 14:
    svar = input("Minipris: minipris 199,- kan ikke refunderes/endres. Ønskes dette (J/N)? ")
else:
    print("For sent for minipris; fullpris", fullpris, ",-")


if svar == "J" or svar == "j":
    print("Takk for pengene, god reise!")
else:
    alder = int(input("Skriv inn din alder: "))
    if alder < 16:
        print("Prisen på biletten blir:", fullpris / 2)
    elif alder >= 60:
        print("Prisen på biletten blir:", fullpris * 0.75)
    else:
        studentMill = input("Er du millitær eller student (J/N)? ")
        if studentMill == "J" or studentMill == "j":
            print("Prisen på biletten blir:", fullpris * 0.75)
        else:
            print("Prisen på biletten blir:", fullpris)