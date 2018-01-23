# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 2: Corruption Checksum, Part 1                                                  |
# | Website: https://adventofcode.com/2017/day/2                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

filename = "day_02_input.txt"  # The puzzle input.

cumulative = 0
my_list = []

f = open(filename, "r")
for line in f.readlines():
    if line in ["", " ", "\n"]:
        break
    line = line.rstrip()
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    line.sort()
    my_list.append(line)
f.close()

# Extract the maximum and minimum from each row, subtract, and accrue to the cumulative sum.
for row in my_list:
    difference = max(row) - min(row)
    cumulative += difference

print(str(cumulative) + " is the checksum.")
# Answer is 36766.
