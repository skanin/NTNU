def fakultet(n):
    if n == 0:
        return 1
    else:
        return n * fakultet(n-1)


print(fakultet(2))
