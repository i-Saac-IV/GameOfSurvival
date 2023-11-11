


#from main import *
import math

# colours
BLACK = (30, 30, 35)
WHITE = (219, 219, 219)
GREY = (89, 89, 89)

RED = (146, 20, 12)
ORANGE = (200, 100, 0)
YELLOW = (186, 170, 50)
GREEN = (68, 175, 105)
TEAL = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (55, 34, 72)
BROWN = (150, 100, 50)

dead_cell_colour = (80, 50, 20)
live_cell_colour = (70, 175, 70)
hex_border_colour = PURPLE
# BASIC_CELL = 
# VOID_CELL = 
# GRID = 

SEED = 6

# Calculate the number of tiles for a given radius
def calc_num_tiles(radius):
	return (1 + 3 * (radius - 1) * (radius))

# Maps the coords of any given tile to it's index
def coords_to_index(j, k):
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

# Maps the coords of any given tile to it's index
def index_to_coords(i):
    j = 0
    k = 0
    l = 0
    if i == 0: # the maths part doesn't cope well with all zeros
        # Do nothing
        j = j
    else:
        nthLoop = 0
        total = 0
        while True: # checking what ring the target's in
            nthLoop += 1
            total += 6 * nthLoop
            if total >= i:
                total -= 6 * i
                break
        radius = nthLoop
        currentKnownIndex = calc_num_tiles(nthLoop)
        if i == currentKnownIndex: # checks if "i" lies on the positive j axis
            j = radius
            k = 0
            l = -1 * radius
        else:
            nthLoop = 0
            total = 0
            while True: # checking what side the target's on
                nthLoop += 1
                total = currentKnownIndex + radius * nthLoop
                if total > i:
                    total -= radius * nthLoop
                    nthLoop -= 1
                    break
            currentKnownIndex = total + radius * nthLoop
            match nthLoop: # applying different maths depending on side
                case 0:
                    j = radius
                    k = -1 * (i - currentKnownIndex)
                    l = -j - k
                case 1:
                    k = -1 * radius
                    l = i - currentKnownIndex
                    j = -k - l
                case 2:
                    l = radius
                    j = -1 * (i - currentKnownIndex)
                    k = -j - l
                case 3:
                    j = -1 * radius
                    k = i - currentKnownIndex
                    l = -j - k
                case 4:
                    k = radius
                    l = -1 * (i - currentKnownIndex)
                    j = -k - l
                case 5:
                    l = -1 * radius
                    j = i - currentKnownIndex
                    k = -j - l
                case _:
                    return -1
    # return (j,k) # uncomment desired coord format
    return (j,k,l) # uncomment desired coord format


def pointy_hex_to_pixel(j, k, tile_size):
    x = tile_size * (math.sqrt(3) * j  +  math.sqrt(3)/2 * j)
    y = tile_size * (3/2 * j)
    return (x, y)

def pixel_to_jk_pointy(x, y, tile_size):
    j = (math.sqrt(3) / 3 * x - 1 /3 * y) / tile_size
    k = (2 / 3 * y) / tile_size
    return (round(j), round(k))

def xy_to_jkl(xy, w, h, ts):
	vert = (3 / 2) * ts
	horiz = math.sqrt(3) * ts
	k = (xy[1] - (h / 2)) / vert
	j = (xy[0] - (w / 2) - (horiz * k / 2) / horiz)
	l = -j - k
	return (int(j), int(k), int(l))

def return_neighbour(hex, direction):
    match direction:
        case 'topright':
            return coords_to_index(hex['coords'][0] + 1, hex['coords'][1] - 1)

        case 'right':
            return coords_to_index(hex['coords'][0] + 1, hex['coords'][1])

        case 'botright':
            return coords_to_index(hex['coords'][0], hex['coords'][1] + 1)

        case 'botleft':
            return coords_to_index(hex['coords'][0] - 1, hex['coords'][1] + 1)

        case 'left':
            return coords_to_index(hex['coords'][0] - 1, hex['coords'][1])

        case 'topleft':
            return coords_to_index(hex['coords'][0], hex['coords'][1] - 1)

        case _:
            print("improper direction used in 'return_neighbour' function")



#	x, y = xy[0], xy[1]
#	k = (y - (height / 2)) / vert
#	j = (x - (width / 2) - (horiz * k / 2) / horiz)
#	return coords_to_index(j, k)
	# y = (height / 2) + (vert * k)
	# x = (width / 2) + (horiz * j) + (horiz * k / 2)

	# k = (y - (h / 2)) / vert
	# j = (x - (w / 2) - (horiz * k / 2) / horiz)
