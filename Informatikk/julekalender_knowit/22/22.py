import itertools
from math import sqrt

# inp = requests.get('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-luke-22.txt').text.split("\n")
inp = open('input-luke-22.txt', 'r').read().split("\n")

points = list()
for elem in inp:
    temp = elem.split(",")
    points.append((float(temp[0]), float(temp[1])))

it = itertools.permutations(points, len(points))


def euklid(point1, point2):
    return sqrt((point1[0]-point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def test(x):
    dist = euklid(x[0], x[len(x)-1])
    for i in range(len(x)-1):
        dist += euklid(x[i], x[i+1])
    return dist


print(min(map(lambda x: test(x), it)))
