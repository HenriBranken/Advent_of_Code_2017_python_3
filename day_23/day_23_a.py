# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 23:  Coprocessor Conflagration, Part 1                                          |
# | Website: https://adventofcode.com/2017/day/23                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

from Coprocessor import *

processor_a = Coprocessor("day_23_input.txt", "processor_a", a_value=0)  # day_23_input.txt is your puzzle input.
# In Part 1, a starts out with a value of 0.

while processor_a.status == "Active":
    processor_a.try_next_iteration()

print(str(processor_a.num_muls) + " number of times was the `mul' instruction invoked.")
# Answer is 5929.
