import pandas as pd

"""
Aufgabe: Verarbeitung von Daten mit Pandas

Vervollständige den folgenden Python-Code mit den richtigen Befehlen aus dem Pandas-Modul.
Die Aufgabe umfasst das Laden einer CSV-Datei, das Durchführen von Datenmanipulationen und
das Ausgeben der Ergebnisse.
"""

# Teil 1: Laden der CSV-Datei
def lade_csv_datei(dateipfad):
    daten = pd.read_csv(dateipfad)  # Lücke 1: Funktion zum Laden der CSV-Datei
    return daten

# Teil 2: Durchführen der Operationen
def verarbeite_daten(daten):
    # Lücke 2: Befehl zur Anzeige der ersten 5 Zeilen der Daten
    print(daten.head())  # Lücke 2: Befehl zur Anzeige der ersten 5 Zeilen der Daten
    durchschnitt = daten['SpalteA'].mean()  # Lücke 3: Spalte wählen und Durchschnitt berechnen
    max_wert = daten['SpalteB'].max()  # Lücke 4: Spalte wählen und maximalen Wert finden
    return durchschnitt, max_wert

# Teil 3: Ausgeben der Ergebnisse
def ausgabe(durchschnitt, max_wert):
    print(f"Durchschnittswert: {durchschnitt:.2f}")
    print(f"Maximalwert: {max_wert}")

# Hauptprogramm
def main():
    dateipfad = 'daten.csv'  # Annahme: Die Datei 'daten.csv' befindet sich im aktuellen Verzeichnis
    daten = lade_csv_datei(dateipfad)
    durchschnitt, max_wert = verarbeite_daten(daten)
    ausgabe(durchschnitt, max_wert)

# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
