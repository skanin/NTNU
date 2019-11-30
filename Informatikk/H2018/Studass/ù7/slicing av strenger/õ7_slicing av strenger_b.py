
def get2Last(li):
    getLi = []

    for x in range (0, len(li)):
        string = ' '.join(li[x])
        newLi = string.split(' ', -1)
        getLi.append(newLi[-2])
        getLi.append(newLi[-1])

    return getLi


ordLi = ['xxx12', 'xxx34', 'xxx56', 'xxx78', 'xxx90']
print(get2Last(ordLi))
