'''
Det srives ut [88, 92, 100]
Det skrives ut 100
'''


fruit = dict()

fruit['epler'] = 2
fruit['pærer'] = 3
fruit['appelsiner'] = 1

fruit['bananer'] = 0
fruit['druer'] = 1
del fruit['epler']
del fruit['pærer']
del fruit['appelsiner']

print(fruit)
if 'bananer' in fruit:
    del fruit['bananer']

print(fruit)

fruit['jordbær'] = 10
fruit['blåbær'] = 50

for key in fruit:
    print(key, fruit[key])



