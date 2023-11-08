"""



"""

import sys
sys.path.insert(1, '../config/')
from settings import *
from util import *
import pygame
import random
import math

random.seed(SEED)

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

pygame.display.set_caption('Game of Survival')


basicFont = pygame.font.SysFont(None, 30)
# can change 'None' to path to .ttf file
text_surface = basicFont.render('whatever', True, WHITE)

# pygame.draw.line(surface, colour, (x, y), (x, y))
# vem_surface = pygame.image.load('path/to/file.png').convert_alpha()


""" ----------------------------------------- Variables ----------------------------------------- """

board_radius = 50
board_size = calc_num_tiles(board_radius)
tileSize = ((math.sqrt(3) * ((height - 50) / math.sqrt(3))) / (board_radius * 3 - 1))
board = [(index_to_coords(i), random.randint(0,3)) for i in range(board_size)]
print(f"Radius: {board_radius} Tiles: {board_size}")


""" ----------------------------------------- Custom Funtions ----------------------------------------- """

# draw a hexagon
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

# draw the entire board
def draw_board():
    vert = (3 / 2) * tileSize
    horiz = math.sqrt(3) * tileSize
    for i in range(board_size):
        match board[i][1]:
            case 0: # dead
                draw_hexagon(screen, (width / 2) + (horiz * board[i][0][0]) + (horiz * board[i][0][1] / 2), (height / 2) + (vert * board[i][0][1]), tileSize, True, GREY)
            case 1: # alive
                draw_hexagon(screen, (width / 2) + (horiz * board[i][0][0]) + (horiz * board[i][0][1] / 2), (height / 2) + (vert * board[i][0][1]), tileSize, True, WHITE)
            case 2: # fungi
                draw_hexagon(screen, (width / 2) + (horiz * board[i][0][0]) + (horiz * board[i][0][1] / 2), (height / 2) + (vert * board[i][0][1]), tileSize, True, YELLOW)
            case 3: # virus
                draw_hexagon(screen, (width / 2) + (horiz * board[i][0][0]) + (horiz * board[i][0][1] / 2), (height / 2) + (vert * board[i][0][1]), tileSize, True, GREEN)


""" ----------------------------------------- Main Loop ----------------------------------------- """

frames_clock = pygame.time.Clock()
while True:

    # stops the loop, for testing funtions quickly

    #inputs:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # if event.type == pygame.KEYUP:
        #if event.type == pygame.MOUSEBUTTONUP:
    

    # draw everything:
    
    screen.fill(BLACK)
    draw_board()
    # screen.blit(text_surface, (0,0))
    # screen.blit(surface, (x,y))
    
    pygame.display.update()
    frames_clock.tick(60)

