def summerOlympics(firstYear, lastYear):
    years = []
    for i in range(firstYear, lastYear+1):
        if i % 4 == 0:
            years.append(i)
    return years


year = summerOlympics(1999, 2012)
print(year)