# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 24:  Electromagnetic Moat, Part 2                                               |
# | Website: https://adventofcode.com/2017/day/24                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# | Acknowledgement:  Thanks to Quint Daenen @                                          |
# | http://quint.ulyssis.be/content/AdventOfCode17/day24.py that shed some light to the |
# | solution of the puzzle.                                                             |
# '-------------------------------------------------------------------------------------'

fname = "day_24_input.txt"  # Your puzzle input.

inventory = []  # A list representing all the parts that are available at your side of the moat.
f = open(fname, "r")
for line in f.readlines():
    if line in ["", " ", "\n"]:
        break
    line = line.rstrip()
    left_right = line.split("/")
    left, right = int(left_right[0]), int(left_right[1])
    if left < right:
        inventory.append((left, right))
    else:
        inventory.append((right, left))
f.close()  # inventory is a list of ordered tuples (in ascending order) of all the components available at your side of
# the moat.

strongest = 0  # strongest is a placeholder to contain the strength of the strongest possible bridge during the
# recursive loop of the attach function.
my_list = [0, 0]  # a placeholder to contain the strength and length of the strongest and longest possible bridge in the
# recursive loop of the attach function.


# The key insight to this problem is the use of a recursive function that recursively delves into all the possible
# connections of the components to form various bridges.  Only the strength of the strongest bridge, and the length
# of the longest bridge, however, survives.
# The lines concerned with le and length is new in Part 2 of the puzzle.  le represents the length of the bridge.
# Ultimately, we are interested in the strength of the longest possible bridge that we can make.  If we can make
# multiple bridges of the longest length, then we simply pick the strongest one.
# The strength of the longest possible bridge is extracted by means of the second if conditions: if le >= my_list[0],
# etc.
# Notice also that in order to accommodate for bridge length, the attach function has an additional fourth argument,
# called length.
def attach(remaining, previous, strength, length):
    global strongest
    global my_list

    for component in remaining:  # The recursive method breaks when all of the components in the inventory have become
        # exhausted.  I.e. when all the possible combinations have been considered.
        if component[0] == previous:  # We should not flip the order of the component part, but keep it as it is.
            adjacent = component[1]  # The new open, unconnected side that has the potential of getting connected to
            # another component part.
            le = length
            le += 1  # update the length by incrementing it with 1.
            re = remaining.copy()  # make a copy of the remaining parts that have not been used up until this point.
            re.remove(component)  # Accordingly remove the component that is under consideration in the if condition.
            st = strength
            st += component[0] + component[1]  # Update the strength by accruing the strength of the component under
            # consideration in the if condition to the cumulative strength.

            if st > strongest:  # We are only interested in the strongest possible bridge.  Hence if str > strongest,
                # we update the value of the strongest bridge up until this point.
                strongest = st

            if le >= my_list[0]:  # We are only interested in the longest and strongest possible bridge.  Therefore
                # we perform 2 if conditions to check whether we need to update the strength and length of the longest
                # and strongest possible bridge up until this point.
                if st > my_list[1]:
                    my_list = [le, st]

            attach(re, adjacent, st, le)  # recursively call the attach method again.
        elif component[1] == previous:  # we should flip the order of the component part.
            adjacent = component[0]
            le = length
            le += 1
            re = remaining.copy()
            re.remove(component)
            st = strength
            st += component[0] + component[1]

            if st > strongest:
                strongest = st

            if le >= my_list[0]:
                if st > my_list[1]:
                    my_list = [le, st]

            attach(re, adjacent, st, le)


attach(inventory, 0, 0, 0)
print(str(my_list[1]) + " is the strength of the longest bridge you can make.")
# Answer is 1471.
