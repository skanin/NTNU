def chess_scorer():
    parti = float(input("Hvilket parti spilles? "))
    score = float(input("Hvor mange poeng har spiller 1? "))
    while score > parti:
        print("Umulig resultat")
        score = float(input("Hvor mange poeng har spiller 1? "))
    score2 = (parti - score)

    return "Spiller 1 har " + str(score) + " poeng, spiller 2 har " + str(score2)


print(chess_scorer())
