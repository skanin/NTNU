def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(round(n**0.5 + 0.5))):
        if n % i == 0:
            return False

    return True


def overskudds_tall(n):
    summ = 0
    for i in range(1, n):
        if n % i == 0:
            summ += i

    return summ > n


def inneklemt_riking(n):
    return is_prime(n-1) and is_prime(n+1)


lst = []
for i in range(1, 10000000):
    print(i)
    if inneklemt_riking(i) and overskudds_tall(i):
        lst.append(i)


print(sum(lst))

"""        
summ = 0
for elem in lst:
    if inneklemt_riking(elem):
        sum+=elem

print(summ)

"""

print("Summen: ", sum(lst))