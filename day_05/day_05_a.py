# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 5: A Maze of Twisty Trampolines, All Alike, Part 1                              |
# | Website: https://adventofcode.com/2017/day/5                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

instructions = []
f = open("day_05_input.txt")  # Your puzzle input goes here.
for line in f.readlines():
    if line in ["", " ", "\n"]:
        break
    line = line.rstrip()
    instructions.append(int(line))
f.close()

max_index = len(instructions) - 1

cumulative = 0
index = 0

# once our running index jumps outside the index boundaries of the instructions list, we break the while-loop.
# Otherwise, we increment cumulative for every legal jump.
while True:
    n_jumps = instructions[index]
    instructions[index] = n_jumps + 1  # offset of the current instruction increases by 1
    index += n_jumps
    cumulative += 1
    if (index > max_index) or (index < 0):
        break

print(str(cumulative) + " steps to reach the exit.")
# Answer is 356945.
