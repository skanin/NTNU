import requests

f = requests.get('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-gullbursdag.txt').text.strip().split("\n")
f = [elem.split("-")[1].split(".") for elem in f]

count = 0
for i in range(len(f)):
    j = 1
    year = int(f[i][1][-4::])
    while j <= year:
        if j**2 == year + j:
            count += 1
            break
        j += 1

print(count)
