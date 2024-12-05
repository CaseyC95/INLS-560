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
    def __init__(self, snake_body):
        self.position = self.generate_random_pos(snake_body)
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

    def generate_random_pos(self, snake_body):
        # Generate a position that is not on the snake's body
        while True:
            x = random.randint(0, number_of_cells - 1)
            y = random.randint(0, number_of_cells - 1)
            position = Vector2(x, y)
            if position not in snake_body:
                return position

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
    
    def reset(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)

    def move(self):
        # Add a new head based on the direction and remove the tail
        new_head = self.body[0] + self.direction
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        # Grow the snake by adding a new segment at the end
        tail = self.body[-1]
        self.body.append(tail)

# Create the Game class
class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.score = 0
        self.state = "RUNNING"

    def update(self):
        if self.state == "RUNNING":
            self.snake.move()
            self.check_collision_with_food()
            self.check_collision_with_edges()

    def draw(self):
        self.snake.draw()
        self.food.draw()

        # Display the score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        if self.state == "STOPPED":
            # Display Game Over message
            font = pygame.font.Font(None, 72)
            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2 - 50))

            # Display option to quit
            font = pygame.font.Font(None, 36)
            restart_text = font.render("Press Q to Quit or R to Restart", True, (255, 255, 255))
            screen.blit(restart_text, (screen.get_width() // 2 - restart_text.get_width() // 2, screen.get_height() // 2 + 50))

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food = Food(self.snake.body)  # Pass the updated snake body
            self.score += 1
    
    def check_collision_with_edges(self):
        if self.snake.body[0].x == number_of_cells or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == number_of_cells or self.snake.body[0].y == -1:
            self.game_over()

    def game_over(self):
        self.snake.reset()
        self.food.position = self.food.generate_random_pos(self.snake.body)
        self.state = "STOPPED"
        print("Game Over")

# Set up the screen
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))
pygame.display.set_caption("Snake Game")

# Game clock
clock = pygame.time.Clock()

# Create game objects
game = Game()

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
        if event.type == SNAKE_UPDATE and game.state == "RUNNING":
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.snake.direction != Vector2(0, 1):
                game.snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN and game.snake.direction != Vector2(0, -1):
                game.snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1, 0)
            # Restart or quit game
            elif event.key == pygame.K_r and game.state == "STOPPED":
                game = Game()  # Create a new game instance to restart
            elif event.key == pygame.K_q and game.state == "STOPPED":
                pygame.quit()
                sys.exit()

    # Drawing the screen
    screen.fill(GREEN)  # Background color
    game.draw()

    # Refresh the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)