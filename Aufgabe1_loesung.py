"""
Aufgabe: Summe und Durchschnitt berechnen

Vervollständige den folgenden Python-Code, der die Summe und den Durchschnitt einer Liste von Zahlen berechnet.
Teile den Code in drei Teile: das Einlesen der Zahlenliste, das Berechnen der Summe und des Durchschnitts,
und das Ausgeben der Ergebnisse.
"""

# Teil 1: Einlesen der Zahlenliste
def lese_zahlen():
    zahlen = []
    anzahl = int(input("Wie viele Zahlen möchtest du eingeben? "))
    for _ in range(anzahl):
        zahl = int(input("Gib eine Zahl ein: "))
        zahlen.append(zahl)
    return zahlen

# Teil 2: Berechnen der Summe und des Durchschnitts
def berechne_summe_und_durchschnitt(zahlen):
    summe = 0
    for zahl in zahlen:
        summe += zahl
    durchschnitt = summe / len(zahlen)
    return summe, durchschnitt

# Teil 3: Ausgabe der Ergebnisse
def ausgabe(summe, durchschnitt):
    print(f"Die Summe der Zahlen ist: {summe}")
    print(f"Der Durchschnitt der Zahlen ist: {durchschnitt}")

# Hauptprogramm
def main():
    zahlen = lese_zahlen()
    summe, durchschnitt = berechne_summe_und_durchschnitt(zahlen)
    ausgabe(summe, durchschnitt)

# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
