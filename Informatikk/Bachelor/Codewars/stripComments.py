string = "apples, pears # and bananas\ngrapes\nbananas !apples"

def solution(string,markers):
    string = string.split('\n')
    for i in range(len(string)):
        for elem in markers:
            if elem in string[i]:
                string[i] = string[i].replace(" " + elem, elem)
                string[i] = string[i][:(string[i].find(elem))]
                
    return '\n'.join(string)


print(solution(string, ["#", "!"]))

def solution2(string, markers):
    return list(
            map(
                lambda x, elem: x.replace(" "+elem, elem)[:x.find(elem)], string.split('\n'), markers
            )
    )

'''st = solution(string, ["#", "!"])
for elem in st:
    print(elem)

print()
st2 = solution2(string, ["#", "!"])
for elem in st2:
    print(elem)
'''

print(solution2(string, ["#", "!"]))