# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 14:  Disk Defragmentation, Part 2                                               |
# | Website: https://adventofcode.com/2017/day/14                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

import numpy as np

my_input = "uugsqrei"  # Your puzzle input.
square_dimension = 128


def convert_to_binary(the_hash_value):
    dummy = ["{0:04b}".format(int(char, 16)) for char in the_hash_value]  # 32 x 4 = 128.
    dummy2 = ""
    for d in dummy:
        dummy2 += d
    dummy3 = [int(char) for char in dummy2]
    return dummy3


# we wrap the knot-hash function from day_10_b.py into a function.
# See day_10_a/b for detailed comments on the knot-hash function.
def get_knot_hash(some_string):
    lengths = []
    for char in some_string:
        lengths.append(ord(char))
    suffix = [17, 31, 73, 47, 23]
    lengths = lengths + suffix

    # instantiating the circular list
    n_elements = 256
    circular_list = [ind for ind in range(n_elements)]
    # print(circular_list)

    # defining other variables
    current_position = 0
    skip_size = 0

    for _ in range(64):
        for length in lengths:
            # reversing the sublist which contains <length> elements
            sublist = []
            starting_pos = current_position
            for ind in range(length):
                sublist.append(circular_list[current_position])
                current_position = (current_position + 1) % len(circular_list)
            sublist = sublist[::-1]
            current_position = starting_pos

            for ind in range(length):
                circular_list[current_position] = sublist[ind]
                current_position = (current_position + 1) % len(circular_list)
            current_position = starting_pos

            # moving the index forward by length + skip_size
            jump_size = length + skip_size
            for ind in range(jump_size):
                current_position = (current_position + 1) % len(circular_list)

            # incrementing the skip_size
            skip_size += 1

    grouped_hash = [[] for _ in range(16)]
    sub_group = [0 for _ in range(16)]
    k = 0
    for ind, elem in enumerate(circular_list):
        if (ind % 16) <= 15:
            sub_group[ind % 16] = elem
        if (ind % 16) == 15:
            grouped_hash[k] = sub_group
            sub_group = [0 for _ in range(16)]
            k += 1

    xored = []
    for sub_group in grouped_hash:
        cum = sub_group[0] ^ sub_group[1]
        for ind in range(2, len(sub_group), 1):
            cum = cum ^ sub_group[ind]
        xored.append(cum)

    knot = ""
    for elem in xored:
        if len(hex(elem)) == 3:
            knot += "0" + hex(elem)[2]
        elif len(hex(elem)) == 4:
            knot += hex(elem)[2:]
    return knot


my_rows = []
for i in range(square_dimension):
    my_rows.append(my_input + "-" + str(i))  # i.e. uugsqrei-1 up untill uugsqrei-127.

my_knot_hashes = []
for row in my_rows:
    my_knot_hashes.append(get_knot_hash(row))  # get the knot-hash for each row in my_rows.

square_grid = np.zeros((square_dimension, square_dimension), dtype=int)
for i in range(128):
    square_grid[i, :] = convert_to_binary(my_knot_hashes[i])  # get the binary representation from the hexadecimal
    # stored in my_knot_hashes.

cumulative = np.sum(square_grid)

n_rows, n_cols = square_grid.shape

invalid_indices = []
one_positions = []
for j in range(n_rows):
    for i in range(n_cols):
        if square_grid[j, i] == 0:
            invalid_indices.append((j, i))  # we have identified an unoccupied tile
        elif square_grid[j, i] == 1:  # we have identified an occupied tile.
            one_positions.append((j, i))

num_one_positions = len(one_positions)

# direction: (dy, dx)
#       key: value
directions = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}

counter = 0
next_index = one_positions[0]  # (first_y_index, first_x_index) tuple representing a tile containing 1.
regions = 0
region_indices = [next_index]

# this while-loop terminates once len(invalid_indices) = the size of the square grid.
while len(invalid_indices) < square_grid.size:  # while len(invalid_indices) < 128 * 128
    for next_index in region_indices:  # loop over the already-identified indices of tiles containing one.
        for direct, (dy, dx) in directions.items():  # loop over the four directions of the compass.
            index = (next_index[0] + dy, next_index[1] + dx)  # create index that has taken step away from next_index.
            cond_1 = 0 <= index[0] < n_rows  # y_index must be within acceptable bounds.
            cond_2 = 0 <= index[1] < n_cols  # x_index must be within acceptable bounds.
            cond_3 = index not in invalid_indices  # index must represent a region-tile that contains 1 (not 0).
            cond_4 = index not in region_indices  # up until now, index has not been identified with region_indices.
            if cond_1 and cond_2 and cond_3 and cond_4:  # should all conditions be satisfied, add index to
                # region_indices.
                region_indices.append(index)
            else:
                continue  # try out the next direction
    else:  # once the above for-loop has exhausted itself, we have formed a bona-fide region of connected indices.
        invalid_indices = invalid_indices + region_indices  # grow invalid_indices with the bona-fide region indices.
        regions += 1
        if len(invalid_indices) < square_grid.size:
            while True:
                next_index = one_positions[counter]  # we need to find a new tile that belongs to a independent region.
                if next_index not in invalid_indices:
                    break
                elif next_index in invalid_indices:
                    counter += 1
        region_indices = [next_index]  # initialise the next region with the indices of the new tile that belongs to
        # an independent region.

print(str(regions) + " regions are present given the key string of uugsqrei.")
# Answer is 1141.
