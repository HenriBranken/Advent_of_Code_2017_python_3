# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 22:  Sporifica Virus, Part 1                                                    |
# | Website: https://adventofcode.com/2017/day/22                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

import numpy as np


# If the current node is clean, the virus turns to the left.
def turn_anticlockwise(input_direction):  # turning left if the current node is clean
    if input_direction == "S":
        return "E"
    elif input_direction == "E":
        return "N"
    elif input_direction == "N":
        return "W"
    else:
        return "S"


# if the current node is infected, the virus turns to the right.
def turn_clockwise(input_direction):  # turning right if the current node is infected
    if input_direction == "S":
        return "W"
    elif input_direction == "E":
        return "S"
    elif input_direction == "N":
        return "E"
    else:
        return "N"


def padding_array(input_array):
    n_rows, n_cols = input_array.shape

    pad_block_1 = np.chararray((n_rows, 1))
    pad_block_1[:] = "."
    array_1 = np.hstack((pad_block_1, input_array))

    pad_block_2 = np.chararray((1, 1 + n_cols))
    pad_block_2[:] = "."
    array_2 = np.vstack((pad_block_2, array_1, pad_block_2))

    pad_block_3 = np.chararray((n_rows + 2, 1))
    pad_block_3[:] = "."
    array_3 = np.hstack((array_2, pad_block_3))
    return array_3


# Of course, in real life, our computer is not able to hold an infinite grid.  Therefore, in order to solve the problem,
# we approximate our infinite array to be a square matrix that holds approximately 10**6 tiles.  This is an educated
# guess which aims at ensuring that our virus does not step beyond the boundaries of the square matrix.
# Furthermore, a square matrix of 10**6 tiles is populated by iteratively padding the central map with a blank border
# via the padding_array function.  In the padding_array function, the padded white space tiles are filled with the "."
# character, which represents a node that is clean.

f_name = "day_22_input.txt"  # Your puzzle input.

node_map = []
f = open(f_name, "r")
for line in f.readlines():
    if line in ["", " ", "\n"]:
        break
    line = list(line.rstrip("\n"))
    node_map.append(line)
f.close()

node_map = np.array(node_map)

#       key: value
# direction: (dy, dx)
directions = {"S": (1, 0), "N": (-1, 0), "E": (0, 1), "W": (0, -1)}

# iteratively pad an empty border around the central map (where the central map is the original puzzle input.)
k = 0
while True:
    node_map = padding_array(node_map)
    k += 1
    if node_map.size > 10**6:
        break

y_pos, x_pos = node_map.shape[0] // 2, node_map.shape[1] // 2  # start out at the very centre of the map.
direction = "N"  # We start out with the virus facing the North direction.
cause_infection = 0
n_bursts = 10000  # Part of your puzzle input.
for i in range(n_bursts):
    if node_map[y_pos, x_pos] == ".":  # the current node is clean.
        direction = turn_anticlockwise(direction)
        node_map[y_pos, x_pos] = "#"  # The current node becomes infected.
        cause_infection += 1
    else:  # else the current node is infected.
        direction = turn_clockwise(direction)
        node_map[y_pos, x_pos] = "."  # the current node becomes clean.
    del_y, del_x = directions[direction]
    y_pos = y_pos + del_y
    x_pos = x_pos + del_x

print(str(cause_infection) + " infections caused.")
# Answer is 5399.
