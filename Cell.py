import random
import pygame
from Constantes import size, cols, rows, width

WHITE = (255,255,255)
GREY = (20,20,20)
LIGHT_GREY = (200,200,200)
LIGHT_PINK = (219, 144, 235)
BLACK = (0,0,0)
PURPLE = (100,0,100)
CIAN = (0, 255, 255)
RED = (255,0,0)
GREEN = (0, 255, 0)

wall_size = 3
class Cell():
    def __init__(self,x,y):
        global width
        self.x = x * width
        self.y = y * width
        
        self.created = False
        self.current = False
        self.goal = False
        self.visited = False
        self.path = False
        self.queued = False
        self.caller = None

        self.walls = [True,True,True,True] # top , right , bottom , left
        
        # neighbors
        self.neighbors = []
        
        self.top =  0
        self.right = 0
        self.bottom = 0
        self.left = 0
        
        self.next_cell = 0
    
    def draw(self, screen):
        if self.current:
            pygame.draw.rect(screen, RED,(self.x,self.y,width,width))
        elif self.goal:
            pygame.draw.rect(screen,GREEN,(self.x,self.y,width,width))
        elif self.path:
            pygame.draw.rect(screen,CIAN,(self.x,self.y,width,width))
        elif self.visited:
            pygame.draw.rect(screen,LIGHT_GREY,(self.x,self.y,width,width))
        elif self.queued:
            pygame.draw.rect(screen,LIGHT_PINK,(self.x,self.y,width,width))
        elif self.created:
            pygame.draw.rect(screen,WHITE,(self.x,self.y,width,width))
        if self.created == True:
            if self.walls[0]:
                pygame.draw.line(screen,BLACK,(self.x,self.y),((self.x + width),self.y),wall_size)
            if self.walls[1]:
                pygame.draw.line(screen,BLACK,((self.x + width),self.y),((self.x + width),(self.y + width)),wall_size)
            if self.walls[2]:
                pygame.draw.line(screen,BLACK,((self.x + width),(self.y + width)),(self.x,(self.y + width)),wall_size)
            if self.walls[3]:
                pygame.draw.line(screen,BLACK,(self.x,(self.y + width)),(self.x,self.y),wall_size)

    def checkNeighbors(self, grid):
        if int(self.y / width) - 1 >= 0:
            self.top = grid[int(self.y / width) - 1][int(self.x / width)]
        if int(self.x / width) + 1 <= cols - 1:
            self.right = grid[int(self.y / width)][int(self.x / width) + 1]
        if int(self.y / width) + 1 <= rows - 1:
            self.bottom = grid[int(self.y / width) + 1][int(self.x / width)]
        if int(self.x / width) - 1 >= 0:
            self.left = grid[int(self.y / width)][int(self.x / width) - 1]
        
        if self.top != 0:
            if self.top.created == False:
                self.neighbors.append(self.top)
        if self.right != 0:
            if self.right.created == False:
                self.neighbors.append(self.right)
        if self.bottom != 0:
            if self.bottom.created == False:
                self.neighbors.append(self.bottom)
        if self.left != 0:
            if self.left.created == False:
                self.neighbors.append(self.left)
        
        if len(self.neighbors) > 0:
            self.next_cell = self.neighbors[random.randrange(0,len(self.neighbors))]
            return self.next_cell
        else:
            return False

    def getNextCell(self):
        available = []
        if self.top != 0 and self.top.visited == False and not self.walls[0]:
            available.append(self.top)
        if self.right != 0 and self.right.visited == False and not self.walls[1]:
            available.append(self.right)
        if self.bottom != 0 and self.bottom.visited == False and not self.walls[2]:
            available.append(self.bottom)
        if self.left != 0 and self.left.visited == False and not self.walls[3]:
            available.append(self.left)
        return available


def removeWalls(current_cell,next_cell):
    x = int(current_cell.x / width) - int(next_cell.x / width)
    y = int(current_cell.y / width) - int(next_cell.y / width)
    if x == -1: # right of current
        current_cell.walls[1] = False
        next_cell.walls[3] = False
    elif x == 1: # left of current
        current_cell.walls[3] = False
        next_cell.walls[1] = False
    elif y == -1: # bottom of current
        current_cell.walls[2] = False
        next_cell.walls[0] = False
    elif y == 1: # top of current
        current_cell.walls[0] = False
        next_cell.walls[2] = False