def get_price(konsertnavn):
    f = open("prices.txt", "r")
    for i in f:
        konsert = i.split(";")
        if konsert[0] == konsertnavn:
            return int(konsert[1].rstrip("\n"))
        else:
            return -1

print(get_price("fe"))



