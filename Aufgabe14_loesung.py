import pygame
import sys

"""
Aufgabe: Einfache Animation mit Pygame

Vervollständige den folgenden Python-Code mit den richtigen Befehlen aus dem Pygame-Modul.
Die Aufgabe umfasst das Erstellen eines Fensters, das Zeichnen von Formen, das Durchführen
einer Animation und das Behandeln von Ereignissen.
"""

# Teil 1: Initialisierung von Pygame und Erstellung des Fensters
pygame.init()
window = pygame.display.set_mode((400, 300))  # Lücke 1: Fenstergrösse

# Teil 2: Definieren von Farben
schwarz = (0, 0, 0)
weiss = (255, 255, 255)
rot = (255, 0, 0)


# Teil 3: Schleife für die Animation
def animation():
    x = 50
    y = 50
    geschwindigkeit = 5
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(weiss)  # Lücke 2: Hintergrundfarbe des Fensters

        pygame.draw.rect(window, rot, (x, y, 50, 50))  # Lücke 3: Zeichnen eines roten Rechtecks

        pygame.display.update()
        clock.tick(30)

        x += geschwindigkeit
        if x > 350:  # Lücke 4: Bedingung für die Animation
            x = 50


# Teil 4: Hauptprogramm
def main():
    animation()


# Aufruf des Hauptprogramms
if __name__ == "__main__":
    main()
