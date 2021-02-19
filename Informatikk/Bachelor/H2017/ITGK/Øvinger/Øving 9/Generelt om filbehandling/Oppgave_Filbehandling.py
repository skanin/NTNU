def write_to_file(data):
    filnavn = open("my_file.txt", "a")
    filnavn.write(data + "\n")
    filnavn.close()


def read_from_file(filename):
    filnavn = open(filename, "r")
    print("\nData i filen:\n")
    print(filnavn.read())
    filnavn.close()


def main():
    svar = input("Vil du skrive eller lese fra fil? (R/W) ").lower()

    while svar != "done":
        if svar == "r":
            filename = input("Skriv inn filnavnet på filen du vil lese: ")
            read_from_file(filename)
        elif svar == "w":
            data = input("Skriv inn det du vil legge til i filen\n>>> ")
            write_to_file(data)
            print("Skriver til filen...")
            print("Dataen ble skrevet til filen")

        svar = input("Vil du skrive eller lese fra fil? (R/W) ").lower()


main()
print("Du er ferdig.")
