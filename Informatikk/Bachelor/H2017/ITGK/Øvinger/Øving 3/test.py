'''
for i in range (1, 6):
    print(i, "gangen: ")
    for j in range (1, 11):
        print(i*j)
'''

for i in range (1, 100):
    for j in range (1 , i):
        if i/j is not i//j:
            print(i)