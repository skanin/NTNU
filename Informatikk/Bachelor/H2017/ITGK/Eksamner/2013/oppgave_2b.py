def end_of_match(num_games, game, total_score1, total_score2):
    if num_games != game:
        return 0
    else:
        if total_score1 > ((num_games/2)+0.5):
            return 1
        elif total_score2 > ((num_games/2)+0.5):
            return 2
        elif total_score1 == total_score2:
            return 3
        else:
            return "Kampen holder fortsatt på"


print(end_of_match(4, 3, 1, 2))