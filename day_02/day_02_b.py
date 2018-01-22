# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 2: Corruption Checksum, Part 2                                                  |
# | Website: https://adventofcode.com/2017/day/2                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

filename = "day_02_input.txt"  # Your puzzle input.

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

# We ignore the case in which numerator == denominator, and continue on with the next for-loop iteration.
# The numerator is nominated from the end of each row, which is where the relatively large numbers live.
# Conversely, the denominator is nominated from the beginning of each row, where the relatively small numbers are found.
# If we find that numerator % denominator == 0, accrue numerator // denominator to the cumulative sum.
for row in my_list:
    for numerator in row[::-1]:
        for denominator in row[:]:
            if numerator == denominator:
                continue
            elif numerator % denominator == 0:
                cumulative += numerator // denominator
                break

print(str(cumulative) + " is the checksum.")
# Answer is 261.
