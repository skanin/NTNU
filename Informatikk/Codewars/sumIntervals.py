def sumIntervals(arr):
    arrSorted = sorted(arr, key=lambda x: x[0])
    flag = True
    temp = []
    while flag:
        flag = False
        for i in range(0, len(arrSorted)-1, 2):
            if arrSorted[i][1] > arrSorted[i+1][1]:
                val1 = arrSorted[i][1]
                val2 = arrSorted[i+1][2]

                temp.append(arrSorted[i])
                temp.append(arrSorted[i+1])

                temp.append([val1, val2])