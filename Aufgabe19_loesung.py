# Aufgabe: `while`-Schleife mit `if`-Bedingung

# Teil 1: Initialisiere eine Variable für die Schleifensteuerung
# Lücke 1: Initialisiere eine Ganzzahl-Variable 'zaehler' mit dem Wert 1
zaehler = 1

# Teil 2: Definiere eine while-Schleife, die so lange läuft, wie die Bedingung erfüllt ist
while zaehler <= 5:  # Lücke 2: Setze die Bedingung ein, die überprüft wird (z.B., zaehler <= 5)
    if zaehler % 2 == 0:  # Lücke 3: Überprüfe innerhalb der Schleife, ob 'zaehler' gerade ist
        print(f"Zählerwert {zaehler} ist gerade")
    # Lücke 4: Erhöhe den Wert von 'zaehler' um 1
    zaehler += 1

# Teil 3: Gib eine Abschlussmeldung nach Beendigung der Schleife aus
print("Schleife beendet.")
