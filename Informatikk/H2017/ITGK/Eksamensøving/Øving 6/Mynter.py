def count_coins(coins):
    summen = 0
    for coin in coins:
        summen += coin

    return summen


def num_coins(numbers):
    coins = []
    temp = []
    for num in numbers:
        if num > 10:
            enere = num % 10
            tiere = num // 10
            if tiere % 2 == 0:
                tjue = tiere
                tiere = 0
            else:
                tjue = num // 20
            femere = num // 5
            temp.append(tjue)
            temp.append(tiere)
            temp.append(femere)
            temp.append(enere)
            coins.append(temp)
    return coins


print(num_coins([63, 55]))
