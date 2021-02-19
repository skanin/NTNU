# a
def recursive_sum(n):
    if n > 0:
        return n + recursive_sum(n-1)
    return n


print("a: " +  str(recursive_sum(10)))


# b
def find_smallest_element(numbers):
    min = numbers[0]
    for i in numbers[0:]:
        if i < min:
            min = i
    return min


print("b: " + str(find_smallest_element([1, 2, 3, 1, 2, 3, 4, 6, 8, -5])))


# c
def binary_search(numbers, element):
    lower = 0
    upper = len(numbers)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = numbers[x]
        if element == val:
            return x
        elif element > val:
            if lower == x:
                break
            lower = x
        elif element < val:
            upper = x


liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(liste, 7))
