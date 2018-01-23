# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 17:  Spinlock, Part 2                                                           |
# | Website: https://adventofcode.com/2017/day/17                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

n_steps = 382  # your puzzle input
n_cycles = 50000000  # your puzzle input
search_value = 0  # your puzzle input

circ_buffer = [0]  # the circular buffer starts out with the single value of 0.
buffer_len = len(circ_buffer)
max_index = buffer_len - 1
curr_pos = 0

# A trick is involved here...  It should be noticed that the value of 0 remains fixed at index position 0.
# Consequently, we are only interested in the value at index position 1, i.e. the value adjacent to 0.
# Finally then, we are not concerned with the evolution of the entire circular buffer.
for v in range(1, n_cycles + 1):  # for v in range 1, 2, ..., 49999999, 50000000.
    curr_pos = int((curr_pos + n_steps) % buffer_len)  # step n_steps through the circular buffer; get stop_pos
    if curr_pos == 0:
        value_of_interest = v  # insert v AFTER the stop_pos = curr_position (i.e. at insertion_point)
    curr_pos += 1  # update the current position, curr_pos
    buffer_len += 1

print(str(value_of_interest) + " is the value after 0 the moment 50,000,000 is inserted.")
# Answer is 33454823.
