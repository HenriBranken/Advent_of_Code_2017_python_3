# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 9:  Stream Processing, Part 2                                                   |
# | Website: https://adventofcode.com/2017/day/9                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

# reading in the input
puzzle_input = []
filename = "day_09_input.txt"  # Your puzzle input

f = open(filename, "r")
for line in f.readlines():
    for char in line:
        if char == '\n' or char == "":
            break
        else:
            puzzle_input.append(char)

# removing the !, and characters cancelled by !
length = len(puzzle_input)
index = 0
while True:
    if puzzle_input[index] == "!":
        del puzzle_input[index]  # delete the !
        del puzzle_input[index]  # delete the character following the !
        length = len(puzzle_input)  # get the new, shortened length of the character stream.
    else:  # else, we have ound a character other than the exclamation mark.  Increment the index to continue the search
        # for !'s
        index += 1
    if index >= length:  # we have exhausted the entire character stream and reached the end.  Break.
        break

# remove the garbage
closing_angle = True
length = len(puzzle_input)
flag = True
index = 0
garbage_chars = 0
while flag:
    if puzzle_input[index] == "<":
        garbage_begin_i = index
        closing_angle = False
        index += 1
        while not closing_angle:  # we search now for the index of the corresponding closing > of the opening <.
            if puzzle_input[index] != ">":
                index += 1  # keep on searching for the closing >
            elif puzzle_input[index] == ">":  # we have found the corresponding closing >.
                garbage_end_i = index
                garbage = garbage_end_i - garbage_begin_i + 1  # find the inclusive length of the garbage group.
                closing_angle = True
                for _ in range(garbage):
                    del puzzle_input[garbage_begin_i]  # delete all the garbage.
                    garbage_chars += 1  # keep track of how many garbage characters hare deleted.
                length = len(puzzle_input)
                index = garbage_begin_i  # reset the index to garbage_begin_i
                garbage_chars -= 2  # take account of the opening and closing < >.
    else:  # else, increment the index to keep on searching for <.
        index += 1
    if index >= length:
        flag = False  # hence the while-loop is broken.
# garbage_chars represent all the garbage characters that were enclosed within the < > group.
print(str(garbage_chars) + " non-cancelled characters are within the garbage.")
# Answer is 6285.
