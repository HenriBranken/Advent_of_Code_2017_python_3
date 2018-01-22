# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 18:  Duet, Part 2                                                               |
# | Website: https://adventofcode.com/2017/day/18                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

from Singer import *

f_name = "day_18_input.txt"  # Your puzzle input

# Each program also has its own program ID (one 0 and the other one 1); the register p should begin with this value.
program_0 = Singer(0, f_name, "program_0")
program_1 = Singer(1, f_name, "program_1")

program_0.partner(program_1)  # therefore, program_0 is configured to send messages to program_1.  Conversely, program_0
# receives messages from program_1.
program_1.partner(program_0)  # therefore, program_1 is configured to send messages to program_0.  Conversely, program_1
# receives messages from program_0.

while True:
    program_0.try_next_iteration()
    program_1.try_next_iteration()
    if (program_0.status == "Waiting") and (program_1.status == "Waiting"):  # the deadlock.  Both programs terminate.
        break
    elif program_1.status == "Terminated":  # we are interested in how many times program 1 sends a value, therefore
        # if program 1 has reached a status of Terminated, we can break the loop irrespective of the status of program 2
        break
    elif (program_0.status == "Terminated") and (program_1.status == "Waiting"):  # if program 0 has terminated while
        # program 1 is Waiting, program 1 will be waiting indefinitely.  Hence we break the while loop to output the
        # results.
        break
    elif (program_0.status == "Terminated") and (program_1.status == "Terminated"):  # when both programs have
        # terminated, we break the while loop.
        break

print(str(program_1.my_sends) + " times did program 1 send a value.")
# Answer is 8001.
