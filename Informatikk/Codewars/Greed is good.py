def score(dice):
    ones = dice.count(1)
    twos = dice.count(2)
    threes = dice.count(3)
    fours = dice.count(4)
    fives = dice.count(5)
    sixes = dice.count(6)

    score = 0

    if ones >= 3:
        score += 1000 + (ones - 3)*100
    else:
        score += ones * 100

    if fives >= 3:
        score += 500 + (fives - 3)*50
    else:
        score += fives * 50

    if twos >= 3:
        score += 200

    if threes >= 3:
        score += 300

    if fours >= 3:
        score += 400

    if sixes >= 3:
        score += 600

    return score


print(score([5, 3, 5, 5, 5]))