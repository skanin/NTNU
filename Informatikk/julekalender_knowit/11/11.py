#file = open("input-crisscross.txt", "r").read()
import requests

file = requests.get('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-bounding-crisscross.txt').text
#file = "2H2F2H1B3V"
h, f, b, v = 0, 0, 0, 0

for i in range(1, len(file), 2):
    c = file[i]
    num = int(file[i-1])
    if c == 'H':
        h += num
    elif c == 'F':
        f += num
    elif c == 'V':
        v += num
    else:
        b += num


print([h-v, f-b])