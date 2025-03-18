stufen = int(input("Wie gross soll die Pyramide sein? "))

for i in range(1, stufen+1):
    anzahl_sterne = i*2 - 1
    anzahl_space = (stufen - i)
    print(f"{anzahl_space * ' '}{anzahl_sterne * '*'}{anzahl_space * ' '}")
