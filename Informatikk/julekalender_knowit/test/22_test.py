import math

inp = [elem.split(",") for elem in open('../22/input-luke-22.txt', 'r').read().split("\n")]


def euklid(point1, point2):
    return math.sqrt((float(point1[0])-float(point2[0])) ** 2 + (float(point1[1]) - float(point2[1])) ** 2)


print(math.pi * euklid(min(inp, key=lambda x: float(x[0])), max(inp, key=lambda x: float(x[0]))))