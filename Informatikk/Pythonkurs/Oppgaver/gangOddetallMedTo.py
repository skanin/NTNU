def gang(liste):
    for i in range(len(liste)):
        if liste[i] % 2 != 0:
            liste[i] = liste[i]*2
    return liste


print(gang([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
