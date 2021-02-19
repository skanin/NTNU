#from oppgave_4d import create_db


def print_db(weather):
    header = "Day".rjust(4) + "Temp".rjust(6) + "Rain".rjust(6) + "Humidity".rjust(10) + "Wind".rjust(6)
    print(header)
    print("====+======+======+========+======")
    s = ""
    for x in weather:
        liste = weather[x]
        for i in range(x):
            if i == 0:
                s += weather[i].rjust(4)
            elif 0 < i < 3:
                s += weather[i].rjust(6)
            elif i == 3:
                s += weather[i].rjust(10)
            else:
                s += weather[i].rjust(6)

    print(s)


temp = [1, 5, 3]
rain = [0, 30, 120]
humidity = [30, 50, 65]
wind = [3, 5, 7]

print_db({1: [1, 0, 30, 3], 2: [5, 30, 50, 5], 3: [3, 120, 65, 7]})
