my_family = {}


def add_family_member(role, name):
    if role in my_family:
        my_family[role].append(name)
    else:
        my_family[role] = [name]


add_family_member('mor', 'Birgit')
add_family_member('far', 'Thor')
add_family_member('bror', 'Simen')
add_family_member('bror', 'Sindre')
add_family_member('hund', 'Lara')


def print_dict(dict):
    for key in dict:
        print(key + ": ", end='')
        for val in dict[key]:
            if len(my_family[key]) > 1 and not (val == my_family[key][-1]):
                print(val.rjust(20-len(val)), end=', ')
            else:
                print(val.rjust(20-len(val)), end=' ')
        print()


print_dict(my_family)



print(my_family)