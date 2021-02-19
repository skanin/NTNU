import math

# a:


def lag_vektor(komp1, komp2, komp3):
    vektor = [komp1, komp2, komp3]
    return vektor


# b:


def print_vektor(vec1):
    return print("Vec1: ", vec1)


# c:


def skalar(vec, skal):
    vec2 = [None, None, None]
    for i in range(len(vec)):
        vec2[i] = skal*vec[i]

    return vec2

# d:


def lengde(vec):
    length = math.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
    return length

# e:


def prikkeprodukt(vec1, vec2):
    produkt = 0
    for i in range(len(vec1)):
        produkt += (vec1[i]*vec2[i])

    return produkt


komponent1, komponent2, komponent3 = input("Skriv inn tre komponenter (separer med mellomrom): ").split()

vektor = lag_vektor(float(komponent1), float(komponent2), float(komponent3))

print_vektor(vektor)

print(vektor, "har lengde:", lengde(vektor))

skal1 = int(input("Skriv inn et skalar: "))

skalert_vektor = skalar(vektor, skal1)

print(str(skal1) + " *", vektor, "=", skalert_vektor)

print(skalert_vektor, "har lengde:", lengde(skalar(vektor, skal1)))

print("Forholdet mellom lengdene er: ", lengde(vektor)/lengde(skalar(vektor, skal1)))

komponent4, komponent5, komponent6 = input("Skriv inn tre komponenter (separer med mellomrom): ").split()

vec2 = lag_vektor(float(komponent4), float(komponent5), float(komponent6))

print("Prikkeproduktet er mellom ", vektor, "og", vec2, "er", prikkeprodukt(vektor, vec2))
