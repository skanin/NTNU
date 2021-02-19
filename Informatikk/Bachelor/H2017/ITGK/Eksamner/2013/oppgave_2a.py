def chess_math():
    total_score1 = 0
    total_score2 = 0
    num_games = int(input("Hvor mange spill skal spilles?"))

    if num_games < 1:
        print("Så kjedelig, da blir det ingen kamp")
    else:
        i = 1
        while num_games > 0:
            print("Parti " + str(i))
            i += 1
            score1 = int(input("Hvor mange poeng skal spiller 1 få? "))
            score2 = int(input("Hvor mange poeng skal spiller 2 få? "))
            total_score1 += score1
            total_score2 += score2
            num_games -= 1

        print("Kampen er slutt!")
        print("Spiller 1 fikk " + str(total_score1) + " poeng!")
        print("Spiller 2 fikk " + str(total_score2) + " poeng!")


chess_math()