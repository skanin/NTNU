
def bubble_sort(list):

    sortedList = list
    
    print(list)
    sortedList.sort()     #hvordan ikke sorte list? / hvordan fungerer pekere?
    print(list)

    mellomregning = sortedList[-1]
    list.append(mellomregning+1)
    print(list)

    while list != list.sort():   #Og her er jo de to like, så hvorfor starter løkka
        for x in range (0, len(list)-1):
            a = list[x]
            b = list[x+1]
            print(a, b)
            if (a > b):
                print('in if')
                a = list[x]
                b = list[y]
                list[x] = b
                list[y] = a
        print('after for')
    print('after while')

    list.pop()
    return list



liste = [0,9,1,8,2,7,3,6,4,5]
print(bubble_sort(liste))
