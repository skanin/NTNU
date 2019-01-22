birthdays = {
"22 nov": ["Lars", "Mathias"],
"10 des": " Elle ",
"30 okt": ["Veronica", "Rune"],
"12 jan": "Silje",
"31 okt": "Willy",
"8 jul": ["Brage", "Øystein"],
"1 mar": "Nina"
}

def add_birthday_to_date(date, name):
    temp_list = []
    try:
        birthdays[date].append(name)

    except AttributeError:
        temp_list.append(birthdays[date])
        temp_list.append(name)
        birthdays.pop(date, None)
        birthdays[date] = temp_list

    except KeyError:
        birthdays[date] = name


add_birthday_to_date("30 okt", "Gunnar")
add_birthday_to_date("12 jan", "Sindre")
add_birthday_to_date("9 feb", "Lillian")

print(birthdays)
