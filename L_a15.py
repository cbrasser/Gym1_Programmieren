name = input("Wie heisst du?")
anzahl_hefte = int(input("Wie viele Hefte möchtest du? "))
anzahl_stifte = int(input("Wie viele Stifte möchtest du? "))

preis = anzahl_hefte * 2.5 + anzahl_stifte * 1.2

print(f"Bestellung für {name}")
print(f"Anzahl Hefte gekauft: {anzahl_hefte}")
print(f"Anzahl Stifte gekauft: {anzahl_stifte}")
print(f"Gesamtpreis: {preis} Franken")