import pandas as pd

"""
Aufgabe: Fortgeschrittene Verarbeitung von Daten mit Pandas

Vervollständige den folgenden Python-Code mit den richtigen Befehlen aus dem Pandas-Modul.
Die Aufgabe umfasst das Laden einer CSV-Datei, das Filtern von Daten, das Hinzufügen neuer Spalten
und das Ausgeben der Ergebnisse.
"""


# Teil 1: Laden der CSV-Datei
def lade_csv_datei(dateipfad):
    daten = pd.______(dateipfad)  # Lücke 1: Funktion zum Laden der CSV-Datei
    return daten


# Teil 2: Durchführen der Operationen
def verarbeite_daten(daten):
    # Lücke 2: Filtern der Daten für Werte in 'SpalteA', die größer als 10 sind
    gefilterte_daten = daten[______]

    # Lücke 3: Hinzufügen einer neuen Spalte 'Produkt' als Produkt von 'SpalteA' und 'SpalteB'
    daten['Produkt'] = _______

    # Lücke 4: Berechnen des Gesamtwerts in der 'SpalteB'
    gesamt_wert = _______

    return gefilterte_daten, gesamt_wert


# Teil 3: Ausgeben der Ergebnisse
def ausgabe(gefilterte_daten, gesamt_wert):
    print("Gefilterte Daten:")
    print(gefilterte_daten)
    print(f"Gesamtwert in SpalteB: {gesamt_wert}")


# Hauptprogramm
def main():
    dateipfad = 'daten.csv'  # Annahme: Die Datei 'daten.csv' befindet sich im aktuellen Verzeichnis
    daten = lade_csv_datei(dateipfad)
    gefilterte_daten, gesamt_wert = verarbeite_daten(daten)
    ausgabe(gefilterte_daten, gesamt_wert)


# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
