def app(alder, sykkel):
    if alder < 5:
        pris = 0
    elif 5 <= alder <= 20:
        pris = 20
    elif 20 < alder <= 25:
        pris = 50
    elif 25 < alder <= 60:
        pris = 80
    else:
        pris = 0

    if sykkel == "j":
        pris = pris + 50

    if pris == 0:
        print("Din pris: gratis!")
    else:
        print("Din pris: " + str(pris))


app(int(input("Hvor gammel er du? ")), input("Har du med deg sykkel (j/n)? ").lower())
