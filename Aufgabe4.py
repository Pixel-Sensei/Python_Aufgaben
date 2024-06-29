"""
Aufgabe: Summe und Durchschnitt aus einer Datei berechnen

Vervollständige den folgenden Python-Code, der die Summe und den Durchschnitt von Zahlen berechnet,
die in einer externen `.txt`-Datei gespeichert sind. Die Datei enthält eine Zahl pro Zeile.
Teile den Code in drei Teile: das Einlesen der Zahlen aus der Datei, das Berechnen der Summe und des Durchschnitts,
und das Ausgeben der Ergebnisse.
"""

# Teil 1: Einlesen der Zahlen aus der Datei
def lese_zahlen_aus_datei(dateiname):
    zahlen = []
    with open(dateiname, 'r') as datei:
        for zeile in datei:
            zahl = int(__________)
            zahlen.append(__________)
    return zahlen

# Teil 2: Berechnen der Summe und des Durchschnitts
def berechne_summe_und_durchschnitt(zahlen):
    summe = 0
    for zahl in zahlen:
        summe += _________
    durchschnitt = summe / len(__________)
    return summe, durchschnitt

# Teil 3: Ausgabe der Ergebnisse
def ausgabe(summe, durchschnitt):
    print(f"Die Summe der Zahlen ist: {summe}")
    print(f"Der Durchschnitt der Zahlen ist: {__________}")

# Hauptprogramm
def main():
    dateiname = 'zahlen.txt'
    zahlen = lese_zahlen_aus_datei(__________)
    summe, durchschnitt = berechne_summe_und_durchschnitt(__________)
    ausgabe(summe, durchschnitt)

# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
