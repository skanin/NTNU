def bin_search(liste, verdi, min, max):
    if max < min:
        return "Ikke funnet"
    else:
        midtpunkt = (min + max)//2
        if verdi < liste[midtpunkt]:
            return bin_search(liste, verdi, min, midtpunkt-1)
        elif verdi > liste[midtpunkt]:
            return bin_search(liste, verdi, midtpunkt+1, max)
        else:
            return midtpunkt


liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(bin_search(liste, 7, 0, 9))
