




# colours
BLACK = (30, 30, 35)
WHITE = (219, 219, 219)
GREY = (107, 107, 107)

RED = (146, 20, 12)
ORANGE = (200, 100, 0)
YELLOW = (255, 255, 0)
GREEN = (68, 175, 105)
TEAL = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (55, 34, 72)
BROWN = (150, 100, 50)

# BASIC_CELL = 
# VOID_CELL = 
# GRID = 

# Uses recursion to calculate the number of tiles for a given radius, f(x) = 6 * (x - 1) + f(x - 1)
def calc_num_tiles(radius):
    if radius == 1:
        return 1
    else:
        return 6 * (radius - 1) + calc_num_tiles(radius - 1)