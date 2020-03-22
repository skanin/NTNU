def cap_data(array, min_value, max_value):
    result = []
    for elem in array:
        if elem < min_value:
            elem = min_value
            result.append(elem)
        elif elem > max_value:
            elem = max_value
            result.append(elem)
        else:
            result.append(elem)
    return result


A = [-70, 30, 0, 90, 23, -12, 95, 12]
print(cap_data(A, -50, 50))