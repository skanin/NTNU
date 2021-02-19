def sum_of_intervals(lst):
    dic = dict()
    for i in range(len(lst)):
        dic[str(lst[i])] = 1

    return dic


print(sum_of_intervals([
   [1,4],
   [7, 10],
   [3, 5]
]))