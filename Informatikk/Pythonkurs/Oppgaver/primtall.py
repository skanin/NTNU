def primtall(n):
    i = 2
    while i < n:
        if n % i == 0:
            return "Tallet er ikke et primtall"
        i += 1

    return "Tallet er et primtall"


print(primtall(70))
