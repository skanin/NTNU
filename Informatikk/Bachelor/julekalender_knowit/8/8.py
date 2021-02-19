f = open('input-dolls.txt', 'r')
lst = [line.strip().split(',') for line in f.readlines()]

for i in range(len(lst)):
    lst[i][1] = int(lst[i][1])


def vekksort(arr):
    temp = []
    temp.append(arr[0])

    del lst[0]
    for i in range(len(arr)):
        if arr[i][0] != temp[-1][0] and arr[i][1] > temp[-1][1]:
            temp.append(arr[i])

    return len(temp)


lst.sort(key=lambda x:x[1])
print(vekksort(lst))