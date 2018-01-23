# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 1: Inverse Captcha, Part 1                                                      |
# | Website: https://adventofcode.com/2017/day/1                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

fname = "day_01_input.txt"  # Your puzzle input
f = open(fname, "r")
str_number = f.readline().rstrip()
f.close()

cumulative = 0
length = len(str_number)

# Notice how the modulo operator is used to wrap the index back to the front if (index + 1) >= length.
for index in range(len(str_number)):
    if str_number[index % length] == str_number[(index + 1) % length]:
        cumulative += int(str_number[index])

print(str(cumulative) + " is the cumulative value.")
# Answer is 1031.
