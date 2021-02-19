hemmelig_ord = input("Skriv inn det hemmelige ordet: ").lower()
hemmelig_ord = list(hemmelig_ord)

hint = ""

for i in range(len(hemmelig_ord)):
    hint += "*"

hint = list(hint)

antall_liv = int(input("Antall liv: "))
print('\n'*80)
guessed_letters = []
occurences = 0

while True:
    guessed_letter = input("Gjett en bokstav: ").lower()
    while len(guessed_letter) != 1:
        print("Vennligst skriv inn kun en bokstav")
        guessed_letter = input("Gjett en bokstav: ").lower()

    print("Allerede gjettet? " + str(guessed_letter in guessed_letters))
    while guessed_letter in guessed_letters:
        print("Du har allerede gjettet " + guessed_letter.upper())
        print("")
        guessed_letter = input("Gjett en bokstav: ").lower()

    if guessed_letter not in guessed_letters:
        if guessed_letter in hemmelig_ord:
            print("Rett! " + guessed_letter.upper() + " er i ordet!")
            for letter in hemmelig_ord:
                if letter == guessed_letter:
                    occurences += 1

            for i in range(len(hemmelig_ord)):
                if hemmelig_ord[i] == guessed_letter:
                    hint[i] = guessed_letter

            for i in range(occurences):
                guessed_letters.append(guessed_letter)
            occurences = 0

        else:
            print(guessed_letter.upper() + " er ikke i ordet :(")
            antall_liv -= 1
            print("Du har nå " + str(antall_liv) + " liv igjen")
            guessed_letters.append(guessed_letter)

    if antall_liv == 0:
        print("Du tapte! Det hemmelige ordet var '" + "".join(hemmelig_ord) + "'")
        break

    '''
    if len(guessed_letters) == len(hemmelig_ord):
        print("Du vant! Det hemmelige ordet var " + "'" + "'".join(hemmelig_ord) + "'")
        break
    '''

    if "".join(hint) == "".join(hemmelig_ord):
        print("Du vant! Det hemmelige ordet var '" + "".join(hemmelig_ord) + "'")
        break

    print("Hint: " + "".join(hint))
    print("Guessed letters: " + str(guessed_letters))
    print("")