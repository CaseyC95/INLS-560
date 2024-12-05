import pygame
import sys
import random
from pygame.math import Vector2
import os

# Initialize Pygame
pygame.init()

# Colors
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

# Grid and Cell Configuration
cell_size = 30
number_of_cells = 25

# Ensure correct working directory
os.chdir(os.path.dirname(__file__))
print(f"Working directory: {os.getcwd()}")

# Verify the food image file exists
if not os.path.exists("graphics/food.png"):
    print("Error: File not found - graphics/food.png")
    print("Using a placeholder food instead.")
    food_surface = pygame.Surface((cell_size, cell_size))
    food_surface.fill(DARK_GREEN)
else:
    try:
        food_surface = pygame.image.load("graphics/food.png")
    except pygame.error as e:
        print(f"Error loading image: {e}")
        print("Using a placeholder instead.")
        food_surface = pygame.Surface((cell_size, cell_size))
        food_surface.fill(DARK_GREEN)

# Food Class
class Food:
    def __init__(self):
        self.position = self.generate_random_pos()

    def draw(self):
        food_rect = pygame.Rect(
            self.position.x * cell_size, 
            self.position.y * cell_size, 
            cell_size, 
            cell_size
        )
        screen.blit(food_surface, food_rect)

    def generate_random_pos(self):
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)
        return Vector2(x, y)

# Screen Setup
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))
pygame.display.set_caption("560 Snake Game")
clock = pygame.time.Clock()

# Initialize Food Object
food = Food()

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(GREEN)
    food.draw()

    pygame.display.update()
    clock.tick(60)