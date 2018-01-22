# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 17:  Spinlock, Part 1                                                           |
# | Website: https://adventofcode.com/2017/day/17                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

n_steps = 382  # your puzzle input.
n_cycles = 2017  # your puzzle input
search_value = 2017  # your puzzle input.

circ_buffer = [0]  # The circular buffer starts out with the single value of 0.
buffer_len = len(circ_buffer)
curr_pos = 0

for v in range(1, n_cycles + 1):  # for v in range 1, 2, ..., 2016, 2017.
    curr_pos = int((curr_pos + n_steps) % buffer_len)  # step n_steps through the circular buffer; get stop_pos
    curr_pos += 1  # update the current position, curr_pos
    circ_buffer.insert(curr_pos, v)
    buffer_len += 1

index_of_interest = circ_buffer.index(2017) + 1  # we want the value that is adjacent to 2017.
print(str(circ_buffer[index_of_interest]) + " is the value after 2017 in the completed buffer.")
# Answer is 1561.
