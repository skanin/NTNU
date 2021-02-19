n = int(input("Skriv inn et heltall: "))
x = 1

for i in range(1, n+1):
    if i == 1:
        x = i**2
    elif i % 2 != 0:
        x = x + i**2
    else:
        x = x - i**2
    y = i

print("Tallrekken ga summen:", x, "og kjørte", y, "ganger")
