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


basicFont = pygame.font.SysFont(None, 20)
# can change 'None' to path to .ttf file
text_surface = basicFont.render('whatever', True, WHITE)

# pygame.draw.line(surface, colour, (x, y), (x, y))
# vem_surface = pygame.image.load('path/to/file.png').convert_alpha()


""" ----------------------------------------- Variables ----------------------------------------- """

board_radius = 10
board_size = calc_num_tiles(board_radius)
board = [{'coords' : index_to_coords(i), 'state' : random.randint(0,1)} for i in range(board_size)]
tileSize = ((math.sqrt(3) * ((min(height, width) - 60) / math.sqrt(3))) / (board_radius * 3 - 1))
print(f"Radius: {board_radius} Tiles: {board_size}")
scroll = 100
scroll_rate = 5
DIRECTIONS = ('topright', 'right', 'botright', 'botleft', 'left', 'topleft')


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
    pygame.draw.polygon(surface, hex_border_colour, points, 2)
    text_surface = basicFont.render(str(jkl), True, PURPLE)
    #surface.blit(text_surface, (x - int((text_surface.get_width() / 2)), y - int((text_surface.get_height() / 2))))

# draw the entire board
def draw_board():
    vert = (3 / 2) * tileSize
    horiz = math.sqrt(3) * tileSize
    for i in range(board_size):
        x = (width / 2) + (horiz * board[i]['coords'][0]) + (horiz * board[i]['coords'][1] / 2)
        y = (height / 2) + (vert * board[i]['coords'][1])
        jkl = (board[i]['coords'][0], board[i]['coords'][1], board[i]['coords'][2])
        match board[i]['state']:
            case 0: # dead
                draw_hexagon(screen, x, y, tileSize, True, dead_cell_colour, jkl)
            case 1: # alive
                draw_hexagon(screen, x, y, tileSize, True, live_cell_colour, jkl)
            case 2: # fungi
                draw_hexagon(screen, x, y, tileSize, True, YELLOW, jkl)
            case 3: # virus
                draw_hexagon(screen, x, y, tileSize, True, GREEN, jkl)


def check_neighbours(coords):
    i = 0





""" ----------------------------------------- Main Loop ----------------------------------------- """

frames_clock = pygame.time.Clock()
while True:

    # stops the loop, for testing funtions quickly

    #inputs:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                pygame.quit()
                sys.exit()

            case pygame.VIDEORESIZE:
                width, height = event.w, event.h
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                tileSize = ((math.sqrt(3) * ((min(height, width) - 60) / math.sqrt(3))) / (board_radius * 3 - 1))

            case pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            case pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    print(pygame.mouse.get_pos())
                    mouse_pos = pygame.mouse.get_pos()
                    vemjk = pixel_to_jk_pointy(mouse_pos[0] - width / 2, mouse_pos[1] - height /2, tileSize)
                    print(vemjk)
                    vemindex = coords_to_index(vemjk[0], vemjk[1])

            case pygame.MOUSEWHEEL:
                print(scroll)
                if event.y == 1: #scroll up/in
                    scroll += scroll_rate
                elif event.y == -1: #scroll down/out 
                    scroll -= scroll_rate
                tileSize = ((math.sqrt(3) * ((min(height, width) - 60) / math.sqrt(3))) / (board_radius * 3 - 1)) * (scroll / 100)

            case pygame.KEYUP:
                if event.key == pygame.K_r:
                    board = [{'coords' : index_to_coords(i), 'state' : random.randint(0,1)} for i in range(board_size)]
                if event.key == pygame.K_i:
                    for hex in board:
                        alive_neighbours = 0

                        for direction in DIRECTIONS:
                            neighbour_i = return_neighbour(hex, direction)
                            if neighbour_i  < board_size:
                                if board[neighbour_i]['state'] == 1:
                                    alive_neighbours += 1

                        if alive_neighbours == 3 or  alive_neighbours == 2 and hex['state'] == 1:
                        #if alive_neighbours == 2:
                            hex["next_state"] = 1

                        else:
                            hex["next_state"] = 0

                    #important that it uopdates board all in one go not as it goes
                    for hex in board:
                        hex['state'] = hex['next_state']



    # draw everything:
    screen.fill(BLACK)
    draw_board()
    #for i in range(board_size):
    #    board[i] = ((board[i][0]), random.randint(0,3))
    # screen.blit(text_surface, (0,0))
    # screen.blit(surface, (x,y))
    
    pygame.display.update()
    frames_clock.tick(60)



