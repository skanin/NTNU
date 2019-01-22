k = int(input("Skriv inn et heltall: "))
x = 1
y = 1

for i in range(1, k+1):
    if i == 1:
        y = i**2
        if(y > k):
            break
        else:
            x = i**2
    elif i % 2 != 0:
        y = x + i**2
        if(y > k):
            break
        else:
            x = x + i**2
    elif i % 2 == 0:
        y = x - i**2
        if(y > k):
            break
        else:
            x = x - i**2
    z = i
print("Den minste summen før", k, "er:", x, ". Tallrekken kjørte", z, "ganger")