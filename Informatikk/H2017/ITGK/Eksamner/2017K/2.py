'''
def file_to_list(filename):
    dataList=[]
    f = open(filename)
    for line in f:
        lineList = line.split("\t")
        lineList[1] = float(lineList[1])
        dataList.append(lineList)
    f.close()
    return dataList


print(file_to_list("pricewar.txt"))
'''

f = open("pricewar.txt", "r")
for line in f:
    linelist = line.split("\t")
    print(linelist)
