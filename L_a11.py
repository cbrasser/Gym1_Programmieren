from turtle import *

wandlaenge = 50

# Mauern
forward(wandlaenge)
right(90)
forward(wandlaenge)
right(90)
forward(wandlaenge)
right(90)
forward(wandlaenge)
color("teal")

# Dach
right(30)
forward(wandlaenge)
right(120)
forward(wandlaenge)
right(30)

up()
forward(wandlaenge)
right(90)
forward(wandlaenge/5)
right(90)
down()

# Türe
forward(wandlaenge/3)
left(90)
forward(wandlaenge/6)
left(90)
forward(wandlaenge/3)
up()
home()

forward(wandlaenge/3)
right(90)
forward(wandlaenge*0.4)
down()

# Fenster
forward(wandlaenge/5)
right(90)
forward(wandlaenge/5)
right(90)
forward(wandlaenge/5)
right(90)
forward(wandlaenge/5)

