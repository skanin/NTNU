def lagOgSkriv(filnavn, tekst):
    fil = open(filnavn, "w")
    fil.write(tekst)
    fil.close()


def lagOgLeggTil(filnavn, tekst):
    fil = open(filnavn, "a")
    fil.write(tekst)
    fil.close()
    

lagOgLeggTil("Hei.txt", "Hei, dette er den forste linjen\n")
lagOgLeggTil("Hei.txt", "Hei, dette er den andre linjen\n")
lagOgSkriv("Hei.txt", "Dette skal egt bli den tredje linjen")
