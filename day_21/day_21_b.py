# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 21:  Fractal Art, Part 2                                                        |
# | Website: https://adventofcode.com/2017/day/21                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

import numpy as np


# Chop the two-dimensional array into 2x2 or 3x3 sub-arrays.  A list of 2d sub-arrays is returned.
# The size of an input array is equal to the number of rows (which is equal to the number of columns since the input
# array is a square array).
# If the size is evenly divisible by 2, break the pixels up into 2x2 squares, and convert each 2x2 square into a 3x3
# square by following the corresponding enhancement rule in the rule-book.
# Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3 squares, and convert each 3x3 square into
# a 4x4 square by following the corresponding enhancement rule.
# The returned object, array_chops, contains the sub-arrays in order first from left to right (horizontally speaking),
# and then from top to bottom (vertically speaking).
def get_array_chops(array_2d):
    n_elements = array_2d.size
    if not (n_elements % 2):
        denominator = 4
    else:
        denominator = 9
    n_blocks = n_elements // denominator
    n_rows_or_cols_of_n_blocks = int(np.sqrt(n_blocks))
    arrays_downwards = np.vsplit(array_2d, n_rows_or_cols_of_n_blocks)
    array_chops = []
    for index in range(n_rows_or_cols_of_n_blocks):
        arrays_across = np.hsplit(arrays_downwards[index], n_rows_or_cols_of_n_blocks)
        array_chops += arrays_across
    return array_chops


# Flatten the list of two-dimensional 2x2 or 3x3 numpy sub-arrays into a list of strings.
def get_flat_strings_version(array_chops_list):
    my_strings = []
    for elem in array_chops_list:
        elem = list(elem.flatten())
        flat_elem = "".join(str(e) for e in elem)
        my_strings.append(flat_elem)
    return my_strings


# Use the "rule-book" to determine the new string that should take the place of the old string.  I.e. follow the
# appropriate enhancement rule in the art rule-book.
# A string corresponding to a 2x2 sub-array is replaced by a string that corresponds to a 3x3 sub-array.
# Similarly, a string corresponding to a 3x3 sub-array is replaced by a string that corresponds to a 4x4 sub-array.
def new_flats_list(flat_strings_list):
    new_list = []
    for flat_string in flat_strings_list:
        new_list.append(my_dict[flat_string])
    return new_list


# Convert the input list of strings into a large two-dimensional numpy array.
def populate_new_array(flat_strings_list):
    n_blocks = len(flat_strings_list)
    array_dimension = int(np.sqrt(n_blocks))
    n_elements_per_block = len(flat_strings_list[0])
    dimension_per_block = int(np.sqrt(n_elements_per_block))
    array_list = []
    for flat_string in flat_strings_list:
        array_holder = np.zeros((dimension_per_block, dimension_per_block), dtype=str)
        array_holder[:, :] = np.array(list(flat_string)).reshape((dimension_per_block, dimension_per_block))
        array_list.append(array_holder)
    base_indices = list(range(array_dimension))
    arrays_down = []
    for k in range(array_dimension):  # create a list of numpy arrays that have been stitched together horizontally.
        indices = [(array_dimension * k) + index for index in base_indices]
        stitch = np.hstack((array_list[indices[0]: indices[-1] + 1]))
        arrays_down.append(stitch)
    return np.vstack(arrays_down[0: array_dimension])  # stitch all the horizontal components vertically into a square
# array.


# Check to see if the variation of a rule in the "rule-book" is already present in the my_dict dictionary.
def test_variation(variation, value):
    if variation in my_dict.keys():  # we ignore the variation and do not add it to the rule book since it is already
        # present.
        pass
    else:  # we add the variation to the rule book since it is missing at this stage from the rule-book.
        my_dict[variation] = value


