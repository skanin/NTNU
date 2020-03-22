from turtle import *
import time

def flyto(x, y):
    up()
    goto(x, y)
    down()


def fill_circle(farge, radius):
    begin_fill()
    color(farge)
    circle(radius)
    end_fill()


bgcolor("grey")

#Tegner ansikt
flyto(0, -100)
fill_circle("yellow", 100)

#Tegner det ene øyet
flyto(-30, 20)
fill_circle("green", 20)
#pupill
fill_circle("black", 10)

#Tegner det andre øyet
flyto(30, 20)
fill_circle("green", 20)
#pupill
fill_circle("black", 10)

#munnen
flyto(0, -50)
pensize(5)
color("red")
circle(50,30)
circle(50,-60)


time.sleep(5)