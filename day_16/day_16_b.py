# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 16:  Permutation Promenade, Part 2                                              |
# | Website: https://adventofcode.com/2017/day/16                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

ref = "abcdefghijklmnop"
filename = "day_16_input.txt"  # Your puzzle input.
f = open(filename, "r")
line = f.readline().rstrip()
dance_moves = line.split(",")
f.close()


# makes X programs move from the end to the front, but maintain their order otherwise.
def spin(input_programs, move):
    n_programs = int(move[1:])
    length = len(input_programs)
    l_sublist, r_sublist = input_programs[0: length - n_programs], input_programs[length - n_programs:]
    return r_sublist + l_sublist


# makes the programs at positions A and B swap places.
def exchange(input_programs, move):
    positions = move[1:].split("/")
    position_a, position_b = int(positions[0]), int(positions[1])
    if position_a > position_b:
        position_a, position_b = position_b, position_a  # swap the positions
    program_at_a, program_at_b = input_programs[position_a], input_programs[position_b]
    comp_1 = input_programs[0: position_a] + program_at_b
    comp_2 = input_programs[position_a + 1: position_b]
    comp_3 = program_at_a + input_programs[position_b + 1:]
    return comp_1 + comp_2 + comp_3


# makes programs named A and B swap places.
def partner(input_programs, move):
    progs = move[1:].split("/")
    program_a, program_b = progs[0], progs[1]
    program_a_pos, program_b_pos = input_programs.index(program_a), input_programs.index(program_b)
    if program_a_pos > program_b_pos:
        program_a_pos, program_b_pos = program_b_pos, program_a_pos
        program_a, program_b = program_b, program_a
    comp_1 = input_programs[0: program_a_pos] + program_b
    comp_2 = input_programs[program_a_pos + 1: program_b_pos]
    comp_3 = program_a + input_programs[program_b_pos + 1:]
    return comp_1 + comp_2 + comp_3


# one dancing round in which all the moves in dance_moves have been executed exactly once in consecutive order.
def one_round(input_programs, moves=dance_moves):
    for move in moves:
        if move[0] == "s":
            input_programs = spin(input_programs, move)
        elif move[0] == "x":
            input_programs = exchange(input_programs, move)
        elif move[0] == "p":
            input_programs = partner(input_programs, move)
    return input_programs


programs = ref
i = 0
while True:
    programs = one_round(programs)
    i += 1
    if programs == "abcdefghijklmnop":  # the sequence of programs have reverted to their original order.
        print("Number of iterations for a loop back to the original state = " + str(i) + ".")
        break

loop_cycle = i  # the size of the loop for programs to evolve from abcdefghijklmnop --> abcdefghijklmnop.
remainder = 10**9 % loop_cycle  # how many dance rounds remain in total?
print("The remainder is: " + str(remainder) + ".")

programs = "abcdefghijklmnop"
for i in range(remainder):  # execute the remainder of dancing rounds.
    programs = one_round(programs)

print("Programs after 10**9 cycles = " + programs + ".")
# Answer is ejkflpgnamhdcboi.
