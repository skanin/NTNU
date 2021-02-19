from turtle import *
print("Jeg kan tegne et regulært polygon!")

sider = int(input("Hvor mange sider?: "))
omkrets = int(input("Velg omkrets: "))

vinkel = 360/sider
piksler = omkrets/sider

for i in range(sider):
    forward(piksler)
    left(vinkel)
done()