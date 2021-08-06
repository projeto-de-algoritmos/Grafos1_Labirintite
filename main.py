import random
import pygame
import queue
from Constantes import size, cols, rows, width, GREY
import Theme
import maze_generator as mg
from Cell import Cell, removeWalls, reload_colors
from importlib import reload

opt = 0
while opt > 2 or opt < 1:
    opt = int(input("1- DFS \n2- BFS\n"))
    if opt == 3:
        new_theme = Theme.next_theme()
        reload_colors()
        print("\nTema definido para:", new_theme)



pygame.init()

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Maze Generator")

done = False

clock = pygame.time.Clock()
stack = []
queue = queue.Queue()

grid = mg.generate()
grid[0][0].caller = grid[0][0]

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
    if(current_cell.goal == True):
        finded = True

    for y in range(rows):
        for x in range(cols):
            grid[y][x].draw(screen)

    next_cells = current_cell.getNextCell()

    if opt == 1:
        if finded and len(stack):
            current_cell.path = True
            current_cell.current = False
            current_cell = stack.pop()
        elif len(next_cells) > 0:
            current_cell.neighbors = []
            
            stack.append(current_cell)
            
            current_cell.current = False
            
            current_cell = next_cells[0]
        elif len(stack) > 0:
            current_cell.current = False
            current_cell = stack.pop()
    elif opt == 2:
        for cell in next_cells:
            cell.queued = True
            cell.caller = current_cell
            queue.put(cell)

        if finded:
            current_cell.path = True
            current_cell.current = False
            current_cell = current_cell.caller
        elif queue.qsize() > 0:
            current_cell.current = False
            current_cell = queue.get()

    clock.tick(100)
    pygame.display.flip()
    a = input()

pygame.quit()