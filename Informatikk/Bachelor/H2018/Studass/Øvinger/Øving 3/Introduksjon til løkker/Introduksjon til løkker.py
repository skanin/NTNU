#A

print("A\n")

for i in range(3):
    adj = input("Beskriv deg selv med et adjektiv? ")
    print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
print("Takk for nå!")


#B

print("\nB\n")

i = 0
while i < 3:
    adj = input("Beskriv deg selv med et adjektiv? ")
    print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
    i += 1  # øker i med 1
print("Takk for nå!")


#C

print("\nC\n")

bokstaver = 42

while bokstaver > 0:
    adj = input("Beskriv deg selv med et adjektiv? ")
    if len(adj) > bokstaver:
        print("Det er ikke mulig med et så langt ord")
    else:
        print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
        bokstaver -= len(adj)

    print("Du har nå " + str(bokstaver) + " bokstaver igjen")

print("Takk for nå!")


#D

print("\nD\n")

print("Tallene i 5-gangen mellom 20 og 81:")
for number in range(10, 81, 5):  ###
    print(number, end=" ")
print()

print("Tallsekvensen 48, 56, 64, 72, 80")
for number in range(48, 81, 8):  ###
    print(number, end=" ")
print()

print("Telle baklengs fra 100 til 80, med intervall på -3, dvs. 100, 97, ...:")
for number in range(100, 80, -3):  ###
    print(number, end=" ")
print()