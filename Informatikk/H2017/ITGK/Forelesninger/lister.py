'''
Sekvens: Et objekt som inneholder flere dataenheter
- Enhetene lagres i sekvens.
Lister og Tupler.
Lister kan endres, tupler kan ikke.


'''

# Oppgave 1:
'''
liste = [1, 3, 5, 7, 9]*5

for i in liste:
    print(i**2)
'''

# Oppgave 2:
'''
liste = [1, 3, 5, 7, 9] * 5

for i in range (0, len(liste)):
    if (i + 1) % 3 == 0:
        print(liste[i]**2)
'''

# Oppgave 3:
'''
liste = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

i = 3

for x in range (1, len(liste), 2):
        liste[x] = i
        i += 3


print(liste)
'''

# Oppgave 4:
