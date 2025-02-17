from turtle import *

grösse = 5
wachstum = 2

for i in range(100):
    forward(grösse)
    grösse = grösse + wachstum
    right(90)