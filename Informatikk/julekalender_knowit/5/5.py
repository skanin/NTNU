def combine(num1, num2):
    return int(str(num1) + str(num2))


def test(a):

    lst = a
    b = []
    j = 0

    while not lst in b:
        b.append(lst)
        lst = []

        if j != 1:
            for elem in a[0:j]:
                lst.append(elem)

        for i in range(j, len(a)-1, 2):
            lst.append(combine(a[i], a[i+1]))

        if lst[-1] != 21:
            lst.append(a[-1])
        elif lst[0] != 12 and lst[0] != 1:
            lst.insert(0, 1)

        j += 1

    return b


#a = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]
#test = []
'''
counter = 0
while counter < len(a):
    for i in range(0, len(a)-1):
        temp_lst = []
        temp = combine(a[i], a[i+1])
        for j in range(1, len(a)-1):
            if j == i+1:
                temp_lst.append(temp)
            elif j == i:
                continue
            else:
                temp_lst.append(a[j])
        if temp_lst not in test:
            test.append(temp_lst)
    counter += 1
'''

#print(test)
#print(test(a))
'''
test = []
for i in range(0, len(a)):
    for j in range(i, len(a)):
        temp = list(map(combine(a[i], a[j]), a))
    test.append(temp)
print(test)
'''
'''
test = []
for i in range(0, len(a)-1):
    temp = []
   
    for k in range(0, i):
        temp.append(a[k])
    
    temp.append(combine(a[i], a[i + 1]))
    for j in range(0, len(a), 2):

        if j+1 != len(a) and j > i:
            temp.append(combine(a[j], a[j+1]))
        else:
            temp.append(a[j])
    test.append(temp)

print(test)
'''
'''
a = [1,2,3,4,5,6,7]
temp = []
k = 6
for i in range(0, len(a) - 1):
    comb = combine(a[i], a[i+1])
    lst = []
    for j in range(0, len(a), 2):
        try:
            if j == i or j == i + 1:
                lst.append(comb)
                continue
            else:
                lst.append(combine(a[j], a[j+1]))
            if j == k:
                lst.append(a[k])
                k -= 1
                continue
        except IndexError:
            lst.append(a[i-1])

    k = 6
    temp.append(lst)

print(temp)
'''
a = [1,2,3,4,5,6,7]


def all_after(a):
    temp = list()
    j = 0
    while j < len(a):
        lst = list()
        for i in range(0, j):
            lst.append(a[i])

        for i in range(j, len(a), 2):
            try:
                lst.append(combine(a[i], a[i+1]))
            except IndexError:
                lst.append(a[-1])

        temp.append(lst)
        j += 1
    return temp

def all_before(a):
    temp = list()
    j = len(a)-1
    while j >= 0:
        lst = list()
        for i in range(0, j):
            lst.append(a[i])

        for i in range(j, len(a), 2):
            try:
                lst.append(combine(a[i], a[i+1]))
            except IndexError:
                lst.append(a[-1])
        temp.append(lst)
        j -= 1


    return temp


def test2(a, goal):
    before = all_before(a)
    after = all_after(a)
    lst = list()
    for i in range(0,len(before)):
        lst.append(before[i])

    for i in range(0, len(after)):
        lst.append(after[i])

    for i in range(0, len(a)):
        lst.append(one_of_each_minus(a, i))

    for i in range(len(after)):
        for j in range(0, len(after[i])):
            lst.append(one_of_each_minus(after[i], j))
        for j in range(0, len(after[i])):
            lst.append(alternate_minus(after[i], 0))
            lst.append(alternate_minus(after[i], 1))

    for i in range(len(before)):
        for j in range(0, len(before[i])):
            lst.append(one_of_each_minus(before[i], j))
        for j in range(0, len(before[i])):
            lst.append(alternate_minus(before[i], 0))
            lst.append(alternate_minus(before[i], 1))


    lst.append(alternate_minus(a, 0))
    lst.append(alternate_minus(a, 1))

    count = 0
    for i in range(len(lst)):
        if sum(lst[i]) == goal:

            count += 1
        print(sum(lst[i])) 
    return count


def one_of_each_minus(a, i):
    lst = []
    for elem in a:
        lst.append(elem)
    lst[i] = lst[i] * -1
    return lst


def alternate_minus(a, j):
    lst = []
    for elem in a:
        lst.append(elem)
    for i in range(j, len(a), 2):
        lst[i] = lst[i] * -1
    return lst

'''
minus_lst = list()
def minus(a, j):
    lst = [elem for elem in a]

    for i in range(0, len(lst)):
        if i == j:
            continue
        lst[i] *= -1
    return lst


lst = list()
for i in range(len(a)):
    for j in range(i, len(a)):
        lst.append(minus(a, j))

print(lst)
'''
'''
lst = list()
def test3(a, i):
    lst.append(minus(a, i))
    if i >= len(a):
        return lst
    return test3(a, i+1)

print(test3(a, 0))
'''
'''
lst = list()
def test4(a, j):
'''

