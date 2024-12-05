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
        return Vector2(x, y)

# Create the Snake class
class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)  # Initially moving to the right

    def draw(self):
        for segment in self.body:
            segment_rect = pygame.Rect(
                segment.x * cell_size, 
                segment.y * cell_size, 
                cell_size, 
                cell_size
            )
            pygame.draw.rect(screen, DARK_GREEN, segment_rect, border_radius=5)

    def move(self):
        # Add a new head based on the direction and remove the tail
        new_head = self.body[0] + self.direction
        self.body = [new_head] + self.body[:-1]

# Set up the screen
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))
pygame.display.set_caption("Snake Game")

# Game clock
clock = pygame.time.Clock()

# Create game objects
food = Food()
snake = Snake()

# Timer for snake movement
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SNAKE_UPDATE:
            snake.move()
        # Control snake direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: 
                snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN: 
                snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT: 
                snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)

    # Drawing the screen
    screen.fill(GREEN)  # Background color
    food.draw()
    snake.draw()

    # Refresh the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)