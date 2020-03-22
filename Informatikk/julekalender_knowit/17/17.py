import math
import itertools
import datetime
import requests
import time

t = datetime.datetime.now()

# inp = [(7.1, 10.5), (18.8, 9.2), (2.1, 62.1), (74.2, 1.5), (58.4, 5.6), (15.9, 6.2), (44.5, 15.6),
#      (88.1, 53.4), (36.2, 84.2), (26.9, 8.5)]

inp = open('input-luke-22.txt', 'r').read().split("\n")

inp2 = list()
for elem in inp:
    temp = elem.split(",")
    inp2.append((float(temp[0]), float(temp[1])))


it = itertools.permutations(inp2, len(inp2))


def euklid(point1, point2):
    return math.sqrt((point1[0]-point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


min_dist = 2**32
dist = 0

print("For loop")
for elem in it:
    for i in range(len(elem)-1):
        dist += euklid(elem[i], elem[i+1])
        if i == len(elem) - 1:
            dist += euklid(elem[i+1], elem[0])
        if dist > min_dist:
            break
    if dist < min_dist:
        min_dist = dist
        print(min_dist)
    dist = 0


print(round(min_dist))
print("Tok: ", datetime.datetime.now()-t)
