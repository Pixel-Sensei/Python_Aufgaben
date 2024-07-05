import random

"""
Aufgabe: Verarbeitung einer Liste von zufälligen Personen

Vervollständige den folgenden Python-Code, der eine Liste von zufälligen Personen erstellt,
verschiedene Operationen auf dieser Liste durchführt und die Ergebnisse ausgibt.
Die Namen und Alter der Personen sollen zufällig generiert werden.
"""


# Teil 1: Erstellen der Liste von zufälligen Personen
def erstelle_zufaellige_personen(anzahl):
    namen = ["Alice", "Bob", "Charlie", "Diana", "Emma", "Frank", "Gina", "Hans", "Ingrid", "Jack"]
    personen = []
    for _ in range(anzahl):
        name = random.choice(namen)
        alter = random.randint(18, 70)
        person = (name, alter)
        personen.append(person)
    return personen


# Teil 2: Durchführen der Operationen
def verarbeite_personen(personen):
    summe = 0
    aelteste_person = ("", 0)
    juengste_person = ("", float('inf'))

    for person in personen:
        summe += person[1]
        if person[1] > aelteste_person[1]:
            aelteste_person = person
        if person[1] < juengste_person[1]:
            juengste_person = person

    durchschnittsalter = summe / len(personen)
    return durchschnittsalter, aelteste_person, juengste_person


# Teil 3: Ausgeben der Ergebnisse
def ausgabe(durchschnittsalter, aelteste_person, juengste_person):
    print(f"Durchschnittsalter der Personen: {durchschnittsalter:.2f}")
    print(f"Älteste Person: {aelteste_person[0]} ({aelteste_person[1]} Jahre)")
    print(f"Jüngste Person: {juengste_person[0]} ({juengste_person[1]} Jahre)")


# Hauptprogramm
def main():
    anzahl_personen = int(input("Gib die Anzahl der Personen ein: "))
    personen = erstelle_zufaellige_personen(anzahl_personen)
    durchschnittsalter, aelteste_person, juengste_person = verarbeite_personen(personen)
    ausgabe(durchschnittsalter, aelteste_person, juengste_person)


# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
