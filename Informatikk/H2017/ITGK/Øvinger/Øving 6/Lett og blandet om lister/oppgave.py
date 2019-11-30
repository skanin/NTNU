def is_six_at_edge(liste):
    if (liste[0] or liste[-1]) == 6:
        return True
    else:
        return False


def average(liste):
    return "Gjennomsnitt: " + str(sum(liste)/len(liste))


def median(liste):
    liste.sort()
    i = len(liste)//2
    return liste[int(i)]


min_liste = [1, 3, 8, 4, 3, 1, 5, 8, 6, 3, 8, 7]

print("Er 6 på starten eller slutten?: " + str(is_six_at_edge(min_liste)))

print(average(min_liste))

print(median(min_liste))