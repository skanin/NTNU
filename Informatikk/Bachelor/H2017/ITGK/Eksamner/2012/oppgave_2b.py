def currentDate():
    date = (2017, 11, 14)
    return date


def findAge(bYear, bMonth, bDay):
    date = currentDate()
    age = date[0] - bYear

    if bMonth >= date[1]:
        if bDay > date[2]:
            return age-1
        return age
    else:
        return age
