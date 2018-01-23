# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 12:  Digital Plumber, Part 2                                                    |
# | Website: https://adventofcode.com/2017/day/12                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

filename = "day_12_input.txt"  # Your puzzle input.
f = open(filename, "r")
data = dict()
for line in f.readlines():
    line = line.rstrip()
    left_right = line.split(" <-> ")
    left = int(left_right[0])
    right = left_right[1].split(",")
    for i, r in enumerate(right):
        right[i] = int(r)
    data[left] = right
f.close()

groups = 0
set_aside = list(data.keys())

while len(set_aside) > 0:
    entity = set_aside[0]  # programs in set_aside have not been assigned to a group of programs yet; needs evaluation.
    connected_to_entity = []  # i.e. connected to the first program entity in set_aside.
    difference = [777]  # the difference list serves as a sentinel and informs us when to break the while loop.
    delta = difference[0]  # a dummy initialisation to ensure the following while-loop is activated.
    while delta > 0:  # while we have not exhausted all the programs connected to nominated entity.
        for key in set_aside:  # looping over all the remaining programs in set_aside.
            if key == entity:  # the key is the nominated entity.
                connected_to_entity.append(key)  # append key.
                set_aside.remove(key)  # remove appended key from set_aside.
            elif key != entity:  # the key from set_aside is not equal to the nominated entity.
                if entity in data[key]:  # nominated entity is in list of programs specified by data[key] = some_list.
                    connected_to_entity.append(key)  # And therefore key is connected to the nominated entity.
                    set_aside.remove(key) # remove appended key from set_aside.
                else:  # else if nominated entity is NOT in list of programs specified by data[key] = some_list.
                    for v in data[key]:  # loop over the list of programs specified by data[key] = some_list.
                        if v in connected_to_entity:  # if individual program is in growing list connected_to_entity.
                            connected_to_entity.append(key)  # working backwards, key must be connected to entity.
                            set_aside.remove(key)  # remove afore-mentioned key from set_aside.
                            break # we should break to ensure that key does not accidentally get appended again.
        difference.append(len(set_aside))
        delta = abs(difference[-1] - difference[-2])
        # should delta > 0, execute while-loop again to find more programs connected to nominated entity.
    # should delta be zero, we have exhausted all the programs that are connected to entity.
    # Therefore a bona-fide group has been formed; we should move on to a new nominated entity from set_aside.
    groups += 1

print(str(groups) + " groups in total represent the village.")
# Answer is 202.
