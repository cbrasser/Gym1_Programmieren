punkte = int(input("Gib deine Punktzahl (0-100) ein: "))

if punkte >= 90:
    note = "6 - Sehr gut"
else:
    if punkte >= 80:
        note = "5 - Gut"
    else:
        if punkte >= 70:
            note = "4 - Ausreichend"
        else:
            note = "Ungenügend"

print(f"Bei {punkte} Punkten erhältst du die Note: {note}")