zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))
operation = input("Wähle eine Operation (+, -, *, /): ")

if operation == "+":
    ergebnis = zahl1 + zahl2
    print(f"{zahl1} + {zahl2} = {ergebnis}")
elif operation == "-":
    ergebnis = zahl1 - zahl2
    print(f"{zahl1} - {zahl2} = {ergebnis}")
elif operation == "*":
    ergebnis = zahl1 * zahl2
    print(f"{zahl1} * {zahl2} = {ergebnis}")
elif operation == "/":
    if zahl2 == 0:
        print("Fehler: Division durch Null ist nicht erlaubt!")
    else:
        ergebnis = zahl1 / zahl2
        print(f"{zahl1} / {zahl2} = {ergebnis}")
else:
    print("Ungültige Operation eingegeben!")