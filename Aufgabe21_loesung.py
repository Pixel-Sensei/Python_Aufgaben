# Aufgabe: Größeres Dictionary verwenden

# Teil 1: Definiere ein Dictionary für einen Schüler
# Lücke 1: Definiere ein Dictionary namens 'schueler', das folgende Schlüssel-Wert-Paare enthält:
# - 'name': 'Max Mustermann'
# - 'alter': 18
# - 'klasse': '12A'
# - 'faecher': ['Mathematik', 'Physik', 'Chemie']
# - 'noten': {'Mathematik': 85, 'Physik': 78, 'Chemie': 92}
schueler = {
    'name': 'Max Mustermann',
    'alter': 18,
    'klasse': '12A',
    'faecher': ['Mathematik', 'Physik', 'Chemie'],
    'noten': {'Mathematik': 85, 'Physik': 78, 'Chemie': 92}
}

# Teil 2: Gib den Namen des Schülers aus dem Dictionary aus
# Lücke 2: Gib den Wert des Schlüssels 'name' aus dem Dictionary 'schueler' aus
print(schueler['name'])

# Teil 3: Füge ein neues Fach und eine Note zum Dictionary hinzu
# Lücke 3: Füge dem Dictionary 'schueler' ein neues Fach 'Informatik' mit der Note 90 hinzu
schueler['noten']['Informatik'] = 90

# Teil 4: Aktualisiere die Note in einem bestehenden Fach
# Lücke 4: Aktualisiere die Note für das Fach 'Physik' im Dictionary auf 82
schueler['noten']['Physik'] = 82

# Teil 5: Gib das gesamte Dictionary aus
# Lücke 5: Gib das gesamte Dictionary 'schueler' aus
print(schueler)
