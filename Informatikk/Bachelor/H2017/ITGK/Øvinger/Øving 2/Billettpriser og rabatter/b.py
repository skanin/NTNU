print("Velkommen til TravelatoR!\nVi tilbyr reiser fra Trondheim til Pythonville.\n"
      "Ved bestilling minst 14 dager før avreise, kan du få minipris til 199kr.")
dager = int(input("Hvor mange dager er det til du reiser? "))
svar = ""
if dager >=14:
    svar = input("Minipris 199,- kan ikke refunderes/endres. Ønskes dette (J/N)? ")
else:
    print("For sent for minipris; fullpris 440,-")


if svar == "J":
    print("Takk for pengene, god reise!")
elif svar == "N":
    print("Da tilbyr vi fullpris: 440,-")
else:
    print("Vennligst svar 'J' eller 'N'")