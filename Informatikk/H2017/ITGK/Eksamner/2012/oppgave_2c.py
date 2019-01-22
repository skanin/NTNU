from oppgave_2b import findAge


def printAge(table):
    for i in range(len(table)-1):
        if findAge(table[i][2], table[i][3], table[i][4]) == findAge(table[i+1][2], table[i+1][3], table[i+1][4]):
            print(table[i][0] + " " + table[i][1] + " is the same age as " + table[i+1][0] + " " + table[i+1][1])
        elif findAge(table[i][2], table[i][3], table[i][4]) < findAge(table[i+1][2], table[i+1][3], table[i+1][4]):
            print(table[i][0] + " " + table[i][1] + " younger than " + table[i + 1][0] + " " + table[i + 1][1])
        else:
            print(table[i][0] + " " + table[i][1] + " older than " + table[i + 1][0] + " " + table[i + 1][1])


personer = [['Justin','Bieber',1994,3,1],['Donald','Duck',1934,8,1],['George','Clooney',1961,5,6],['Eddie','Murphy',1961,4,3]]


printAge(personer)