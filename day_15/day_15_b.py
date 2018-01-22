# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 15:  Dueling Generators, Part 2                                                 |
# | Website: https://adventofcode.com/2017/day/15                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

# the input
val_a, val_b = 634, 301  # Your puzzle input.
sample_size = 5000000


def convert_to_binary(some_value):
    return "{0:032b}".format(int(some_value))


def get_rightmost_half(some_binary):
    return some_binary[16:]


def generator_a(value_a):
    yield (value_a * 16807) % 2147483647


def generator_b(value_b):
    yield (value_b * 48271) % 2147483647


cumulative = 0
i = 0
while True:
    while True:  # we need to find a val_a that satisfies val_a % 4 == 0.
        val_a = next(generator_a(val_a))
        if not (val_a % 4):
            break
    val_a_bin = convert_to_binary(val_a)
    val_a_bin16 = get_rightmost_half(val_a_bin)
    while True:  # we need to find a val_b that satisfies val_b % 8 == 0 to compare with val_a.
        val_b = next(generator_b(val_b))
        if not (val_b % 8):
            break
    val_b_bin = convert_to_binary(val_b)
    val_b_bin16 = get_rightmost_half(val_b_bin)
    if val_a_bin16 == val_b_bin16:
        cumulative += 1
    i += 1
    if not (i % 100000):
        print(i)
    if i >= sample_size:  # once we have exceeded the sample size, we break out of the infinite while loop.
        break

print(str(cumulative) + " is the judge's final count.")
# Answer is 294.
