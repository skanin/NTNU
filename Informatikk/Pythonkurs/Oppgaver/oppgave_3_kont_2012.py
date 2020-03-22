def mshd2s(minutter, sekunder, hundredeler):
    m = minutter * 60
    s = sekunder
    h = hundredeler/100

    antall_sek = m+s+h
    return antall_sek


#print(mshd2s(2, 10, 20))

def rundeTid(startTid, sluttTid):
    return mshd2s(sluttTid[0], sluttTid[1], sluttTid[2]) - mshd2s(startTid[0], startTid[1], startTid[2])


#print(rundeTid([0, 45, 20], [1, 32, 55]))


def alleRundeTider(passeringsTider):
    liste = []
    for i in range(len(passeringsTider)-1):
        liste.append(rundeTid(passeringsTider[i], passeringsTider[i+1]))
    return liste