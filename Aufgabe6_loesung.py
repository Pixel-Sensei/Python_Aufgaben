"""
Aufgabe: Namen aus einer Datei sortieren

Vervollständige den folgenden Python-Code, der eine `.txt`-Datei mit Namen erstellt, diese Namen einliest,
alphabetisch sortiert und ausgibt.
Teile den Code in drei Teile: das Erstellen der Datei, das Einlesen der Namen,
und das Sortieren und Ausgeben der Namen.
"""

# Teil 1: Erstellen der Datei mit Namen
def erstelle_datei(dateiname):
    inhalt = """Anna
Beate
Clara
David
Eva"""
    with open(dateiname, 'w') as datei:
        datei.write(inhalt)

# Teil 2: Einlesen der Namen aus der Datei
def lese_namen_aus_datei(dateiname):
    with open(dateiname, 'r') as datei:
        namen = datei.readlines()
    return [name.strip() for name in namen]

# Teil 3: Sortieren und Ausgeben der Namen
def sortiere_und_ausgeben(namen):
    namen.sort()
    for name in namen:
        print(name)

# Hauptprogramm
def main():
    dateiname = 'namen.txt'
    erstelle_datei(dateiname)
    namen = lese_namen_aus_datei(dateiname)
    sortiere_und_ausgeben(namen)

# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
