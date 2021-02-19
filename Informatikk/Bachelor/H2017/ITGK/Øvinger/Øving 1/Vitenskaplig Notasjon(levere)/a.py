avogadros = 6.022e23

stoff = input("Si et stoff du er i besittelse av: ")
molekylvekt = int(input("Hva er molekylvekt i gram for {}?: ".format(stoff)))
gram = int(input("Hvor mange gram {} har du? ".format(stoff)))
molekyler = ((gram/molekylvekt)*avogadros)

print("Du har", molekyler," molekyler {}".format(stoff))
