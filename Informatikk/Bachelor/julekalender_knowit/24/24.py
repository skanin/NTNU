lst = ['A']
# Å = 197
# Æ = 198
# Ø = 216

'''
j = 0
while ''.join(lst) != "AA":
    if lst != []:
        if lst.count("Å") == len(lst):
            for i in range(len(lst)):
                lst[i] = "A"

            lst.insert(0, 'A')
        else:
            if 'Å' in lst:
                for i in range(len(lst)):
                    if lst[i] == 'Å':
                        lst[i-1] = chr(ord(lst[i-1]) + 1)
            else:
                for i in range(len(lst)-1, -1, -1):
                    if lst[i] == 'Z':
                        lst[i] = 'Æ'
                    if lst[i] == 'Æ':
                        lst[i] = 'Ø'
                    if lst[i] == 'Ø':
                        lst[i] = 'Å'

                lst[-1] = chr(ord(lst[-1]) + 1)

    else:
        lst.append("A")

    j += 1


print(''.join(lst), j)
'''

'''
j = 1
while ''.join(lst) != "AÅA":
    j += 1
    print(''.join(lst))
    if lst.count('Å') == len(lst):
        for i in range(len(lst)):
            lst[i] = 'A'
        lst.append('A')
        continue

    if len(lst) == 1 and not ord(lst[-1]) >= 90:
        lst[-1] = chr(ord(lst[-1]) + 1)
        continue

    if len(lst) == 1 and ord(lst[-1]) >= 90:
        if lst[-1] == 'Z':
            lst[-1] = 'Æ'
        elif lst[-1] == 'Æ':
            lst[-1] = 'Ø'
        elif lst[-1] == 'Ø':
            lst[-1] = 'Å'
        continue

    if 'Å' in lst:
        for i in range(len(lst)-1, -1, -1):
            if lst[i] == 'Å' and lst[i-1] != 'Å':
                if lst[i-1] == 'Z':
                    lst[i-1] = 'Æ'
                elif lst[i-1] == 'Æ':
                    lst[i-1] = 'Ø'
                elif lst[i-1] == 'Ø':
                    lst[i-1] = 'Å'
                    break
                else:
                    lst[i-1] = chr(ord(lst[i-1]) + 1)
                lst[i] = 'A'
                break
    else:
        if lst[-1] == 'Z':
            lst[-1] = 'Æ'
        elif lst[-1] == 'Æ':
            lst[-1] = 'Ø'
        elif lst[-1] == 'Ø':
            lst[-1] = 'Å'
        else:
            lst[-1] = chr(ord(lst[-1]) + 1)
        continue






print(''.join(lst), j)
'''
'''
dic = {'A': 1,
       'B': 2,
       'C': 3,
       'D': 4,
       'E': 5,
        }
'''
st = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"

inp = "GODJULOGGODTNYTTÅR"

summen = 0
for i in range(len(inp)):
    if i == len(inp) - 1:
        summen += st.index(inp[i]) + 1
    else:
        summen += (st.index(inp[i])+1) * 29**(len(inp)-i-1)

print(summen)