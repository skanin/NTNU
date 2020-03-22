'''
def funksjon(liste, item):
    for element in liste:
        if element == item:
            return True
    return False


liste = [1, 2, 3, 4, 5, 6, 7, 8]
print(funksjon(liste, 100))
'''

liste = [3, 7, 3, 1, 4, 6, 7, 3, 1, 5, 8]


def ins_sort(liste):
    for i in range(len(liste)-1):
        element = liste[i]
        hull = i
        while hull > 0 and liste[hull-1] > element:
            liste[hull] = liste[hull-1]
            hull -= 1
            liste[hull] = element
    return liste


print(ins_sort(liste))
