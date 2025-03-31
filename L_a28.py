import random

zufallszahl = random.randint(1,10)
eingabe = int(input("Rate eine Zahl von 1 bis 10"))

if eingabe < 1:
    print("Lern lesen")
else:
    if eingabe > 10:
        print("Willst du mich veräppeln?")
    else:
        if eingabe == zufallszahl:
            print("Glück gehabt!")
        else:
            print("Ich habe leider kein Foto für dich")
