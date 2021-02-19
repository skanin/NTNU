def multiplikasjonsmatrise(n):
    liste = []
    for i in range(1, n+1):
        temp_liste = []
        for j in range(1, n+1):
            temp_liste.append(i*j)
        liste.append(temp_liste)

    return liste


tabell = multiplikasjonsmatrise(10)

for elem in tabell:
    print(elem)

