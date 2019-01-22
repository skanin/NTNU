tabell_3x3 = [[0 for col in range(3)] for row in range(3)]

print(tabell_3x3)

tall = 2
for row in range(3):
    for col in range(3):
        tabell_3x3[row][col] = tall
        tall += 2

for rekke in tabell_3x3:
    print(rekke)

