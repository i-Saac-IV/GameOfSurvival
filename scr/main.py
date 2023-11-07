"""







"""


import sys
sys.path.insert(1, '../config/')
from settings import *
from util import *
import pygame
import math

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game of Survival')



basicFont = pygame.font.SysFont(None, 30)
# can change 'None' to path to .ttf file
text_surface = basicFont.render('whatever', True, WHITE)

# pygame.draw.line(surface, colour, (x, y), (x, y))
# vem_surface = pygame.image.load('path/to/file.png').convert_alpha()


""" ----------------------------------------- Variables ----------------------------------------- """

board_radius = 100
board_size = calc_num_tiles(board_radius)
board = [(10, 20, 0) for _ in range(board_size)]
print(f"Radius: {board_radius} Tiles: {board_size}")


""" ----------------------------------------- Custom Funtions ----------------------------------------- """

# Define a function to draw a hexagon
def draw_hexagon(surface, x, y, radius, pointUp, colour):
    points = []
    for i in range(6):
        if pointUp == True:
            angle = i * (2 * math.pi / 6) - (math.pi / 6)
        else:
            angle = i * (2 * math.pi / 6)
        xi = x + radius * math.cos(angle)
        yi = y + radius * math.sin(angle)
        points.append((xi, yi))
    pygame.draw.polygon(surface, colour, points)


# Math funtion for changing the cell state, called as folowing: toggle_cell_state(*event.pos)
def toggle_cell_state(i, state):
    board[i] = (board[i][0], board[i][1], state)

def cell_map(j, k):
    if j == 0 and k == 0:
        i = 0
    else:
        l = -j - k
        abs_j = abs(j)
        abs_k = abs(k)
        abs_l = abs(l)
        ring = max(abs_j, abs_k, abs_l)

        i = calc_num_tiles(ring)
        if j * k * l == 0: # if this is true the tile lies on an axis
            if abs_j == abs_l: # 
                if j > l:
                    i += 0
                else:
                    i += ring * 3
            elif abs_k == abs_l:
                if k > l:
                    i += ring * 5
                else:
                    i += ring * 2
            elif abs_j == abs_k:
                if j > k:
                    i += ring
                else:
                    i += ring * 4
            else:
                return -1
        else: # if the tile is NOT on an axis
            if j == ring:
                i += abs_k
            elif k * -1 == ring:
                i += ring + l
            elif l == ring:\
                i += ring * 2 + abs_j
            elif j * -1 == ring:
                i += ring * 3 + k
            elif k == ring:
                i += ring * 4 + abs_l
            elif l * -1 == ring:
                i += ring * 5 + j
    return i

find_j = 0
find_k = 1

print(f"({find_j},{find_k}) --> {cell_map(find_j, find_k)}")

print(board[0])
toggle_cell_state(0, 16)
print(board[0])

""" Not my code...
# Function to update the grid and draw cells
def generate_board(radius):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col]:
                color = ALIVE_COLOR
            else:
                color = DEAD_COLOR
            pygame.draw.rect(screen, color, pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
"""

""" ----------------------------------------- Main Loop ----------------------------------------- """



frames_clock = pygame.time.Clock()
while True:

    break # stops the loop, for testing funtions quickly

    #inputs:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if event.type == pygame.KEYDOWN:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        #if event.type == pygame.MOUSEBUTTONUP:
    

    # draw everything:
    
    screen.fill(BLACK)
    draw_hexagon(screen, 400, 200, 200, False, WHITE)
    draw_hexagon(screen, 400, 200, 20, True, GREY)
    # screen.blit(text_surface, (0,0))
    # screen.blit(surface, (x,y))
    
    pygame.display.update()
    frames_clock.tick(60)
