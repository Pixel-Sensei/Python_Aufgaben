"""
Aufgabe: Ersetze alle Vorkommen von "wuff" durch "miao"

Vervollständige den folgenden Python-Code, der eine `.txt`-Datei namens `wuff.txt` erstellt, diese Datei einliest,
alle Vorkommen des Wortes "wuff" durch "miao" ersetzt und die geänderte Geschichte ausgibt.
Teile den Code in vier Teile: das Erstellen der Datei, das Einlesen des Textes,
das Ersetzen der Wörter und das Ausgeben des geänderten Textes.
"""

# Teil 1: Erstellen der Datei mit der Geschichte
def erstelle_datei(dateiname):
    inhalt = """Es war einmal ein Hund, der machte wuff, wuff, wuff.
Die Leute im Dorf nannten ihn den Wuff-Hund.
Eines Tages traf der Wuff-Hund einen anderen Hund.
Zusammen machten sie wuff, wuff, wuff und hatten viel Spass.
"""
    with open(dateiname, 'w') as datei:
        datei.write(inhalt)

# Teil 2: Einlesen des Textes aus der Datei
def lese_text_aus_datei(dateiname):
    with open(dateiname, 'r') as datei:
        text = datei.read()
    return text

# Teil 3: Ersetzen der Wörter
def ersetze_wuff_durch_miao(text):
    geaenderter_text = text.replace('wuff', 'miao')
    return geaenderter_text

# Teil 4: Ausgeben des geänderten Textes
def ausgabe(text):
    print(text)

# Hauptprogramm
def main():
    dateiname = 'wuff.txt'
    erstelle_datei(dateiname)
    text = lese_text_aus_datei(dateiname)
    geaenderter_text = ersetze_wuff_durch_miao(text)
    ausgabe(geaenderter_text)

# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
