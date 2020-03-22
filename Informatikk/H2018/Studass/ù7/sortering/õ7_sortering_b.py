
def selection_sort(list):
    aList = []

    for x in range (0, len(list)):
        aList.insert(0, max(list))
        list.pop(list.index(max(list)))
    return aList



liste = [0,9,1,8,2,7,3,6,4,5,13,1984,1776,11,22,33,1111,777,666]
print(selection_sort(liste))
