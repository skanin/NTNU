def gjennomsnitt(li):
    y = 0
    for x in li:
        y = x + y
    snitt = y/len(li)
    return snitt


print(gjennomsnitt([1, 2, 3]))
