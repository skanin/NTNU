import requests
import datetime
import time
t = datetime.datetime.now()


f = requests.get('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-rpslog.txt').text

a_score = 0
b_score = 0
c_score = 0

dic = { 'RRR': 'uavgjort',
        'RRS': 'rematch AB',
        'RRP': 'c',
        'RSR': 'rematch AC',
        'RSS': 'a',
        'RSP': 'uavgjort',
        'RPR': 'b',
        'RPS': 'uavgjort',
        'RPP': 'rematch BC',
        'SRR': 'rematch BC',
        'SRS': 'b',
        'SRP': 'uavgjort',
        'SSR': 'c',
        'SSS': 'uavgjort',
        'SSP': 'rematch AB',
        'SPR': 'uavgjort',
        'SPS': 'rematch AC',
        'SPP': 'a',
        'PRR': 'a',
        'PRS': 'uavgjort',
        'PRP': 'rematch AC',
        'PSR': 'uavgjort',
        'PSS': 'rematch BC',
        'PSP': 'b',
        'PPR': 'rematch AB',
        'PPS': 'c',
        'PPP': 'uavgjort'}


def check_two(st):
    a = st[0]
    b = st[1]

    if a == 'P' and b == 'S':
        return 1
    elif a == 'S' and b == 'P':
        return 0
    elif a == 'R' and b == 'S':
        return 0
    elif a == 'S' and b == 'R':
        return 1
    elif a == 'P' and b == 'R':
        return 0
    elif a == 'R' and b == 'P':
        return 1
    else:
        return -1


j = 0

while j < len(f):
    a = f[j]
    b = f[j+1]
    c = f[j+2]

    st = a+b+c
    if dic[st] == 'a':
        a_score += 1
        j += 3
        continue
    if dic[st] == 'b':
        b_score += 1
        j += 3
        continue
    if dic[st] == 'c':
        c_score += 1
        j += 3
        continue

    if dic[st] == 'uavgjort':
        j += 3
        continue
    elif dic[st] == 'rematch AB':
        j += 3
        a = f[j]
        b = f[j + 1]
        st = a+b
        if check_two(st) == -1:
            j += 2
            a = f[j]
            b = f[j+1]
            st = a + b

            while check_two(st) == -1:
                j += 2
                st = f[j] + f[j+1]

        if check_two(st) == 0:
            a_score += 1
            j += 2
            continue
        if check_two(st) == 1:
            b_score += 1
            j += 2
            continue
    elif dic[st] == 'rematch AC':
        j += 3
        a = f[j]
        c = f[j + 1]
        st = a + c
        if check_two(st) == -1:
            j += 2
            a = f[j]
            c = f[j + 1]
            st = a + c
            while check_two(st) == -1:
                j += 2
                st = f[j] + f[j + 1]

        if check_two(st) == 0:
            a_score += 1
            j += 2
            continue
        if check_two(st) == 1:
            c_score += 1
            j += 2
            continue
    elif dic[st] == 'rematch BC':
        j += 3
        b = f[j]
        c = f[j+1]
        st = b + c
        if check_two(st) == -1:
            j += 2
            b = f[j]
            c = f[j + 1]
            st = b + c
            while check_two(st) == -1:
                j += 2
                st = f[j] + f[j + 1]

        if check_two(st) == 0:
            b_score += 1
            j += 2
            continue
        if check_two(st) == 1:
            c_score += 1
            j += 2
            continue


print(a_score, b_score, c_score)
print(datetime.datetime.now()-t)
