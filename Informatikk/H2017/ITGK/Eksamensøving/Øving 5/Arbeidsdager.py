def is_leap_year (year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


def weekday_newyear(year):
    if year == 1900:
        return str(year) + " man"
    else:
        day = 0
        for i in range(1901, year+1):
            if day == 6:
                day = -1

            if is_leap_year(i-1):
                if day == 5:
                    day = 0
                else:
                    day += 2
            else:
                day += 1

        if day == 0:
            return str(year) + " man"
        elif day == 1:
            return str(year) + " tir"
        elif day == 2:
            return str(year) + " ons"
        elif day == 3:
            return str(year) + " tor"
        elif day == 4:
            return str(year) + " fre"
        elif day == 5:
            return str(year) + " lør"
        elif day == 6:
            return str(year) + " søn"


for j in range(1900, 1920):
    print(weekday_newyear(j))


def is_work_day(day):
    if day == "lør" or day == "søn":
        return False
    else:
        return True

