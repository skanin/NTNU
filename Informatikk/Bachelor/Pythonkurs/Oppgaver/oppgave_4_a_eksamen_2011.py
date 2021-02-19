def check_highscore(points, score):
    for i in range(1, 11):
        if points > score[i][1]:
            return i
    return -1


def print_highscores(scores):
    for i in scores:
        print(str(i).rjust(2) + scores[i][0].ljust(20) + str(scores[i][1].rjust(5)))
