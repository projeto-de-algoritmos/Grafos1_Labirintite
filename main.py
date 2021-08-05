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
stack = []

grid = mg.generate()
finded = False
current_cell = grid[0][0]
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    current_cell.current = True
    current_cell.visited = True

    for y in range(rows):
        for x in range(cols):
            grid[y][x].draw(screen)

    next_cells = current_cell.getNextCell()

    if finded and len(stack):
        current_cell.path = True
        current_cell.current = False
        current_cell = stack.pop()
    elif len(next_cells) > 0:
        current_cell.neighbors = []
        
        stack.append(current_cell)
        
        current_cell.current = False
        
        current_cell = next_cells[0]
        if(next_cells[0].goal == True):
            finded = True
    elif len(stack) > 0:
        current_cell.current = False
        current_cell = stack.pop()

    clock.tick(100)
    pygame.display.flip()
    a = input()

pygame.quit()