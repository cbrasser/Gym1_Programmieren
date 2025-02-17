from turtle import *

grösse = 200
abstand = 5
speed(0)
for i in range(20):
    forward(grösse)
    right(90)
    forward(grösse)
    right(90)
    forward(grösse)
    right(90)
    forward(grösse)
    right(90)
    up()
    forward(abstand)
    right(90)
    forward(abstand)
    left(90)
    down()
    grösse = grösse - 2*abstand