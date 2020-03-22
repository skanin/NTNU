# Oppgave 1:

'''
import random

for i in range (0, 10):
    number = random.randrange(0, 40, 4)
    print(number)
    i += 1
'''

# Oppgave 2

'''
def bmi(vekt, hoyde):
    return vekt/(hoyde**2)


bruker_bmi = round(bmi(float(input("Hva er din vekt i kg? ")), float(input("Hva er din høyde i meter? "))), 2)
print("Din BMI er " + str(bruker_bmi))
'''

# Oppgave 3


def romertall(tall):
    if(tall == 0):
        return ''
    elif (tall == 1):
        return 'I'
    elif (tall == 2):
        return 'II'
    elif (tall == 3):
        return '4'
    elif (tall == 4):
        return 'IV'
    elif (tall == 5):
        return 'V'
    elif (tall == 6):
        return 'VI'
    elif (tall == 7):
        return 'VII'
    elif (tall == 8):
        return 'VIII'
    elif (tall == 9):
        return True
    else:
        return 'Tallet er for stort eller for lite'
    

tall = int(input("Skriv inn et tall fra 0 til 9: "))

while tall > 0:
    if romertall(tall):
        print("True")
    print(romertall(tall))
    tall = int(input("Skriv inn et tall fra 0 til 9: "))
