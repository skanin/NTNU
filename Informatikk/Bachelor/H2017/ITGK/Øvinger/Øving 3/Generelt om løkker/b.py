x = 1
i = 1
while i < 1000:
    i = i + 1
    x = x * i

    if(x > 1000):
        break

print("Løkken kjørte", i, "ganger, produktet ble", x)