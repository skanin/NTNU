from user import User

users = []


def add_data():
    data = input("Data: ").split(" ")
    if len(data) == 5:
        u = User()
        u.set_info(data)
        users.append(u)
    return data


def get_person(given_name, facebook):
    for u in facebook:
        if u.get_given_name() == given_name:
            return u
    return []


def main():
    data = ""
    while not data == ["done"]:
        data = add_data()

    search = ""
    while True:
        search = input("Search for user: ")
        if search.lower() == "done":
            break

        print(get_person(search, users))


main()