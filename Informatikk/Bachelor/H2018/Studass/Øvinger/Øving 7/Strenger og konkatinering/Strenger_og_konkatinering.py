print("A-------------------------\n")


def concat_str(str1, str2):
    return str1 + " " + str2


print(concat_str("James", "Bond"))
print()
print("B-------------------------\n")


def return_list_as_string(liste):
    temp = ""
    for st in liste:
        temp += st
    return temp


print(return_list_as_string(["abc", "defg", "hijklm", "nop"]))
print("C-------------------------\n")
print()


def print_first_char(liste):
    for st in liste:
        print(st[0])


print_first_char(["UKA", "lever", "videre"])