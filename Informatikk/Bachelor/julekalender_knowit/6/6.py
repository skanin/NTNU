import datetime
now = datetime.datetime.now()
print(sum(list(filter(lambda x: str(x).count('0') > len(str(x))/2, [i for i in range(1, 18163107)]))))
print(datetime.datetime.now() - now)