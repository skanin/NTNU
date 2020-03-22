import requests

inp = requests.get('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-fnr.txt').text.split('\n')


def first_kontrol(nr):
    rekke = [3, 7, 6, 1, 8, 9, 4, 5, 2]
    prods = []

    for i in range(len(nr[0:10])-1):
        prods.append(int(nr[i]) * rekke[i])

    if sum(prods) % 11 == 0:
        return 0

    return 11 - (sum(prods) % 11)


def second_control(nr):
    rekke = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    prods = []

    for i in range(len(nr[0:10])):
        prods.append(int(nr[i]) * rekke[i])

    if sum(prods) % 11 == 0:
        return 0

    if sum(prods) % 11 == 1:
        return -1

    return 11 - (sum(prods) % 11)


def find_women_august(lst):
    valid = []
    for elem in lst:

        if len(str(elem)) != 11 or str(elem)[2:4] != "08" or int(str(elem)[8]) % 2 != 0 or int(str(elem)[0:2]) > 31:
            continue

        if first_kontrol(elem) == int(elem[9]) and second_control(elem) == int(elem[-1]):
            valid.append(elem)

    return len(valid)


print(find_women_august(inp))
