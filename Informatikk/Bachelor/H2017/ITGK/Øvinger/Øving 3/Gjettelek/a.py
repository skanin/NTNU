import random
ovre_grense = int(input("Hva skal øvre grense være? "))

random_number = random.randint(1, ovre_grense)

i = 0
while i < 1:
    svar = int(input("Make a guess: "))
    if(svar < random_number):
        print("The correct number is higher")
    elif (svar > random_number):
        print("The correct number is lower")
    else:
        i = 1
        print("You guessed correct! The number was: ", random_number)
