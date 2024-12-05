import pygame
import sys
import random
from pygame.math import Vector2

# Initialize Pygame
pygame.init()

# Colors
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

# Settings
cell_size = 30
number_of_cells = 25

# Create the Food class
class Food:
    def __init__(self):
        self.position = self.generate_random_pos()
        self.food_surface = pygame.Surface((cell_size, cell_size))
        self.food_surface.fill((200, 0, 0))  # Red food color

    def draw(self):
        food_rect = pygame.Rect(
            self.position.x * cell_size, 
            self.position.y * cell_size, 
            cell_size, 
            cell_size
        )
        screen.blit(self.food_surface, food_rect)

    def generate_random_pos(self):
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)
        position = Vector2(x, y)
        return position

# Set up the screen
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))
pygame.display.set_caption("Snake Game")

# Game clock
clock = pygame.time.Clock()

# Create an instance of Food
food = Food()

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Drawing the screen
    screen.fill(GREEN)  # Background color
    food.draw()

    # Refresh the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)