# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 13:  Packet Scanners, Part 2                                                    |
# | Website: https://adventofcode.com/2017/day/13                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# | Acknowledgements:  Thanks to Michael Gilliland @                                    |
# | https://www.youtube.com/watch?v=i8xOQHGHdDQ for shedding some light on the solution |
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
        firewall.append(0)

delay = 0
while True:
    for layer_or_step_or_tick in range(max_layer + 1):
        if firewall[layer_or_step_or_tick] == 0:
            continue  # we have encountered a layer that has no range, and also no scanner.  Ignore, and continue to
            # next iteration

        # the crux of Part 2 is we add delay to simulate a waiting period of length <delay> picoseconds.
        if ((delay + layer_or_step_or_tick) % ((firewall[layer_or_step_or_tick] - 1) * 2)) == 0:
            delay += 1  # if we have been caught by a scanner, we need to increment delay, break, and try out the new
            # delay value.
            break  # detected by scanner.  Go back to beginning of for loop and try a different delay.
    else:
        break
print(str(delay) + " is the shortest amount in picoseconds to delay the packet by to remain undetected from scanners.")
# Answer is 3830344.
