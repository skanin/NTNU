print("A-------------------------\n")


def return_fourth(st):
    temp = ""
    for i in range(0, len(st), 4):
        temp += st[i]

    return temp


print(return_fourth("I Was Told There’d Be Cake"))
print("B-------------------------\n")
print()


def return_last_two(liste):
    temp = ""
    for st in liste:
        temp += st[-2] + st[-1]

    return temp


print(return_last_two(["sabel", "kan", "mestr", "kuleis"]))



