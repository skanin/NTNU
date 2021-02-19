# a


def add_data(user):
    liste = user.split()
    return liste


print(add_data("Mark Zuckerberg 32 Male Married"))


# b


def get_person(given_name, facebook):
    temp = []
    for i in range(len(facebook)):
        if given_name == facebook[i][0]:
            temp.append(facebook[i])

    return temp


facebook = [["Mark", "Zuckerberg", 32, "Male", "Married"],
                ["Therese", "Johaug", 28, "Female", "Complicated"],
                ["Mark", "Wahlberg", 45, "Male", "Married"],
                ["Siv", "Jensen", 47, "Female", "Single"]]

print(get_person("Mark", facebook))


# c


def main():
    print("Hello, welcome to Facebook. Add a new user by writing 'given_name surname age gender relationship_status'.")
    user = ""
    list_of_users = []
    while user != "done":
        user = input("Add a new user: ")
        list_of_users.append(add_data(user))
        print(list_of_users)
    print("OK")
    search = ""
    while search != "done":
        search = input("Search for a user: ")
        for i in range(len(list_of_users)):
            try:
                if search == list_of_users[i][0]:
                    if list_of_users[i][3] == "Male" or [list_of_users[i][3] == "male"]:
                        print(list_of_users[i][0], list_of_users[i][1], "is", list_of_users[i][2],
                              "years old, his relationship status is", list_of_users[i][4])
                    else:
                        print(list_of_users[i][0], list_of_users[i][1], "is", list_of_users[i][2],
                              "years old, her relationship status is", list_of_users[i][4])
            except IndexError:
                pass
    print("OK")


main()
