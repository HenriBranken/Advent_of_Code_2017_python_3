# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 8:  I Heard You Like Registers, Part 2                                          |
# | Website: https://adventofcode.com/2017/day/8                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

f = open("day_08_input.txt", "r")  # Your puzzle input
g = []
h = dict()
values = []

for line in f.readlines():
    g.append(line.split())
f.close()

for register1, mod, shift, condition, register2, operator, value2 in g:
    if register1 not in h.keys():  # initialise the register to 0 if the register s encountered for the first time.
        h[register1] = 0
    if register2 not in h.keys():  # similar to the above.
        h[register2] = 0

    ans = eval("h[register2] " + operator + " int(value2)")  # evaluate whether te condition is True of False.
    if ans is True:  # If the condition evaluated to be True, proceed with the modifications.
        if mod == "inc":
            h[register1] += int(shift)  # increment register1 with the shift value.
        elif mod == "dec":
            h[register1] -= int(shift)  # decrement register1 with the shift value.
    # the key insight is at the following step.  Append the value of register1 to the growing values list.
    values.append(h[register1])
# use the max function to find the highest value held in ANY REGISTER DURING THE ENTIRE PROCESS.
print(str(max(values)) + " is the highest value held in any register during the process.")
# Answer is 7491.
