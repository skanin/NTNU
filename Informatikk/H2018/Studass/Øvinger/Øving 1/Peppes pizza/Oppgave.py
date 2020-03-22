# a
pizza = 725
studentrabatt = 0.2
tips = 0.08

# b
totalt = (pizza - (pizza*studentrabatt)) + (pizza*tips)

#c
pris = int(input("Pris på pizza: "))
personer = int(input("Hvor mange deltok på middagen? "))
print("Etter som dere var " + str(personer) + " personer, så må dere betale " + str(pris/personer) + " hver")
