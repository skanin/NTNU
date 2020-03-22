# message = '😡😚😀😷😨😥😮😀😩😀😤😩😥😌😀😩😀😷😡😮😮😡😀😤😩😥😀😬😩😫😥😀😣😡😥😳😡😲😎😀😱😚😀😨😯😷😀😣😯😭😥😟😀😡😚😀😨😥😀😤😩😥😤😀😡😭😯😮😧😀😨😩😳😀😦😲😩😥😮😤😳😎'
message = '🍕🚀🍉🐟🐴'
from itertools import permutations
lst = list()
for elem in message:
    lst.append(ord(elem))

lst2 = list(permutations(message, 4))
print(lst2)

lst = sorted(lst)
storst = max(lst)
for i in range(lst[0], storst+1):
    
    for elem in lst2:
        temp = ""
        for elem2 in elem:
            temp += chr(ord(elem2) - i + 65)
        print(temp)
