# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 13:  Packet Scanners, Part 2                                                    |
# | Website: https://adventofcode.com/2017/day/13                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

import time
import copy


# The configuration of the firewall is advanced by moving the scanners in each layer accordingly.
def advance_firewall_pico_second(some_dictionary):
    for d in range(max_layer + 1):
        length = len(some_dictionary[d][1])
        if some_dictionary[d][0] == 0:  # ignore this layer as it does not have a scanner within it.
            continue
        current_s_index = some_dictionary[d][1].index("S")
        some_dictionary[d][1][current_s_index] = ""
        new_s_index = current_s_index + some_dictionary[d][0]  # some_dictionary[d][0] represents the scanner direction.
        some_dictionary[d][1][new_s_index] = "S"
        if new_s_index == (length - 1):
            some_dictionary[d][0] = -1  # reverse the direction of the scanner.
        elif new_s_index == 0:
            some_dictionary[d][0] = 1  # reverse the direction of the scanner.
    return some_dictionary


# If there is a scanner at the top of its layer, and the packet jumps into that layer, then we have been caught by the
# firewall.  Hence our trial delay time was unsuccessful.
def test_firewall_configuration(some_dictionary):
    for step in range(max_layer + 1):
        if some_dictionary[step][1][0] == "S":
            return False
        else:
            some_dictionary = advance_firewall_pico_second(some_dictionary)
    else:
        return True


filename = "day_13_input.txt"  # Your puzzle input
my_dict = {}
f = open(filename, "r")
for line in f.readlines():
    if line in ["", " ", "\n"]:
        break
    line = line.rstrip()
    left_right = line.split(": ")
    left = int(left_right[0])
    right = int(left_right[1])
    my_dict[left] = ["" for _ in range(right)]  # direction, [characters]
f.close()

max_layer = max(list(my_dict.keys()))  # the last layer at the end of the firewall.
firewall = {}
for depth in range(max_layer + 1):
    if depth in list(my_dict.keys()):
        size = len(my_dict[depth])
        firewall[depth] = [1, ["" for _ in range(size)]]
        firewall[depth][1][0] = "S"
    else:
        firewall[depth] = [0, [""]]  # this particular layer does not have scanner.

now = time.time()
pico_second = 0
delay = 0
while True:
    firewall_reference = copy.deepcopy(firewall)  # make a copy of the firewall before testing it out with
    # test_firewall_configuration() and advance_firewall_pico_second().
    flag = test_firewall_configuration(firewall)
    if flag:
        print(delay)
        break  # Our trial delay time was thus successful.  I.e. we have not been caught by the firewall scanners.
    else:
        delay += 1
        firewall = advance_firewall_pico_second(firewall_reference)  # try out a new firewall configuration as
        # determined from the total delay time in pico_seconds.
    if not (delay + 1) % 100000:  # displays the progress of the while-loop.
        print(delay + 1)
        print(time.time() - now)
        now = time.time()
print(str(delay) + " is the fewest number of picoseconds that you need to delay the packet by.")
# Answer is 3830344 (after waiting ~40 minutes).
