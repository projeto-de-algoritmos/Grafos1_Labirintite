import random
import pygame
from Constantes import size, cols, rows, width, GREY
from Cell import Cell, removeWalls
import maze_generator as mg

pygame.init()

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Maze Generator")

done = False

clock = pygame.time.Clock()

grid, goal = mg.generate()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    for y in range(rows):
        for x in range(cols):
            grid[y][x].draw(screen)

    grid[goal[1]][goal[0]].draw_food(screen)
    
    pygame.display.flip()

pygame.quit()