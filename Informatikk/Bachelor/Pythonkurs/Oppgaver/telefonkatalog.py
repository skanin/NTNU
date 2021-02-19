def katalog(navn, tlf, dikt):
    if navn in dikt:
        dikt[navn].append(tlf)
    else:
        dikt[navn] = [tlf]

    return dikt


def findInDict(navn, dikt):
    if navn in dikt:
        return dikt[navn]
    else:
        return -1


dikt = {}
katalog("Sander", 98815561, dikt)
katalog("Marcus", 45427570, dikt)

print(dikt)
