# Lage 10x10 matrise

'''
tabell_10x10 = [[0 for col in range(10)] for row in range(10) ]

print(tabell_10x10)
'''

'''
def fillTable(table):
    number = 2
    for y in range(0, len(table)):
        for x in range(0, len(table[y])):
            table[y][x] = number
            number += 2

    return table


print(fillTable([[0 for col in range(10)] for row in range(10)]))
'''

'''
def sumTable(table):
    total = 0
    for y in range(len(table)):
        for x in range(len(table[y])):
            total += table[y][x]

    return total


print(sumTable([[1,2,3], [4,5,6]]))
'''


from random import randint


def pickRemoveNumber(list):
    index = randint(0,len(list)-1)
    del list[index]

    return index


print(pickRemoveNumber([1,2,3,4,5]))
