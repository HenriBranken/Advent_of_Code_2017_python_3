# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 11:  Hex Ed, Part 2                                                             |
# | Website: https://adventofcode.com/2017/day/11                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'


def get_steps(y_pos, x_pos):
    del_y = abs(y_pos)
    del_x = abs(x_pos)
    if (del_y == 0) and (del_x == 0):
        moves = del_y  # i.e. moves = 0.
    elif del_y == del_x:
        moves = del_y  # i.e. moves = del_x = del_y.
    else:
        diag_steps = del_x  # number of diagonal steps equals del_x.
        del_up_or_down = del_y - del_x  # total change in the vertical direction.
        up_or_down_steps = del_up_or_down // 2  # vertical jumps are equal to 2 units each, compared to horiz jumps.
        moves = diag_steps + up_or_down_steps  # sum diag_steps and up_or_down_steps to get the total number of steps.
    return moves


filename = "day_11_input.txt"  # Your puzzle input.
path = []
f = open(filename, "r")
paths = f.readline().rstrip().split(",")
f.close()

# dictionary of (dy, dx)
my_dict = {"nw": (-1, -1), "n": (-2, 0), "ne": (-1, 1), "se": (1, 1), "s": (2, 0), "sw": (1, -1)}

# y, x position
current_position = [0, 0]  # the starting (y, x) position.

away = []
for step in paths:
    dy, dx = my_dict.get(step)
    current_position[0] += dy
    current_position[1] += dx
    away.append(get_steps(current_position[0], current_position[1]))
    # away is populated by the total number of moves from (0, 0) for each step contained in paths.

# In contrast to Part 1, we calculate the maximum distance the child process ever got from his starting position during
# his entire journey.
print(str(max(away)) + " steps is the furthest the child process ever got from his starting position.")
# Answer is 1567.
