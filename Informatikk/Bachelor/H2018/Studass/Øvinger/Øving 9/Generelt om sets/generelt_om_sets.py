oddetall = set()

for i in range(1, 20, 2):
    oddetall.add(i)


oddetall2 = set()

for i in range(1, 10, 2):
    oddetall2.add(i)

set3 = oddetall.symmetric_difference(oddetall2)

print(set3)

# e Ingenting
set3.intersection(oddetall2)


def allUnique(lst):
    return len(lst) == len(set(lst))


print(allUnique([1,3,2,6,8]))


print(allUnique([1,3,5,2,3,7]))


def removeDuplicates(lst):
    return list(set(lst))


print(removeDuplicates([1,3,5,2,3,7]))