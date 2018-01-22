# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 23:  Coprocessor Conflagration, Part 2                                          |
# | Website: https://adventofcode.com/2017/day/23                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# | Acknowledgement:  Thanks to Michael Gilliland @                                     |
# | https://www.youtube.com/watch?v=AqXTZo6o34s for shedding some light on the solution |
# | to the puzzle problem.                                                              |
# '-------------------------------------------------------------------------------------'


# if we translate day_23_input.txt into imperative code, and do the necessary simplifications, we come up with the
# following initialisation and nested for loop.  This simplified for-loop represents an optimized version of
# day_23_input.txt
# The key to solving this problem, is to find all the non-prime (composite) numbers in the list:
# [107900, 107917, ..., 124883, 124900].
b = 107900
c = 124900
d = 0
e = 0
f = 0
g = 0
h = 0

for value in range(b, c + 1, 17):
    for divisor in range(2, value):
        if not (value % divisor):  # we have determined that value is a non-prime number, and hence increment h.
            h += 1
            break

print(str(h) + " is the value left in register h.")
# Answer is 907.
