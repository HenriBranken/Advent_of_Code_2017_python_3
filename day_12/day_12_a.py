# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 12:  Digital Plumber, Part 1                                                    |
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
# data is a dictionary containing the program ID's as keys, and the IDs with which the program can communicate directly.

inspect_length = [777]  # A dummy initialisation to initiate the infinite while-loop.
difference = inspect_length[0]
connected_to_zero = [0]
while True:
    for key, value_list in data.items():
        if key in connected_to_zero:  # key is already in connected to zero.  Therefore values must also be connected.
            for v in value_list:
                if v not in connected_to_zero:
                    connected_to_zero.append(v)  # append the "value" programs, but only once!
    inspect_length.append(len(connected_to_zero))
    if inspect_length[-1] == inspect_length[-2]:  # should the length of connected_to_zero remain stagnant, then we have
        # exhausted the list of programs that are connected to program ID 0.
        break

print(str(len(connected_to_zero)) + " is the number of programs that are connected to 0.")
# Answer is 113.
