# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 10:  Knot Hash, Part 1                                                          |
# | Website: https://adventofcode.com/2017/day/10                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

# getting the lengths from the input
filename = "day_10_input.txt"  # Your puzzle input.
f = open(filename, "r")
lengths = f.readline().rstrip().split(",")
for i, le in enumerate(lengths):
    lengths[i] = int(le)  # lengths, as the name implies, is a list of integer lengths.
f.close()

# instantiating the circular list
n_elements = 256
circular_list = [i for i in range(n_elements)]  # circular list is a list that ranges from 0 to 255, in steps of 1.

# defining other variables
current_position = 0  # we begin at the beginning of the circular list.
skip_size = 0

# beginning the algorithm
for length in lengths:  # iterating over the list of integer lengths (the puzzle input)
    # reversing the sublist which contains <length> elements
    sublist = []
    starting_pos = current_position
    for i in range(int(length)):  # extract the sublist of length = length.
        sublist.append(circular_list[current_position])
        current_position = (current_position + 1) % len(circular_list)
    sublist = sublist[::-1]  # reverse the extracted sublist.
    current_position = starting_pos  # re-instate the current index position to the starting position.

    for i in range(int(length)):
        circular_list[current_position] = sublist[i]  # set the portion of the circular list equal to the extracted
        #  sublist.
        if i == int(length) - 1:
            break
        else:
            current_position = (current_position + 1) % len(circular_list)
    current_position = starting_pos  # re-instate current index position to the starting position.

    # moving the index forward by length + skip_size
    jump_size = length + skip_size
    current_position = (current_position + jump_size) % len(circular_list)

    # incrementing the skip_size
    skip_size += 1

print(str(circular_list[0] * circular_list[1]) + " is the result of multiplying the first two numbers in the list.")
# Answer is 62238.
