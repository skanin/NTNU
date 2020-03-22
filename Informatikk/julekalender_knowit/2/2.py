import numpy as np
f = open('input-rain.txt', 'r')
lines = f.read().split('\n')

tups = [i.split(';') for i in lines]

vecs = []

for i in range(len(tups)):
        vecs.append([int(tups[i][1].strip('()').split(',')[0]) -
                     int(tups[i][0].strip('()').split(',')[0]),
                     int(tups[i][1].strip('()').split(',')[1]) -
                     int(tups[i][0].strip('()').split(',')[1])])

j = 0
one_of_each= []
for elem in vecs:
    if elem not in one_of_each:
        one_of_each.append(elem)

different_parallel = []

for i in range(len(one_of_each)-1):
    for j in range(i+1, len(one_of_each)):
        if np.cross(np.array([one_of_each[i][0], one_of_each[i][1]]),
                       np.array([one_of_each[j][0], one_of_each[j][1]])) == 0:
            different_parallel.append(one_of_each[i])
            different_parallel.append(one_of_each[j])

all = [[], []]
for i in range(len(vecs)):
    if vecs[i] == different_parallel[0] or vecs[i] == different_parallel[1]:
        all[0].append(vecs[i])
    elif vecs[i] == different_parallel[2] or vecs[i] == different_parallel[3]:
        all[1].append(vecs[i])

print(max(len(all[0]), len(all[1])))