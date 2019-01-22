def find_rate(filename, check_rate, acc):
    f = open(filename, "r")
    for line in f:
        line = line.strip() # Fjerner whitespace
        liste = line.split() # Splitter inn i liste av strenger "dato", "rate"
        rate = float(liste[1]) # Tar ut raten
        if round(check_rate, acc) == round(rate, acc):
            print(liste[0], ":", rate)

