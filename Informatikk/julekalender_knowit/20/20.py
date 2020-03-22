inp = [7096, 3, 3924, 2404, 4502, 4800, 74, 91, 9, 7, 9, 6790, 5, 59, 9, 48, 6345,
88, 73, 88, 956, 94, 665, 7, 797, 3978, 1, 3922, 511, 344, 6, 10, 743, 36,
9289, 7117, 1446, 10, 7466, 9, 223, 2, 6, 528, 37, 33, 1616, 619, 494, 48, 9,
5106, 144, 12, 12, 2, 759, 813, 5156, 9779, 969, 3, 257, 3, 4910, 65, 1, 907,
4464, 15, 8685, 54, 48, 762, 7952, 639, 3, 4, 8239, 4, 21, 306, 667, 1, 2, 90,
42, 6, 1, 3337, 6, 803, 3912, 85, 31, 30, 502, 876, 8686, 813, 880, 5309, 20,
27, 2523, 266, 101, 8, 3058, 7, 56, 6961, 46, 199, 866, 4, 184, 4, 9675, 92]

#print(sorted(map(str, inp), key=lambda x: x[0], reverse=True))

a = [3, 30, 34, 5, 9]
# temp = sorted(temp, key=lambda x: x[1], reverse=True)
'''
a = list(map(str, a))
a.sort(key=lambda x: x[0], reverse=True)
print(a)


a = list(map(str, a))
temp = []
j = 0
for i in range(len(a), 0, -1):
    try:
        key = a[i][j]
        while key > a[i-1][j]:
            a[i], a[i-1] = a[i-1], a[i]
            
    except IndexError:
        continue
'''

from itertools import permutations
'''

b = map(list, permutations(''.join(inp)))
temp = 0
for elem in b:
    if int(''.join(elem)) > temp:
        temp = int(''.join(elem))

print(temp)
inp = list(map(str, inp))
# print(max(map(lambda x: ''.join(x), map(list, permutations(''.join(inp))))))
print(''.join(max(map(list, permutations(''.join(inp))))))
'''


def largestNumber(array):
    # extval is a empty list for extended
    # values and ans for calculating answer
    extval, ans = [], ""

    # calculating the length of largest number
    # from given and add 1 for further operation
    l = len(str(max(array))) + 1

    # iterate given values and
    # calculating extended values
    for i in array:
        temp = str(i) * l

        # make tuple of extended value and
        # equivalant original value then
        # append to list
        extval.append((temp[:l:], i))

        # sort extval in descending order
    extval.sort(reverse=True)

    # iterate extended values
    for i in extval:
        # concatinate original value equivalant
        # to extended value into ans variable
        ans += str(i[1])

    return ans


print(largestNumber(inp))