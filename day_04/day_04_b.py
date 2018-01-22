# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 4: High-Entropy Passphrases, Part 2                                             |
# | Website: https://adventofcode.com/2017/day/4                                        |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

f = open("day_04_input.txt", "r")  # Your puzzle input
my_list = []
for line in f.readlines():
    if line in ["", " ", "\n"]:
        break
    line = line.rstrip()
    line = line.split()
    my_list.append(line)
f.close()


def tester(the_list):
    j = 0
    while j < len(the_list):  # j represents the index of the passphrase against which the remaining passphrases are
        # checked to determine if an anagram is present.
        for i, the_set in enumerate(the_list):
            if i != j and (j < i <= len(the_list) - 1):  # we don't want to test a passphrase against itself.  We also
                # need to ensure that i remains within the appropriate bounds.
                if the_list[j] == the_list[i]:  # we have found a matching anagram.  Hence invalid passphrase provided.
                    # Break, and return False.
                    return 0
        j += 1
    return 1


cumulative = 0

for passphrase in my_list:
    if len(set(passphrase)) != len(passphrase):  # do not bother to test for anagrams because duplicate words are
        # already present.
        continue
    else:
        my_sets = [set(word) for word in passphrase]
        cumulative += tester(my_sets)  # tester function evaluates whether there is a word that is an anagram of another
        # in my_sets.  If there is an anagram present, then we add nothing to cumulative.  Otherwise we increment
        # cumulative with 1.
print(str(cumulative) + " passphrases are valid.")
# Answer is 223.
