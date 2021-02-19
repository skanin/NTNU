def player_score(results):
    total = 0
    for score in results:
        if score is None:
            continue
        else:
            total += score

    return total


print(player_score([None, None, None, None]))
