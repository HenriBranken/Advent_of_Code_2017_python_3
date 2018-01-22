# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 3: Spiral Memory, Part 1                                                        |
# | Website: https://adventofcode.com/2017/day/3                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

import math
import numpy as np

value = 368078  # The puzzle input.

# Approximate for the size of the square array to be roughly equal to the sqrt of the puzzle input
dimension = int(math.ceil(math.sqrt(value)))

# give new (dy, dx) of new direction based on the given (key) direction
count_clock = {"E": (-1, 0), "N": (0, -1), "W": (1, 0), "S": (0, 1)}


# identify the direction based on the supplied del_y and del_x values
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

x = y = dimension // 2  # start populating the array from the middle of the array

i = 1

matrix[y, x] = i  # initialise the center of the matrix  (row, column)
current_stride = 1
current_dir = (0, 1)  # East

while (y < dimension) and (x < dimension):
    # complete the first stride
    for _ in range(current_stride):
        dy, dx = current_dir
        y = y + dy
        x = x + dx
        i += 1
        matrix[y, x] = i
    # turn counterclockwise
    my_dir = identify_dir(dy, dx)
    current_dir = count_clock[my_dir]
    # complete the second stride
    for _ in range(current_stride):
        dy, dx = current_dir
        y = y + dy
        x = x + dx
        i += 1
        matrix[y, x] = i
    # increment the stride and turn counterclockwise (get new direction)
    current_stride += 1
    my_dir = identify_dir(dy, dx)
    current_dir = count_clock[my_dir]

one_y, one_x = np.where(matrix == 1)  # the y and x coordinates of where 1 lives (where we started out)
one_y, one_x = one_x[0], one_y[0]

value_y, value_x = np.where(matrix == value)  # the y and x coordinates of where value lives
value_y, value_x = value_y[0], value_x[0]

# The number of steps is simply equal to the overall del_y + del_x
steps = abs(value_y - one_y) + abs(value_x - one_x)
print(str(steps) + " steps are required.")
# Answer is 371.
