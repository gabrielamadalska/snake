import pygame
import sys

pygame.init()

# stałe
WIDTH, HEIGHT = 800, 600

def game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    # głowna petla gry
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #dodanie poruszania się elif


    pygame.quit()
    sys.exit()

# sprawdzanie, czy skrypt jest uruchamiany jako program główny
if __name__ == "__main__":
    game()