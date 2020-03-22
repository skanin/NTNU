def removeDuplicate(liste):
    temp_liste = []
    for elem in liste:
        if elem not in temp_liste:
            temp_liste.append(elem)
    return temp_liste


print(removeDuplicate([1, 2, 2, 2, 3, 7, 21, 4, 4, 5, 5]))
