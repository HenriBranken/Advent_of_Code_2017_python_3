# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 6:  Memory Reallocation, Part 1                                                 |
# | Website: https://adventofcode.com/2017/day/6                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

import numpy as np


# this function tests whether a configuration is present in the matrix that occurs twice, each at different rows.
# Should this be the case, we need to break from the while loop at the bottom.
def tester(matrix):
    size_y, size_x = matrix.shape
    for index in range(size_y - 1):
        if list(matrix[index, :]) == list(matrix[size_y - 1, :]):
            return 1
    else:
        return 0


f = open("day_06_input.txt", "r")  # Your puzzle input.
line = f.readline()
line = line.rstrip()
arr = line.split()
f.close()

for i in range(len(arr)):
    arr[i] = int(arr[i])

configs = np.zeros((1, len(arr)), dtype=int)
configs[0, :] = arr[:]

sy, sx = configs.shape

flag = 0
j = 0

# In each iteration we invoke flag = tester(configs) to test whether there is a configuration in the growing matrix that
# occurs twice, each one in a different row.
while True:
    list_of_interest = list(configs[sy - 1, :])
    index_max = list_of_interest.index(max(list_of_interest))
    max_val = max(list_of_interest)

    # set the maximum value equal to zero, and redistribute equally among the list by stepping through the indices.
    list_of_interest[index_max] = 0
    for i in range(1, max_val + 1):
        list_of_interest[(index_max + i) % sx] += 1
    configs = np.vstack((configs, list_of_interest))
    sy += 1
    flag = tester(configs)
    j += 1
    if flag:
        break

print(str(j) + " redistribution cycles needed before a configuration is produced that has been seen before.")
# Answer is 3156.
