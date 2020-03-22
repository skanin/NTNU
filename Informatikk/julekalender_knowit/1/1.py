f = open('input-vekksort.txt', 'r')
lst = list(map(int, f.read().split()))
f.close()
temp = [lst[0]]

del lst[0]
for elem in lst:
    if elem >= temp[-1]:
        temp.append(elem)

print(sum(temp))
