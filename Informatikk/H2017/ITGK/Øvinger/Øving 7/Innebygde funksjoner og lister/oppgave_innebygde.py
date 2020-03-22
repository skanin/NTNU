import random
import statistics
# a


random_numbers = [random.randint(0, 100) for i in range(0, 100)]
print(random_numbers)

# b

count = 0
for num in random_numbers:
    if num == 2:
        count += 1

if count == 1:
    print("Det er 1 2er i listen")
else:
    print("Det er " + str(count) + " 2ere i listen")


# c

sum = 0
for num in random_numbers:
    sum += num

print("Summen av tallene i listen er " + str(sum))


# d

sortert_liste = sorted(random_numbers)
print("Listen sortert:", sortert_liste)


# e


try:
    print("Tallet det er mest av i listen er", statistics.mode(random_numbers))
except statistics.StatisticsError:
    print("Det er mer enn ett typetall")


# f

reversed_list = []
for i in reversed(sorted(random_numbers)):
    reversed_list.append(i)

print("Reversert liste:", reversed_list)