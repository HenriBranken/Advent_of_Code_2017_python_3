# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 13:  Packet Scanners, Part 1                                                    |
# | Website: https://adventofcode.com/2017/day/13                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'


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
        if new_s_index == (length - 1):  # reverse direction of the scanner
            some_dictionary[d][0] = -1
        elif new_s_index == 0:  # reverse direction of the scanner
            some_dictionary[d][0] = 1
    return some_dictionary


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
        firewall[depth] = [0, [""]]  # this particular layer does not have a scanner.

# The severity of getting caught on a layer is equal to its depth multiplied by its range.
# We ignore layers in which you do not get caught.
# The severity of the WHOLE TRIP is the sum of these values.
severity = 0
for pico_second in range(max_layer + 1):  # in this for-loop we are traversing the entire firewall from left -> right.
    if firewall[pico_second][1][0] == "S":  # If true, we have then been caught by a scanner at the top of the layer.
        severity += pico_second * len(firewall[pico_second][1])  # accrue to the severity of the entire trip thus far.
    firewall = advance_firewall_pico_second(firewall)  # Move the scanners accordingly to their new configuration.
print(str(severity) + " is the severity of the whole trip if you leave immediately.")
# Answer is 1928.
