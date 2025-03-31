from turtle import *

# Benutzer wählt Form und Farbe
form = input("Welche Form möchtest du zeichnen? (Kreis, Quadrat, Dreieck): ")
farbe = input("Welche Farbe? (rot, grün, blau, gelb): ")

speed(1)

# Farbauswahl
if farbe == "rot":
    color("red")
elif farbe == "grün":
    color("green")
elif farbe == "blau":
    color("blue")
elif farbe == "gelb":
    color("yellow")
else:
    print("Unbekannte Farbe, verwende schwarz.")
    color("black")

# Formauswahl und Zeichnen
if form == "Kreis":
    circle(50)
elif form == "Quadrat":
    for i in range(4):
        forward(100)
        right(90)
elif form == "Dreieck":
    for i in range(3):
        forward(100)
        right(120)
else:
    print("Unbekannte Form. Zeichne einen Stern.")
    for i in range(5):
        forward(100)
        right(144)
