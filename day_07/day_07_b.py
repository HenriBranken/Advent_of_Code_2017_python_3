# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 7:  Recursive Circus, Part 2                                                    |
# | Website: https://adventofcode.com/2017/day/7                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

f_name = "day_07_input.txt"  # Your puzzle input.
sub_towers = dict()  # a dictionary of all the towers in the network.
weights = dict()  # a dictionary containing the weight information of the programs.
tops = list()  # the programs that are suspended at the very tops of the towers (the "leaves" of the network.)
f = open(f_name, "r")
for line in f.readlines():
    opening_bracket_i = line.index("(")
    closing_bracket_i = line.index(")")
    w = int(line[opening_bracket_i + 1: closing_bracket_i])
    name = line[0: opening_bracket_i - 1]
    weights[name] = w
    if "->" in line:
        sub_towers[name] = line[line.index(">") + 2:].rstrip("\n").split(", ")
    else:
        tops.append(name)
f.close()

supported = []
subs = []
for sub_tower, suspended in sub_towers.items():
    supported += suspended  # supported is a growing list of programs that are "suspended in the air"
    subs.append(sub_tower)  # subs is a growing list of all programs on which other programs balance.
for s in subs:  # loop over all the programs on which other programs balance.
    if s not in supported:  # this implies that s is the bottom-most program.
        bottom = s
        break
else:
    bottom = None


# get the total weight along a certain branch (tower)
def get_weights(program):
    if program not in sub_towers:  # if program is not in the keys of sub_towers.  i.e. if program is not a base-program
        # but a program suspended in the air.
        return weights[program]  # return the weight of the suspended program.
    elif program in sub_towers:  # elif program is a base program on which other programs balance.
        dummy = 0
        for child in sub_towers[program]:  # iterate through all the suspended programs / branches.
            dummy += get_weights(child)  # get the weight along a particular branch.  Accrue all weights to dummy.
        return weights[program] + dummy  # sum the weight of dummy to the weight of the base program.


# funelling out the erroneous program.
def deepen(branch):
    global offset
    print("CURRENT BRANCH PROGRAM IS:", branch + " with weight " + str(weights[branch]) + ".")
    sums_of_weights = []
    reference = []
    for p in sub_towers[branch]:  # iterate through the programs that balance on the base program referenced as branch.
        s_o_w = get_weights(p)  # get the weight along each branch
        print(p, s_o_w)
        reference.append((s_o_w, p))  # a list of tuples is populated containing the weight along a particular branch,
        # and the name of the branch.
        sums_of_weights.append(s_o_w)  # a list is populated containing the weight of a particular branch.
    print("-" * 55)
    counts = []
    for s_o_w in list(set(sums_of_weights)):  # get a list in which any duplicates in sums_of_weights have been removed.
        counts.append((sums_of_weights.count(s_o_w), s_o_w))  # counts is a growing list of tuples which contains
        # (the number of occurrences for a particular weight, the value for that weight).
    counts.sort()  # counts is sorted on the first index, the number of occurrences, in ascending order (small -> large)
    if len(counts) > 1:  # i.e. counts list contains at least 2 tuples.
        for s_o_w, p in reference:  # iterate over all the branch weights, and branch program names.
            if s_o_w == counts[0][1]:  # if weight value equals the overweight value, we have spotted the erroneous
                # branch
                wb = p
                break
        else:
            wb = None
        offset = counts[0][1] - counts[1][1]  # find the offset of the overweight value.
        deepen(wb)  # recursively look deeper in the erroneous branch to funnel out the faulty program.
    elif len(counts) == 1:  # i.e. the counts list only contains one tuple.  Meaning we have moved past the erroneous
        # program.
        print("THE ERRONEOUS PROGRAM IS: ", branch + ".")  # which is wb from the previous recursive iteration.
        print("THE WRONG WEIGHT IS: ", str(weights[branch]) + ".")
        print("THE OFFSET IS: ", str(offset) + ".")
        print("THE CORRECT WEIGHT SHOULD BE: ", str(weights[branch] - offset) + " (the puzzle answer).")
        print("*" * 55)


deepen(bottom)
# Answer is 391.
