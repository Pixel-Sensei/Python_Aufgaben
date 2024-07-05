"""
Aufgabe: Maximum und Minimum einer Zahlenliste finden

Vervollständige den folgenden Python-Code, der das Maximum und Minimum einer Liste von Zahlen findet.
Teile den Code in drei Teile: das Einlesen der Zahlenliste, das Finden des Maximums und Minimums,
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

# Teil 2: Finden des Maximums und Minimums
def finde_max_und_min(zahlen):
    maximum = zahlen[0]
    minimum = zahlen[0]
    for zahl in zahlen:
        if zahl > maximum:
            maximum = zahl
        if zahl < minimum:
            minimum = zahl
    return maximum, minimum

# Teil 3: Ausgabe der Ergebnisse
def ausgabe(maximum, minimum):
    print(f"Das Maximum der Zahlen ist: {maximum}")
    print(f"Das Minimum der Zahlen ist: {minimum}")

# Hauptprogramm
def main():
    zahlen = lese_zahlen()
    maximum, minimum = finde_max_und_min(zahlen)
    ausgabe(maximum, minimum)

# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
