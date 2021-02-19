skylder_epler = None
print("Dette er et program for å teste din sjenerøsitet.")
har_epler = int(input("Hvor mange epler har du? "))
if har_epler == 0:
    gir_epler = har_epler
    print("Æsj, det sier du bare for å slippe å gi noe!")
else:
    gir_epler = int(input("Hvor mange kan du gi til meg? "))
    if gir_epler < har_epler / 2:
        print("Du beholder det meste for deg sev...")
    elif gir_epler > har_epler:
        skylder_epler = har_epler - gir_epler
    else:
        print("Takk, det var snilt!")

gjenstaaende_epler = har_epler - gir_epler
if gjenstaaende_epler == 1:
    print("Du har nå 1 eple igjen")
elif gjenstaaende_epler < 0:
    print("Du har nå 0 epler igjen. Gi meg resten ("+ str(abs(skylder_epler))+ ") du skylder meg neste gang vi møtes.")
else:
    print("Du har nå", har_epler, "epler igjen.")
