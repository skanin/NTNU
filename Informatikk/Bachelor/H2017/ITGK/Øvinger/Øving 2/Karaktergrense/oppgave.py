poeng = int(input("Skriv inn antall poeng: "))

if poeng == 100 or poeng > 89:
    print("Du fikk A!")
elif poeng == 88 or poeng > 77:
    print("Du fikk B!")
elif poeng == 76 or poeng > 65:
    print("Du fikk C!")
elif poeng == 64 or poeng > 53:
    print("Du fikk D!")
elif poeng == 52 or poeng > 41:
    print("Du fikk E!")
elif poeng > 100:
    print("Du kan ikke ha mer enn 100 poeng!")
elif poeng < 0:
    print("Du kan ikke få minuspoeng!")
else:
    print("Du fikk F!")
        
