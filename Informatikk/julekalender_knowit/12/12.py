message = '😡😚😀😷😨😥😮😀😩😀😤😩😥😌😀😩😀😷😡😮😮😡😀😤😩😥😀😬😩😫😥😀😣😡😥😳😡😲😎😀😱😚😀😨😯😷😀😣😯😭😥😟😀😡😚😀😨😥😀😤😩😥😤😀😡😭😯😮😧😀😨😩😳😀😦😲😩😥😮😤😳😎'
lst = list()
for elem in message:
    lst.append(ord(elem))

storst = max(lst)
for i in range(128502, storst+1):
    temp = ""
    for elem in lst:
        temp += chr(elem - i + 65)
    print(temp)
