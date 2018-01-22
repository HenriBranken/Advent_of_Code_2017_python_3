# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 6:  Memory Reallocation, Part 2                                                 |
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


def memory_bank_redistributer(array):
    sy, sx = array.shape
    j = 0
    while True:
        list_of_interest = list(array[sy - 1, :])
        index_max = list_of_interest.index(max(list_of_interest))
        max_val = max(list_of_interest)

        list_of_interest[index_max] = 0
        for index in range(1, max_val + 1):
            list_of_interest[(index_max + index) % sx] += 1
        array = np.vstack((array, list_of_interest))
        sy += 1
        flag = tester(array)
        j += 1
        if flag:
            return j, list(array[-1, :])  # return the index at which a repeat occurs, and the repeated configuration.


f = open("day_06_input.txt", "r")  # Your puzzle input.
line = f.readline()
line = line.rstrip()
arr = line.split()
f.close()

for i in range(len(arr)):
    arr[i] = int(arr[i])

configs = np.zeros((1, len(arr)), dtype=int)
configs[0, :] = arr[:]

_, last_config = memory_bank_redistributer(configs)  # first find the specific configuration that occurs twice.
configs = np.zeros((1, len(arr)), dtype=int)
configs[0, :] = last_config  # assign this recurring configuration to configs.
n_cycles, _ = memory_bank_redistributer(configs)  # find the size of the loop in which the configuration repeats again.

print(str(n_cycles) + " is the size of the loop.")
# Answer is 1610.
