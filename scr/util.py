





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

SEED = 4

# Uses recursion to calculate the number of tiles for a given radius, f(x) = 6 * (x - 1) + f(x - 1)
def calc_num_tiles(radius):
    if radius == 1:
        return 1
    else:
        return 6 * (radius - 1) + calc_num_tiles(radius - 1)

# Maps the coords of any given tile to it's index
def map_to_index(j, k):
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
            else:
                return -1
    return i

