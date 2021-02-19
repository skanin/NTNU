#a
def separate(numbers, threshold):
    mindre_liste = []
    mindre_lik_liste = []
    for i in range(len(numbers)):
        if numbers[i] < threshold:
            mindre_liste.append(numbers[i])
        elif numbers[i] >= threshold:
            mindre_lik_liste.append(numbers[i])

    return mindre_liste, mindre_lik_liste


print(separate([i for i in range(0, 50)], 10))

# b


def multiplication_table(n):
    liste = [[0 for x in range(n)] for y in range(n)]

    for i in range(1, len(liste)+1):
        for j in range(1, len(liste)+1):
            liste[i-1][j-1] = (i*j)

    return liste


print(multiplication_table(4))
