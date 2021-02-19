mittNavn = input("Skriv inn ditt navn: ")
minAlder = int(input("Hei, {}. Hvor gammel er du? ".format(mittNavn)))
alderProg = int(input("Hvor gammel var du da du begynte å programmere? "))
alderDiff = minAlder - alderProg

print("Da har du programmert i",alderDiff,"år.")
