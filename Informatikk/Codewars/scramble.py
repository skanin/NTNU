def scramble(s1, s2):
    dic1 = dict()
    dic2 = dict()

    for elem in s1:
        if elem in dic1:
            dic1[elem] += 1
        else:
            dic1[elem] = 1

    for elem in s2:
        if elem in dic2:
            dic2[elem] += 1
        else:
            dic2[elem] = 1

    for key in dic2:
        if key not in dic1:
            return False
        if dic1[key] < dic2[key]:
            return False

    return True


print(scramble('rkqodlw', 'world'))
print("-----------------------------------------------")
print(scramble('cedewaraaossoqqyt', 'codewars'))
print("-----------------------------------------------")
print(scramble('katas', 'steak'))
print("-----------------------------------------------")
print(scramble('scriptjava', 'javascript'))
print("-----------------------------------------------")
print(scramble('scriptingjava', 'javascript'))
