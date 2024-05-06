'''''
    The code implements a simple Snake game using Pygame library in Python, where the player controls a
    snake to eat food and grow while avoiding walls.
    
    :param screen: The `screen` parameter represents the surface on which everything is drawn in the
    game. It is the main window or display area where all the game elements such as the snake, food, and
    score are rendered
    :param score: The `score` parameter in the code represents the player's score in the Snake game. It
    is incremented by 1 each time the snake eats the food (red square) on the screen. The score is
    displayed on the top left corner of the game window and keeps track of how many times the
'''''   

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

class Food:
    def __init__(self):
        self.position = self.food_position()

    def food_position(self):
        x = (random.randint(0, WIDTH // CELL_SIZE - 1)) * CELL_SIZE
        y = (random.randint(0, HEIGHT // CELL_SIZE - 1)) * CELL_SIZE

        return (x, y)
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

def game():
    # ustawienie okna
    pygame.init()
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock() #w module Pygame to obiekt, który służy do kontroli szybkości klatek (FPS - frames per second) w grze.

    # utworzenie obiektu klasy Snake
    snake = Snake()

    # utworzenie obiektu klasy Food
    food = Food()

    # głowna petla gry
    running = True
    
    score = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: # po naciśnieciu klawisza wchodzi w pętlę
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
        if snake.body[0] == food.position:
            food.position = food.food_position()
            score += 1

        # zamknięcie gry z powodu wjechania w ścianę 
        if not (0 <= snake.body[0][0] < WIDTH and 0 <= snake.body[0][1] < HEIGHT):
                running = False


        screen.fill(BLACK)  # wypełnienie ekranu kolorem
        snake.draw(screen)  # rysowanie snake na ekranie 
        food.draw(screen)   # rysowanie jedzenia
        draw_score(screen, score)   # wyswietlanie wyniku
        pygame.display.flip()
        clock.tick(FPS) # odświezacnie co 10 sek
     
    pygame.quit()
    sys.exit()

# sprawdzanie, czy skrypt jest uruchamiany jako program główny
if __name__ == "__main__":
    game()