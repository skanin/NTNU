dic = {}

trib = []

def tribonacci(signature, n):
    if n == 0:
        return []

    if n in [1,2,3]:
        return signature[n-1]

    f = 0
    if n in dic:
        return dic[n]
    else:
        f = tribonacci(signature, n-1) + tribonacci(signature, n-2) + tribonacci(signature, n-3)

    dic[n] = f
    trib.append(f)

    return dic[n]


print(tribonacci([1, 1, 1], 10))
print(trib)