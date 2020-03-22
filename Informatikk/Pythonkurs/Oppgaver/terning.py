from random import randint


def terning(n):
    i = 0
    a = 0
    while i < n:
        a += randint(1, 6)
        i += 1
    return a/n


print(terning(999999))
