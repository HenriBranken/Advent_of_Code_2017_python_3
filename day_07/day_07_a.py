# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 7:  Recursive Circus, Part 1                                                    |
# | Website: https://adventofcode.com/2017/day/7                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

tops = []
towers = []

f = open("day_07_input.txt", "r")  # Your puzzle input.
for line in f.readlines():
    if line in ["", " ", "\n"]:
        break
    line = line.rstrip()
    line = line.split()
    if '->' in line:
        one_dict = dict()
        left = line[0]
        rights = line[3:]
        for i, right in enumerate(rights):
            rights[i] = right.rstrip(',')
        one_dict[left] = rights  # create one dictionary with keys = bottom, supporting program, and values = the
        # programs that are suspended by the bottom program.
        towers.append(one_dict)  # contains all the towers
    else:
        tops.append(line[0])  # populate list containing only the programs that are suspended in the tower at the top.

hidden_nest = []
for tower in towers:  # tower is a dictionary with key = bottom program, and values = programs suspended by the bottom
    # program.
    base = next(iter(tower))  # base represents the program at the bottom doing the balancing.
    supporteds = tower[base]  # find all the programs suspended in the air by the base program.
    for supported in supporteds:  # loop over all the suspended programs one by one.
        if supported in tops:
            continue
        else:  # at this point, we have found a program that lives somewhere between the bottom-most program, and the
            # top-most "leaves" of the tower network.
            hidden_nest.append(supported)

for tower in towers:
    base = next(iter(tower))
    if base not in hidden_nest:  # once we find a base that does not live between the bottom-most program and the leaves
        # it simply means we have spotted the bottom-most program.  We need to break, and output that program name.
        break
else:
    base = None

print(base + " is the bottom-most program.")
# Answer is gmcrj.
