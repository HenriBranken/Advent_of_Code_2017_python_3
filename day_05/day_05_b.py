# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 5: A Maze of Twisty Trampolines, All Alike, Part 2                              |
# | Website: https://adventofcode.com/2017/day/5                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

instructions = []
f = open("day_05_input.txt")  # Your puzzle input
for line in f.readlines():
    if line in ["", " ", "\n"]:
        break
    line = line.rstrip()
    instructions.append(int(line))
f.close()

max_index = len(instructions) - 1

cumulative = 0
index = 0

# Here we appropriately decrement or increment instructions[index] based on the value of instructions[index].
# Again, if the running index value exceeds the index boundaries of the instructions list, we break and output
# the cumulative value.
# For every legal jump we increment the cumulative value.
while True:
    n_jumps = instructions[index]
    if n_jumps >= 3:
        instructions[index] = n_jumps - 1
    else:
        instructions[index] = n_jumps + 1
    index += n_jumps
    cumulative += 1
    if (index > max_index) or (index < 0):
        break

print(str(cumulative) + " steps to reach the exit.")
# Answer is 28372145.
