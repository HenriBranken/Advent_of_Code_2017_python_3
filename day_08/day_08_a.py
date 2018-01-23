# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 8:  I Heard You Like Registers, Part 1                                          |
# | Website: https://adventofcode.com/2017/day/8                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

f = open("day_08_input.txt", "r")  # Your puzzle input.
g = []
h = dict()
for line in f.readlines():
    g.append(line.split())
f.close()

for register1, mod, shift, condition, register2, operator, value2 in g:
    if register1 not in h.keys():  # initialise the register to 0 if the register is encountered for the first time.
        h[register1] = 0
    if register2 not in h.keys():  # similarly as above.
        h[register2] = 0

    ans = eval("h[register2] " + operator + " int(value2)")  # evaluate whether the condition is True or False.
    if ans:  # if the condition evaluated to True, proceed with the modifications.
        if mod == "inc":
            h[register1] += int(shift)  # increment register1 with the shift value.
        elif mod == "dec":
            h[register1] -= int(shift)  # decrement register1 with the shift value.
# find the largest value in any register AFTER COMPLETION of the instructions.
print(str(max(h.values())) + " is the largest value in any register after completing the instructions.")
# Answer is 5221.
