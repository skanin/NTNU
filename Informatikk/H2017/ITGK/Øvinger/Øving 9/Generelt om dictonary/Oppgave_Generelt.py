# a

my_family = {}


def add_family_member(key, value):
    temp_liste = []
    if key in my_family:
        temp_liste.append(my_family[key])
        print(temp_liste)
        temp_liste.append(value)
        my_family[key] = temp_liste
    else:
        my_family[key] = value


add_family_member("bror", "Simen")
add_family_member("bror", "Sindre")
add_family_member("bror", "Sander")
add_family_member("bror", "Peder")
add_family_member("mor", "Birgit")
add_family_member("hund", "Lara")
add_family_member("far", "Thor")

print(my_family)
