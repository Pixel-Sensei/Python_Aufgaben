"""
Aufgabe: Umwandlung von Celsius in Fahrenheit

Vervollständige den folgenden Python-Code, der eine Liste von Temperaturen in Celsius in Fahrenheit umwandelt.
Teile den Code in drei Teile: das Einlesen der Celsius-Temperaturen, das Umwandeln der Temperaturen in Fahrenheit,
und das Ausgeben der Ergebnisse.
"""

# Teil 1: Einlesen der Celsius-Temperaturen
def lese_temperaturen():
    temperaturen = []
    anzahl = int(input("Wie viele Temperaturen möchtest du eingeben? "))
    for _ in range(__________):
        temp = float(input("Gib eine Temperatur in Celsius ein: "))
        temperaturen.append(__________)
    return temperaturen

# Teil 2: Umwandeln der Temperaturen in Fahrenheit
def umwandeln_in_fahrenheit(temperaturen):
    fahrenheit = []
    for temp in temperaturen:
        f_temp = temp * 9/5 + __________
        fahrenheit.append(__________)
    return fahrenheit

# Teil 3: Ausgabe der Ergebnisse
def ausgabe(temperaturen, fahrenheit):
    for c, f in zip(temperaturen, fahrenheit):
        print(f"{c}°C = {__________}°F")

# Hauptprogramm
def main():
    temperaturen = lese_temperaturen()
    fahrenheit = umwandeln_in_fahrenheit(__________)
    ausgabe(temperaturen, fahrenheit)

# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
