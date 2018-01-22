# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 13:  Packet Scanners, Part 1                                                    |
# | Website: https://adventofcode.com/2017/day/13                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# | Acknowledgements:  Thanks to Michael Gilliland @                                    |
# | https://www.youtube.com/watch?v=AmYmwO2O6Z0 for shedding some light on the solution |
# | to the problem.                                                                     |
# '-------------------------------------------------------------------------------------'

filename = "day_13_input.txt"  # Your puzzle input.
my_dict = {}
f = open(filename, "r")
for line in f.readlines():
    if line in ["", " ", "\n"]:
        break
    line = line.rstrip()
    left_right = line.split(": ")
    left = int(left_right[0])
    right = int(left_right[1])
    my_dict[left] = right
f.close()

max_layer = max(list(my_dict.keys()))
firewall = []
for depth in range(max_layer + 1):
    if depth in list(my_dict.keys()):
        firewall.append(my_dict[depth])
    else:
        firewall.append(0)  # i.e. we are at a layer that has no range and also no scanners.

severity = 0
for layer_or_step_or_tick in range(max_layer + 1):
    if firewall[layer_or_step_or_tick] == 0:
        continue  # this layer is not significant because it does not contain any scanners.

    # the following condition reflects whenever a scanner is found at the top of its layer.
    if (layer_or_step_or_tick % ((firewall[layer_or_step_or_tick] - 1) * 2)) == 0:
        severity += layer_or_step_or_tick * firewall[layer_or_step_or_tick]  # we have been caught, therefore accrue
        # severity value to severity variable.
print(str(severity) + " is the severity when the firewall is crossed immediately.")
# Answer is 1928.
