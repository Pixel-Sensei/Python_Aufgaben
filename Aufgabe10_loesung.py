"""
Aufgabe: Verarbeitung einer Liste von Personen (Tupeln)

Vervollständige den folgenden Python-Code, der eine Liste von Personen (repräsentiert durch Tupel von Name und Alter) einliest,
verschiedene Operationen auf dieser Liste durchführt und die Ergebnisse ausgibt.
Teile den Code in drei Teile: das Einlesen der Personen, das Durchführen der Operationen
und das Ausgeben der Ergebnisse.
"""

# Teil 1: Einlesen der Personen
def einlesen_personen():
    personen = []
    anzahl = int(input("Gib die Anzahl der Personen ein: "))
    for i in range(anzahl):
        name = input(f"Gib den Namen der Person {i + 1} ein: ")
        alter = int(input(f"Gib das Alter der Person {name} ein: "))
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
    personen = einlesen_personen()
    durchschnittsalter, aelteste_person, juengste_person = verarbeite_personen(personen)
    ausgabe(durchschnittsalter, aelteste_person, juengste_person)

# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
