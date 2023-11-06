import pygame
from sys import exit

pygame.init()

#window setup:
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Template')

basicFont = pygame.font.SysFont(None, 30)
#can change 'None' to path to .ttf file
#text_surface = basicfont.render('whatever', True, WHITE)

#Colours:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (200, 100, 0)
BROWN = (150, 100, 50)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
TEAL = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)

#pygame.draw.line(surface, colour, (x, y), (x, y))
#vem_surface = pygame.image.load('path/to/file.png').convert_alpha()

#main loop:
frames_clock = pygame.time.Clock()
while True:
    #inputs:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.KEYDOWN:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        #if event.type == pygame.MOUSEBUTTONUP:
    
    #draw everything:
    screen.fill(BLACK)
    #screen.blit(surface, (x,y))
    
    pygame.display.update()
    frames_clock.tick(60)
