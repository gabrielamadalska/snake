import pygame
import sys
import random

# stałe
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 10

# kolory
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)] # warunkuje polozenie na srodku okna
        self.direction = random.choice([(CELL_SIZE, 0),(-CELL_SIZE, 0),(0, CELL_SIZE),(0, -CELL_SIZE)])
    
    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body = [new_head] + self.body[:-1]  

    def draw(self, screen):
        # Rysuj głowę węża (pierwszy segment)
        for segment in self.body:
            
            pygame.draw.rect(screen, WHITE, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            #pygame.draw.rect(screen, WHITE, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def game():
    # ustawienie okna
    pygame.init()
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock() #w module Pygame to obiekt, który służy do kontroli szybkości klatek (FPS - frames per second) w grze.

    # utworzenie obiektu klasy Snake
    snake = Snake()
    
    # głowna petla gry
    running = True
 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, CELL_SIZE):
                    snake.direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -CELL_SIZE): # jesli on nie idzie w dół zmien jego keirunek na DOŁ
                    snake.direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and snake.direction != (CELL_SIZE, 0):
                    snake.direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-CELL_SIZE, 0):
                    snake.direction = (CELL_SIZE, 0)



        # przesuniecie weza o komórke 
        snake.move()

        # zamknięcie gry z powodu wjechania w ścianę 
        if not (0 <= snake.body[0][0] < WIDTH and 0 <= snake.body[0][1] < HEIGHT):
                running = False

        # if snake.body < WIDTH:
        #     running = False


        screen.fill(BLACK)
        # rysowanie snake na ekranie
        snake.draw(screen) 

        pygame.display.flip()
        
        # odświezacnie co 10 sek
        clock.tick(FPS)
     
    pygame.quit()
    sys.exit()

# sprawdzanie, czy skrypt jest uruchamiany jako program główny
if __name__ == "__main__":
    game()