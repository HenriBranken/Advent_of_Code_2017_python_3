# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 3: Spiral Memory, Part 2                                                        |
# | Website: https://adventofcode.com/2017/day/3                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

import math
import numpy as np


# in this function, we check all adjacent cells, including diagonals, to determine the value of the current cell,
# which is simply te sum of all the adjacent cells.
def check_adjacent_cells(y_pos, x_pos):
    global matrix
    # check left
    if (x_pos - 1) >= 0:
        left = matrix[y_pos, x_pos - 1]
    else:
        left = 0
    # check right
    if (x_pos + 1) < dimension:
        right = matrix[y_pos, x_pos + 1]
    else:
        right = 0
    # check up
    if (y_pos - 1) >= 0:
        up = matrix[y_pos - 1, x_pos]
    else:
        up = 0
    # check down
    if (y_pos + 1) < dimension:
        down = matrix[y_pos + 1, x_pos]
    else:
        down = 0
    # check top_left
    if (x_pos - 1) >= 0 and (y_pos - 1) >= 0:
        top_left = matrix[y_pos - 1, x_pos - 1]
    else:
        top_left = 0
    # check top_right
    if (x_pos + 1) < dimension and (y_pos - 1) >= 0:
        top_right = matrix[y_pos - 1, x_pos + 1]
    else:
        top_right = 0
    # check bottom_left
    if (x_pos - 1) >= 0 and (y_pos + 1) < dimension:
        bottom_left = matrix[y_pos + 1, x_pos - 1]
    else:
        bottom_left = 0
    # check bottom_right
    if (x_pos + 1) < dimension and (y_pos + 1) < dimension:
        bottom_right = matrix[y_pos + 1, x_pos + 1]
    else:
        bottom_right = 0
    return left + right + up + down + top_left + top_right + bottom_left + bottom_right


value = 368078  # Your puzzle input.

# Approximate for the size of the square array to be roughly equal to the sqrt of the puzzle input.
dimension = int(math.ceil(math.sqrt(value)))

# give new (dy, dx) of new direction based on the given (key) direction
count_clock = {"E": (-1, 0), "N": (0, -1), "W": (1, 0), "S": (0, 1)}


# identify the direction based on the data supplied by del_y and del_x
def identify_dir(del_y, del_x):
    if (del_y == 0) and (del_x == 1):
        return "E"
    elif (del_y == -1) and (del_x == 0):
        return "N"
    elif (del_y == 0) and (del_x == -1):
        return "W"
    else:
        return "S"


matrix = np.zeros((dimension + 1, dimension + 1), dtype=int)

# start out in the approximate middle of the array
x = y = dimension // 2  # start in the middle

i = 1

matrix[y, x] = i  # initialise the center of the matrix  (row, column)
current_stride = 1
current_dir = (0, 1)  # east
flag = 0

# When we add a value to the square array that is larger than <value>, we break the while-loop, and output that value.
while True:
    # complete the first stride
    for _ in range(current_stride):
        dy, dx = current_dir
        y = y + dy
        x = x + dx
        i += 1
        matrix[y, x] = check_adjacent_cells(y, x)
        if matrix[y, x] > value:
            flag = 1
            break
    if flag:
        break
    # turn counterclockwise:
    my_dir = identify_dir(dy, dx)
    current_dir = count_clock[my_dir]

    # complete the second stride
    for _ in range(current_stride):
        dy, dx = current_dir
        y = y + dy
        x = x + dx
        i += 1
        matrix[y, x] = check_adjacent_cells(y, x)
        if matrix[y, x] > value:
            flag = 1
            break
    if flag:
        break
    # increment the stride and turn counterclockwise
    current_stride += 1
    my_dir = identify_dir(dy, dx)
    current_dir = count_clock[my_dir]

# At this stage, matrix[y, x] simply represents the first value written that is larger than <value>.
print(str(matrix[y, x]) + " is the first value written that is larger than " + str(value) + ".")
# Answer is 369601.
