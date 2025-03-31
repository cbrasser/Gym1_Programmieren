punkte = 0

antwort_1 = input("Wie heisst die Hauptstadt der Schweiz? ")
if antwort_1 == "Bern" or antwort_1 == "bern":
    punkte = punkte + 1
    print("korrekt")
else:
    print("Falsch!")


antwort_2 = input("Wie heisst die Hauptstadt von Italien? ")
if antwort_2 == "rom" or antwort_2 == "Rom":
    punkte = punkte + 1
    print("korrekt")
else:
    print("Falsch!")

antwort_3 = input("Wie heisst die Hauptstadt von England? ")
if antwort_3 == "London" or antwort_3 == "london":
    punkte = punkte + 1
    print("korrekt")
else:
    print("Falsch!")
    
print(f"Du hast {punkte}/3 Punkten erreicht!")