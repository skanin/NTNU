# a

number_list = []

for i in range(0, 100):
    number_list.append(i)

    
# b

sum = 0
for num in number_list:
    if(num % 3 == 0) or (num % 10 == 0):
        sum += num


print("Summen er " + str(sum))

# c

for i in range(len(number_list)):
    if(number_list[i] % 2 == 0):
        number_list[i] = number_list[i+1]
    else:
        number_list[i] = number_list[i]-1

   
print(number_list)

# d
number_list.sort()
lengde = len(number_list)

reversed_list = [None] * lengde

for item in number_list:
    lengde = lengde - 1
    reversed_list[lengde] = item

print(reversed_list)
