"""
Aufgabe: Häufigste Wörter zählen

Vervollständige den folgenden Python-Code, der die häufigsten Wörter in einer externen `.txt`-Datei zählt.
Teile den Code in drei Teile: das Einlesen des Textes aus der Datei, das Zählen der Wörter,
und das Ausgeben der häufigsten Wörter.
"""

from collections import Counter

# Teil 1: Einlesen des Textes aus der Datei
def lese_text_aus_datei(dateiname):
    with open(dateiname, 'r') as datei:
        text = datei.read()
    return text

# Teil 2: Zählen der Wörter
def zaehle_woerter(text):
    woerter = text.split()
    wort_zaehler = Counter(woerter)
    return wort_zaehler

# Teil 3: Ausgabe der häufigsten Wörter
def ausgabe(wort_zaehler):
    haeufigste_woerter = wort_zaehler.most_common(5)
    for wort, anzahl in haeufigste_woerter:
        print(f"{wort}: {anzahl}")

# Hauptprogramm
def main():
    dateiname = 'text.txt'
    text = lese_text_aus_datei(dateiname)
    wort_zaehler = zaehle_woerter(text)
    ausgabe(wort_zaehler)

# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
