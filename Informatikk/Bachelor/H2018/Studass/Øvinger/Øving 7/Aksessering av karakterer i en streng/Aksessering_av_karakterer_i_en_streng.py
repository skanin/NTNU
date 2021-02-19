print("A--------------------------------------")


def print_char_str(st):
    for ch in st:
        print(ch)


print_char_str("Hei på deg")
print()

print("B--------------------------------------")


def return_third(st):
    if len(st) < 3:
        return 'q'
    return st[2]


print(return_third("Mistborn"))
print(return_third("IT"))
print()
print("C--------------------------------------")


def return_index(st):
    return len(st)-1


print(return_index("The way of Kings"))
print(return_index("Elantris"))