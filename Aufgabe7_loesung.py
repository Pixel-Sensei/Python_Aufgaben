"""
Aufgabe: Namen und Alter aus einer Datei sortieren und hinzufügen

Vervollständige den folgenden Python-Code, der eine `.txt`-Datei mit Namen und Alter erstellt, diese Daten einliest,
alphabetisch nach Namen sortiert und ausgibt. Ausserdem soll es möglich sein, weitere Namen und Alter zur Datei hinzuzufügen.
Teile den Code in fünf Teile: das Erstellen der Datei, das Einlesen der Namen und Alter, das Sortieren und Ausgeben der Namen und Alter,
das Hinzufügen neuer Namen und Alter, und das Speichern der aktualisierten Daten.
"""

# Teil 1: Erstellen der Datei mit Namen und Alter
def erstelle_datei(dateiname):
    inhalt = """Anna,25
Beate,30
Clara,22
David,28
Eva,35"""
    with open(dateiname, 'w') as datei:
        datei.write(inhalt)

# Teil 2: Einlesen der Namen und Alter aus der Datei
def lese_namen_und_alter_aus_datei(dateiname):
    daten = []
    with open(dateiname, 'r') as datei:
        for zeile in datei:
            name, alter = zeile.strip().split(',')
            daten.append((name, int(alter)))
    return daten

# Teil 3: Sortieren und Ausgeben der Namen und Alter
def sortiere_und_ausgeben(daten):
    daten.sort()
    for name, alter in daten:
        print(f"{name}, {alter}")

# Teil 4: Hinzufügen neuer Namen und Alter
def hinzufuegen_neue_namen_und_alter(daten):
    while True:
        name = input("Gib einen Namen ein (oder 'stop' zum Beenden): ")
        if name.lower() == 'stop':
            break
        alter = int(input("Gib das Alter ein: "))
        daten.append((name, alter))

# Teil 5: Speichern der aktualisierten Daten
def speichern_daten(dateiname, daten):
    with open(dateiname, 'w') as datei:
        for name, alter in daten:
            datei.write(f"{name},{alter}\n")

# Hauptprogramm
def main():
    dateiname = 'namen_und_alter.txt'
    erstelle_datei(dateiname)
    daten = lese_namen_und_alter_aus_datei(dateiname)
    sortiere_und_ausgeben(daten)
    hinzufuegen_neue_namen_und_alter(daten)
    speichern_daten(dateiname, daten)
    print("Aktualisierte Liste:")
    sortiere_und_ausgeben(daten)

# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
