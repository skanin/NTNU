def crc(string, generator):
    pos = 0
    string = string + "0"*(len(generator)-1)
    print(string)
    # string_liste = list(string)
    rest = string[pos:len(generator)]
    while len(string) >= len(generator)-1:
        restTemp = ""
        for i in range(0, len(rest)):
            print("string_sub:",rest[i], "Generator:",generator[i])
            restTemp += str(int(bool(int(rest[i])) != bool(int(generator[i]))))


        rest = str(int(restTemp))
        if rest == "0":
            rest = ""

        print("Rest før while:",rest)
        print("String før while:", string)
        while len(rest) < len(generator):
            if len(string) == 0:
                break

            rest += string[0]
            print("Hei")
            string = string[1::]


        if len(string) < len(generator) and len(rest) < len(generator):
            break
        print("String:",string)
        print("Rest:", rest)

    print(rest)


crc("10001", "1100")
