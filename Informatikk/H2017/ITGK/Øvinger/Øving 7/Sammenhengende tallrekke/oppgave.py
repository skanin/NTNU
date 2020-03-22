# a


from random import randint


def randList(size, lower_bound, upper_bound):
    liste = []
    for i in range(size):
        liste.append(randint(lower_bound, upper_bound))

    return liste


# b


def compareLists(list1, list2):
    liste = []
    for x in list1:
        if x in list2:
            if x not in liste:
                liste.append(x)

    return liste


# c


def multiCompList(lists):
    