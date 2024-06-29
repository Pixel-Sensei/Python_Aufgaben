# Aufgabe: `ValueError` generieren und behandeln

# Teil 1: Initialisiere eine Zeichenkette, die keine Zahl ist
# Lücke 1: Initialisiere eine Variable 'ungültige_zahl' mit der Zeichenkette 'abc'
ungültige_zahl = ________

# Teil 2: Versuche, die Zeichenkette in eine Ganzzahl umzuwandeln und fange die Ausnahme ab
try:
    # Lücke 2: Versuche, 'ungültige_zahl' in eine Ganzzahl umzuwandeln
    zahl = int(________)
except ________ as e:  # Lücke 3: Fange die ValueError-Exception ab
    # Lücke 4: Gib eine Fehlermeldung aus, die den Fehler beschreibt
    print("Fehler: Die Zeichenkette kann nicht in eine Ganzzahl umgewandelt werden.")
    print("Fehlermeldung:", ________)
