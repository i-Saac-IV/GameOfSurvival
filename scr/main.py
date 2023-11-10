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

width, height = 800, 800
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

pygame.display.set_caption('Game of Survival')


basicFont = pygame.font.SysFont(None, 15)
# can change 'None' to path to .ttf file
text_surface = basicFont.render('whatever', True, WHITE)

# pygame.draw.line(surface, colour, (x, y), (x, y))
# vem_surface = pygame.image.load('path/to/file.png').convert_alpha()


""" ----------------------------------------- Variables ----------------------------------------- """

board_radius = 5
board_size = calc_num_tiles(board_radius)
board = [[index_to_coords(i), random.randint(0,1)] for i in range(board_size)]
tileSize = ((math.sqrt(3) * ((min(height, width) - 60) / math.sqrt(3))) / (board_radius * 3 - 1))
print(f"Radius: {board_radius} Tiles: {board_size}")


""" ----------------------------------------- Custom Funtions ----------------------------------------- """

# draw a hexagon
def draw_hexagon(surface, x, y, radius, pointUp, colour, jkl):

    points = []
    for i in range(6):
        angle = i * (2 * math.pi / 6)
        if pointUp == True:
            angle -= (math.pi / 6)
        xi = x + radius * math.cos(angle)
        yi = y + radius * math.sin(angle)
        points.append((xi, yi))
    pygame.draw.polygon(surface, colour, points)
    pygame.draw.polygon(surface, PURPLE, points, 3)
    text_surface = basicFont.render(str(jkl), True, PURPLE)
    # surface.blit(text_surface, (x, y))

# draw the entire board
def draw_board():
    vert = (3 / 2) * tileSize
    horiz = math.sqrt(3) * tileSize
    for i in range(board_size):
        jkl = (board[i][0][0], board[i][0][1], board[i][0][2])
        match board[i][1]:
            case 0: # dead
                draw_hexagon(screen, (width / 2) + (horiz * board[i][0][0]) + (horiz * board[i][0][1] / 2), (height / 2) + (vert * board[i][0][1]), tileSize, True, GREY, jkl)
            case 1: # alive
                draw_hexagon(screen, (width / 2) + (horiz * board[i][0][0]) + (horiz * board[i][0][1] / 2), (height / 2) + (vert * board[i][0][1]), tileSize, True, WHITE, jkl)
            case 2: # fungi
                draw_hexagon(screen, (width / 2) + (horiz * board[i][0][0]) + (horiz * board[i][0][1] / 2), (height / 2) + (vert * board[i][0][1]), tileSize, True, YELLOW, jkl)
            case 3: # virus
                draw_hexagon(screen, (width / 2) + (horiz * board[i][0][0]) + (horiz * board[i][0][1] / 2), (height / 2) + (vert * board[i][0][1]), tileSize, True, GREEN, jkl)


def check_neighbours(coords):
    i = 0

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
            tileSize = ((math.sqrt(3) * ((min(height, width) - 60) / math.sqrt(3))) / (board_radius * 3 - 1))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print(pygame.mouse.get_pos())
                print(xy_to_jkl(pygame.mouse.get_pos(), width, height, tileSize))
                if board[0][1] == 0:
                    pass
                else:
                    pass
        # if event.type == pygame.KEYUP:
    
    # draw everything:
    screen.fill(BLACK)
    draw_board()
    #for i in range(board_size):
    #    board[i] = ((board[i][0]), random.randint(0,3))
    # screen.blit(text_surface, (0,0))
    # screen.blit(surface, (x,y))
    
    pygame.display.update()
    frames_clock.tick(60)

