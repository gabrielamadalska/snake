import pygame
import sys

pygame.init()

# stałe
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, WHITE, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))   
    
    


def game():
    # ustawienie okna
    screen = pygame.display.set_mode((WIDTH, HEIGHT), )
    screen.fill(BLACK)
    pygame.display.update()
    pygame.display.set_caption("Snake")

    # głowna petla gry
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #dodanie poruszania się elif

        snake = Snake()
        pygame.display.flip()
        snake.draw(screen)
        #food.draw(screen)
        #clock.tick(FPS)


    pygame.quit()
    sys.exit()

# sprawdzanie, czy skrypt jest uruchamiany jako program główny
if __name__ == "__main__":
    game()