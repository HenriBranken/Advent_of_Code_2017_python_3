# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 25: The Halting Problem, Part 1                                                 |
# | Website: https://adventofcode.com/2017/day/25                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

import time

blueprint = dict()  # blueprint is a python dictionary that corresponds with the puzzle input contained in
# day_25_input.txt
blueprint["A"] = {0: [1, "right", "B"], 1: [0, "left", "B"]}
blueprint["B"] = {0: [0, "right", "C"], 1: [1, "left", "B"]}
blueprint["C"] = {0: [1, "right", "D"], 1: [0, "left", "A"]}
blueprint["D"] = {0: [1, "left", "E"], 1: [1, "left", "F"]}
blueprint["E"] = {0: [1, "left", "A"], 1: [0, "left", "D"]}
blueprint["F"] = {0: [1, "right", "A"], 1: [1, "left", "E"]}

tape = [0 for i in range(3*12586542)]  # we approximate the maximum, necessary length of the tape to be roughly equal to
# 3 times the number of steps taken by the turing machine.  This allows for approximately 1.5 times the number of steps
# in either the right or left direction, when starting at the middle of the tape.
# If we start out with a tape = [0], it means we have to use insert and append methods to grow the tape accordingly.
# This takes up way too much memory, and takes a very long time for the whole script to execute.
curr_position = len(tape) // 2

n_steps = 12586542  # part of the puzzle input.
state = "A"  # the state in which the Turing machine starts out.
value = 0  # all values along the tape initially start out at zero.
now = time.time()
for i in range(n_steps):
    tape[curr_position] = blueprint[state][value][0]  # set the value of the tape at curr_position to the value
    # predefined in the blueprint.
    direction = blueprint[state][value][1]  # determine the new direction, according to the blueprint.
    state = blueprint[state][value][2]  # determine the new state of the Turing machine, according to the blueprint.
    if direction == "right":
        del_x = 1  # Move in the East direction.
    else:
        del_x = -1  # Move in the West direction.
    curr_position += del_x
    value = tape[curr_position]  # determine what is the value of the tape at the new index position.
    if not (i + 1) % 1000000:
        print("i + 1 = " + str(i + 1) + ".")
        print("time.time() - now = " + str(time.time() - now))
        now = time.time()

num_ones = tape.count(1)  # Count the number of times the value 1 appears on the tape.

print("\n" + str(num_ones) + " is the checksum after " + str(n_steps) + " steps.")
# Answer is 3732.
