# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 10:  Knot Hash, Part 2                                                          |
# | Website: https://adventofcode.com/2017/day/10                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

# getting the lengths from the input
lengths = []
filename = "day_10_input.txt"  # Your puzzle input.
f = open(filename, "r")
for char in f.readline():
    lengths.append(ord(char))  # return an integer representing the Unicode code point of the character when the
    # argument is a unicode object, or the value of the byte when the argument is an 8-bit string.
f.close()
suffix = [17, 31, 73, 47, 23]
lengths = lengths + suffix  # lengths, as the name implies, is a list of integer lengths.

# instantiating the circular list
n_elements = 256
circular_list = [i for i in range(n_elements)]  # circular list is list that ranges from 0 to 255, in steps of 1.

# defining other variables
current_position = 0  # we begin at the beginning of the circular list.
skip_size = 0

# repeat the algorithm of Part 1 a number of 64 times altogether.
# Note that the current position and skip size are preserved between the rounds.
for _ in range(64):
    # beginning the algorithm
    for length in lengths:  # iterating over the list of integer lengths (the puzzle input).
        # reversing the sublist which contains <length> elements
        sublist = []
        starting_pos = current_position
        for i in range(length):  # extract the sublist of length = length.
            sublist.append(circular_list[current_position])
            current_position = (current_position + 1) % len(circular_list)
        sublist = sublist[::-1]  # reverse the extracted sublist.
        current_position = starting_pos  # re-instate the current index position to the starting position.

        for i in range(length):
            circular_list[current_position] = sublist[i]  # set the portion of the circular list equal to the extracted
            # sublist.
            current_position += 1
            if current_position > (len(circular_list) - 1):
                current_position = 0
        current_position = starting_pos  # re-instate the current index position to the starting position.

        # moving the index forward by length + skip_size
        jump_size = length + skip_size
        current_position = (current_position + jump_size) % len(circular_list)

        # incrementing the skip_size
        skip_size += 1

grouped_hash = [[] for _ in range(16)]  # a list of 16 empty python lists.
sub_group = [0 for _ in range(16)]  # a list of 16 zeros.
j = 0
# here we are partitioning the circular list into 16 sublists each of length 16.  (16 x 16 = 256.)
for i, elem in enumerate(circular_list):  # circular list has a length of 256.
    if (i % 16) <= 15:
        sub_group[i % 16] = elem
    if (i % 16) == 15:
        grouped_hash[j] = sub_group
        sub_group = [0 for _ in range(16)]  # re-instate subgroup to be a list of 16 zeros.
        j += 1

xored = []
for sub_group in grouped_hash:  # stepping through the 16 sublists contained in grouped_hash.
    cum = sub_group[0] ^ sub_group[1]
    for i in range(2, len(sub_group)):
        cum = cum ^ sub_group[i]  # perform numeric bitwise XOR on 16 elements of each sublist to populate dense hash.
    xored.append(cum)  # at the end, the dense hash is a list of 16 elements.

# Here we convert the dense hash into hexadecimal notation.
# Because every knoth hash is 16 numbers, the hexadecimal representation is always 32 hexadecimal digits long.
knot = ""
for elem in xored:
    if len(hex(elem)) == 3:
        knot += "0" + hex(elem)[2]  # always represent each number as 2 hexadecimal digits, including a leading 0 as
        # necessary.
    elif len(hex(elem)) == 4:
        knot += hex(elem)[2:]

print(knot + " is the knot hash.")
# Answer is 2b0c9cc0449507a0db3babd57ad9e8d8.
