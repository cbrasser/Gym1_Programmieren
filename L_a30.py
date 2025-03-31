geheimes_passwort = "p4ssw0rd"
for i in range(1,4):
    eingegebenes_passwort = input("Gib dein Passwort ein: ")
    if geheimes_passwort == eingegebenes_passwort:
        print(f"korrekt, {i} Versuche benötigt")
        break
    else:
        if i == 3:
            print("Falsch, blockiert!")
        else:
            print(f"Falsch, noch {3-i} Versuche")
