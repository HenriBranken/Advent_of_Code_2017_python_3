# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 9:  Stream Processing, Part 1                                                   |
# | Website: https://adventofcode.com/2017/day/9                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

# reading in the input
puzzle_input = []
filename = "day_09_input.txt"  # Your puzzle input.

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
    else:  # else, we have found a character other than the exclamation mark.  Increment index to continue the search
        # for !'s.
        index += 1
    if index >= length:  # we have exhausted the entire character stream and reached the end.  break.
        break

# remove the garbage demarcated by <   >
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
                    garbage_chars += 1  # keep track of how many garbage characters are deleted.
                length = len(puzzle_input)
                index = garbage_begin_i  # reset the index to garbage_begin_i.
                garbage_chars -= 2  # take account of the opening and closing < >.
    else:  # else, increment the index to keep on searching for <.
        index += 1
    if index >= length:
        flag = False  # hence the while-loop is broken.

# count the groups
flag = True
index = 0
length = len(puzzle_input)  # at this point, puzzle_input has been cleaned of all the garbage.
n_groups = 0
while flag:
    if puzzle_input[index] == "{":
        n_groups += 1  # we have found a group.
        index += 1
    else:
        index += 1
    if index >= length:
        flag = False

# getting the score
nesting_level = 0
flag = True
index = 0
length = len(puzzle_input)
cumulative = 0
while flag:
    if puzzle_input[index] == "{":
        nesting_level += 1  # nesting_level keeps track of the level of nested {.
        cumulative += nesting_level  # cumulative keeps track of the total running score.
        index += 1
    elif puzzle_input[index] == "}":
        nesting_level -= 1
        index += 1
    else:
        index += 1
    if index >= length:
        flag = False
print(str(cumulative) + " is the total score for all groups in the input.")
# Answer is 11846.
