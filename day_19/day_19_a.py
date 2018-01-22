# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 19:  A Series of Tubes, Part 1                                                  |
# | Website: https://adventofcode.com/2017/day/19                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

import numpy as np


# changing from a vertical direction to a horizontal direction and vice versa whenever a "+" string character is
# encountered.
def checker(direct, position):
    global directions, array
    if direct in ["N", "S"]:
        options = ["E", "W"]
    else:
        options = ["N", "S"]
    del_y, del_x = directions[options[0]]  # Try out the first plausible direction.
    trial_pos = (position[0] + del_y, position[1] + del_x)  # Try out the first plausible direction.
    condition_1 = (j_bounds[0] <= trial_pos[0] <= j_bounds[1])  # the y/row index must be within acceptable bounds.
    condition_2 = (i_bounds[0] <= trial_pos[1] <= i_bounds[1])  # the x/col index must be within acceptable bounds.
    if condition_1 and condition_2:
        condition_3 = (array[trial_pos[0], trial_pos[1]] != " ")  # the first trial position must not be a blank char.
    else:
        condition_3 = False
    if condition_1 and condition_2 and condition_3:
        return options[0]  # the first plausible direction is the correct direction to continue in.
    else:
        return options[1]  # the second plausible direction is the correct direction to continue in.


f_name = "day_19_input.txt"  # Your puzzle input.
f = open(f_name, "r")
cols = len(f.readline().rstrip("\n"))
f.close()
rows = 0
f = open(f_name, "r")
for line in f.readlines():
    if line == "":
        break
    else:
        rows += 1
array = np.zeros((rows, cols), dtype=np.str_)
f.close()
f = open(f_name, "r")
for j, line in enumerate(f.readlines()):
    for i in range(cols):
        array[j, i] = line[i]
f.close()

# trim the array:  Remove any redundant white space surrounding the borders of the map.
while True:  # trim blank space surrounding the lhs of the map.
    lhs = array[:, 0]
    if all(lhs == " "):
        array = array[:, 1:]
    else:
        break
while True:  # trim blank space surrounding the rhs of the map.
    rhs = array[:, -1]
    if all(rhs == " "):
        array = array[:, 0:-1:1]
    else:
        break
while True:  # trim blank space surrounding the top of the map.
    top = array[0, :]
    if all(top == " "):
        array = array[1:, :]
    else:
        break
while True:  # trim blank space surrounding the bottom  of the map.
    bottom = array[-1, :]
    if all(bottom == " "):
        array = array[0:-1:1, :]
    else:
        break

rows, cols = array.shape
j_bounds = (0, rows - 1)
i_bounds = (0, cols - 1)
n_tiles = rows * cols  # which is equal to array.size

# key:value pairs are in the form of "direction": (dy, dx) taking computer-screen convention into account
directions = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}

illegal_js, illegal_is = np.where(array == " ")  # all the blank tiles are illegal tiles.
illegal_js, illegal_is = list(illegal_js), list(illegal_is)
illegal_inds = list(zip(illegal_js, illegal_is))  # a list of all the illegal indices that result in a blank tile " "

curr_pos = [0, list(array[0, :]).index("|")]  # The starting index on the top of the diagram
direction = "S"
dy, dx = directions[direction]
pathway = list()
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # alphabetic letters strewn along the path of the network packet.
char = array[curr_pos[0], curr_pos[1]]  # char at the [y, x] position
illegal_inds.append((curr_pos[0], curr_pos[1]))  # tiles already visited are added to the illegal_inds list.
flag = 0
steps = 1
while True:
    while char != "+":  # propagate in the current given direction until encountering a "+" sign
        curr_pos[0], curr_pos[1] = curr_pos[0] + dy, curr_pos[1] + dx
        char = array[curr_pos[0], curr_pos[1]]
        steps += 1  # a step has been taken by the network packet along the map.
        if tuple(curr_pos) not in illegal_inds:
            illegal_inds.append((curr_pos[0], curr_pos[1]))
        if char in letters:
            pathway.append(char)
        if len(illegal_inds) == n_tiles:  # we have exhausted the entire map at this point, and need to break.
            flag = 1
        if flag:
            break

    if flag:
        break
    direction = checker(direction, curr_pos)  # curr_pos should be at a "+" at this point.  We need to check what are
    # the plausible directions, and continue in the correct direction; i.e. the direction that does not start out with
    # a blank character " ".

    dy, dx = directions[direction]  # get the del_y and del_x of the new correct direction.
    curr_pos[0], curr_pos[1] = curr_pos[0] + dy, curr_pos[1] + dx
    char = array[curr_pos[0], curr_pos[1]]  # char is changed from "+" to the character adjacent to "+"
    illegal_inds.append((curr_pos[0], curr_pos[1]))
    steps += 1  # a step has been taken by the network packet along the map.
    if char in letters:
        pathway.append(char)  # we have encountered an alphabetic letter that was strewn along the path of the network
        # packet.  Append the alphabetic character to the pathway.

pathway = "".join(pathway)
print(pathway + " is the pathway followed by the network packet.")
# Answer is VEBTPXCHLI.
