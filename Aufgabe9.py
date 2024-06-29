"""
Aufgabe: Verarbeitung einer Liste von Wörtern

Vervollständige den folgenden Python-Code, der eine Liste von Wörtern einliest,
verschiedene Operationen auf dieser Liste durchführt und die Ergebnisse ausgibt.
Teile den Code in drei Teile: das Einlesen der Wörter, das Durchführen der Operationen
und das Ausgeben der Ergebnisse.
"""

# Teil 1: Einlesen der Wörter
def einlesen_woerter():
    woerter = input("Gib eine Liste von Wörtern, getrennt durch Leerzeichen, ein: ").split()
    return ________

# Teil 2: Durchführen der Operationen
def verarbeite_woerter(woerter):
    anzahl_woerter = ________
    sortierte_woerter = ________
    umgekehrte_woerter = ________
    anzahl_buchstaben = ________
    return anzahl_woerter, sortierte_woerter, umgekehrte_woerter, anzahl_buchstaben

# Teil 3: Ausgeben der Ergebnisse
def ausgabe(anzahl_woerter, sortierte_woerter, umgekehrte_woerter, anzahl_buchstaben):
    print(f"Anzahl der Wörter: {________}")
    print(f"Sortierte Wörter: {________}")
    print(f"Umgekehrte Reihenfolge: {________}")
    print(f"Anzahl der Buchstaben pro Wort: {________}")

# Hauptprogramm
def main():
    woerter = einlesen_woerter()
    anzahl_woerter, sortierte_woerter, umgekehrte_woerter, anzahl_buchstaben = verarbeite_woerter(woerter)
    ausgabe(anzahl_woerter, sortierte_woerter, umgekehrte_woerter, anzahl_buchstaben)

# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
