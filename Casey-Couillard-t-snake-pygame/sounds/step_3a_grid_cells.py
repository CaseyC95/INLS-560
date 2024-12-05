import pygame, sys

pygame.init()

GREEN = (173,204,96)
DARK_GREEN = (43,51,24)

cell_size = 30 
number_of_cells = 25

screen = pygame.display.set_mode((cell_size * number_of_cells,cell_size * number_of_cells))

pygame.display.set_caption("560 Snake Game")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(GREEN)
    pygame.display.update()
    clock.tick(60)

