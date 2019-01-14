def skriv_tegn_index(tekst, tegn):
    teller = 0
    for x in tekst:
        if(x == tegn):
            print(teller)
        teller += 1


streng = "heoaiejgiiiiejdieg"

skriv_tegn_index(streng, "i")
