def cold_days(temlist):
    temperatures = []
    for temp in temlist:
        if temp < 0:
            temperatures.append(temp)
    days = len(temperatures)
    return days


print(cold_days([1, -5, 3, 0, -6, -3, 15, 0]))