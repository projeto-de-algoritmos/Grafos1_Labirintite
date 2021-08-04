import random
import pygame
from Constantes import size, cols, rows, width, GREY
from Cell import Cell, removeWalls

def generate():

    pygame.init()

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Maze Generator")

    done = False

    clock = pygame.time.Clock()


    stack = []
    grid = []

    for y in range(rows):
        grid.append([])
        for x in range(cols):
            grid[y].append(Cell(x,y))

    current_cell = grid[0][0]
    next_cell = 0
    goal = [random.randrange(0, cols - 1), random.randrange(0, rows - 1)]
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        

        screen.fill(GREY)
        
        current_cell.visited = True
        current_cell.current = True
        
        for y in range(rows):
            for x in range(cols):
                grid[y][x].draw(screen)
        
        next_cell = current_cell.checkNeighbors(grid)
        
        if next_cell != False:
            current_cell.neighbors = []
            
            stack.append(current_cell)
            
            removeWalls(current_cell,next_cell)
            
            current_cell.current = False
            
            current_cell = next_cell
        
        elif len(stack) > 0:
            current_cell.current = False
            current_cell = stack.pop()
            
        elif len(stack) == 0:
            return (grid, goal)
        
        pygame.display.flip()