# variant_1 --> variant_7 represent all the possible variations of a given rule in the rule-book.
# The variants can be achieved via rotation and/or flipping of the original input pattern.
# Rotation can be either anticlockwise, or clockwise, whereas flipping can be either along the vertical axis or the
# horizontal axis (mirroring).
def populate_variants(orig):
    original_value = my_dict[orig]
    if not (len(orig) % 2):
        variant_1 = orig[2] + orig[3] + orig[0] + orig[1]
        variant_2 = orig[1] + orig[0] + orig[3] + orig[2]
        variant_3 = orig[3] + orig[2] + orig[1] + orig[0]
        variant_4 = orig[0] + orig[2] + orig[1] + orig[3]
        variant_5 = orig[1] + orig[3] + orig[0] + orig[2]
        variant_6 = orig[2] + orig[0] + orig[3] + orig[1]
        variant_7 = orig[3] + orig[1] + orig[2] + orig[0]
    else:
        variant_1 = orig[6] + orig[7] + orig[8] + orig[3] + orig[4] + orig[5] + orig[0] + orig[1] + orig[2]
        variant_2 = orig[2] + orig[1] + orig[0] + orig[5] + orig[4] + orig[3] + orig[8] + orig[7] + orig[6]
        variant_3 = orig[8] + orig[7] + orig[6] + orig[5] + orig[4] + orig[3] + orig[2] + orig[1] + orig[0]
        variant_4 = orig[0] + orig[3] + orig[6] + orig[1] + orig[4] + orig[7] + orig[2] + orig[5] + orig[8]
        variant_5 = orig[2] + orig[5] + orig[8] + orig[1] + orig[4] + orig[7] + orig[0] + orig[3] + orig[6]
        variant_6 = orig[6] + orig[3] + orig[0] + orig[7] + orig[4] + orig[1] + orig[8] + orig[5] + orig[2]
        variant_7 = orig[8] + orig[5] + orig[2] + orig[7] + orig[4] + orig[1] + orig[6] + orig[3] + orig[0]
    # Before naively adding all the variations to the rule-book, we test first whether the variations might be already
    # present.  Otherwise our rule-book becomes redundant as it contains duplicated key:value pairs.
    test_variation(variant_1, original_value)
    test_variation(variant_2, original_value)
    test_variation(variant_3, original_value)
    test_variation(variant_4, original_value)
    test_variation(variant_5, original_value)
    test_variation(variant_6, original_value)
    test_variation(variant_7, original_value)


f_name = "day_21_input.txt"  # Your puzzle input, a.k.a. the (incomplete) art rule-book containing the enhancement
# rules.

my_dict = dict()
f = open(f_name, "r")
for line in f.readlines():
    if line in ["\n", "", " "]:
        break
    line = line.rstrip("\n")
    line = line.split("=>")
    left = line[0].strip()
    right = line[1].strip()
    left = "".join(list(filter(lambda char: char != "/", left)))  # remove all the / characters.
    right = "".join(list(filter(lambda char: char != "/", right)))  # remove all the / characters.
    # print(left + " | " + right)
    my_dict[left] = right  # my_dict is a dictionary with (input pattern): (output pattern) pairs.
f.close()

my_keys = list(my_dict.keys())

for key in my_keys:
    populate_variants(key)

fractal_array = np.array([[".", "#", "."],  # part of your puzzle input; how the 2d array starts out in the beginning.
                          [".", ".", "#"],
                          ["#", "#", "#"]])

n_iterations = 18  # The alteration for Part 2 of the puzzle problem.  In Part 1, n_iterations was equal to 5.

for i in range(n_iterations):
    chops = get_array_chops(fractal_array)
    flat_strings = get_flat_strings_version(chops)
    new_flat_strings = new_flats_list(flat_strings)
    fractal_array = populate_new_array(new_flat_strings)

condition = fractal_array == "#"
number_on_pixels = np.count_nonzero(condition)
print(str(number_on_pixels) + " number of # pixels after " + str(n_iterations) + " iterations.")
# Answer is 2169301.
