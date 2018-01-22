# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 1: Inverse Captcha, Part 2                                                      |
# | Website: https://adventofcode.com/2017/day/1                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

fname = "day_01_input.txt"  # Your puzzle input.
f = open(fname, "r")
str_number = f.readline().rstrip()
f.close()

cumulative = 0
length = len(str_number)
step_size = length // 2

# Notice how the modulo operator is used to wrap the index back near the front if pos + step_size >= length.
for pos in range(length):
    if str_number[pos] == str_number[(pos + step_size) % length]:
        cumulative += int(str_number[pos])

print(str(cumulative) + " is the cumulative value.")
# Answer is 1080.
