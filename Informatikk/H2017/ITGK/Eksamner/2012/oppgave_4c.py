from random import randint


def generate_testdata(N, min_value, max_value):
    result = []
    temp_list = []
    for i in range(min_value, max_value+1):
        temp_list.append(i)

    while len(result) != N:
        j = randint(0, N)
        if temp_list[j] not in result:
            result.append(temp_list[j])

    return result


print(generate_testdata(10, -5, 10))
