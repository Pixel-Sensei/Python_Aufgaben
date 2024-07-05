import pygame
import sys

"""
Aufgabe: Interaktives Pygame-Spiel mit zusätzlichen Bewegungen

Vervollständige den folgenden Python-Code mit den richtigen Befehlen aus dem Pygame-Modul.
Die Aufgabe umfasst das Erstellen eines Fensters, das Zeichnen von Objekten, das Hinzufügen
von Bewegung in alle Richtungen und das Behandeln von Tastatureingaben.
"""

# Teil 1: Initialisierung von Pygame und Erstellung des Fensters
pygame.init()
window = pygame.display.set_mode((600, 400))  # Lücke 1: Fenstergrösse

# Teil 2: Definieren von Farben und Geschwindigkeit
schwarz = (0, 0, 0)  # Lücke 2: RGB-Farbwert für Schwarz
weiss = (255, 255, 255)  # Lücke 3: RGB-Farbwert für Weiss
grün = (0, 255, 0)  # Lücke 4: RGB-Farbwert für Grün
spieler_farbe = grün
spieler_breite = 50  # Lücke 5: Breite des Spieler-Rechtecks
spieler_hoehe = 50  # Lücke 6: Höhe des Spieler-Rechtecks
spieler_x = 50  # Lücke 7: Startposition X des Spielers
spieler_y = 150  # Lücke 8: Startposition Y des Spielers
spieler_geschwindigkeit = 5  # Lücke 9: Geschwindigkeit des Spielers

# Teil 3: Schleife für das Spiel
def spiel():
    global spieler_x, spieler_y  # Wir verwenden die globalen Variablen hier
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            spieler_y -= spieler_geschwindigkeit  # Lücke 10: Änderung der Y-Position beim Drücken von oben
        elif keys[pygame.K_DOWN]:
            spieler_y += spieler_geschwindigkeit  # Lücke 11: Änderung der Y-Position beim Drücken von unten
        elif keys[pygame.K_LEFT]:
            spieler_x -= spieler_geschwindigkeit  # Lücke 12: Änderung der X-Position beim Drücken von links
        elif keys[pygame.K_RIGHT]:
            spieler_x += spieler_geschwindigkeit  # Lücke 13: Änderung der X-Position beim Drücken von rechts

        window.fill(weiss)  # Lücke 14: Hintergrundfarbe des Fensters

        pygame.draw.rect(window, spieler_farbe, (spieler_x, spieler_y, spieler_breite, spieler_hoehe))  # Lücke 15: Zeichnen des Spielers

        pygame.display.update()
        clock.tick(30)  # Lücke 16: Framerate des Spiels


# Teil 4: Hauptprogramm
def main():
    spiel()


# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
