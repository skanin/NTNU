
def bubble_sort(list):
    høyeste = max(list) + 1
    list.append(høyeste)
    sortedList = []

    while len(list) != 0:
    
        if list[0] == min(list):
            sortedList.append(list[0])
            del list[0]

        for x in range (0, len(list)-1):
            a = list[x]
            b = list[x+1]
            if (a > b):
                a = list[x]
                b = list[x+1]
                list[x] = b
                list[x+1] = a

    sortedList.pop()
    return sortedList



liste = [0,9,1,8,2,7,3,6,4,5,13,1984,1776,11,22,33,1111,777,666]
print(bubble_sort(liste))
