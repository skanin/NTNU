print("Velkommen til TravelatoR!\nVi tilbyr reiser fra Trondheim til Pythonville.\n"
      "Ved bestilling minst 14 dager før avreise, kan du få minipris til 199kr.")
dager = int(input("Hvor mange dager er det til du reiser? "))
if dager >= 14:
    print("Du kan få minipris: 199,-")
else:
    print("For sent for minipris; fullpris 440,-")
