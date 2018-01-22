# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 4: High-Entropy Passphrases, Part 1                                             |
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

# set(passphrase) removes any duplicates from passphrase.
# if len(set(passphrase)) == len(passphrase), we have found a valid passphrase without no duplicate words.
cumulative = 0
for passphrase in my_list:
    if len(set(passphrase)) == len(passphrase):
        cumulative += 1

print(str(cumulative) + " passphrases are valid.")
# Answer is 451.
