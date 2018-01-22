# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 24:  Electromagnetic Moat, Part 1                                               |
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


# The key insight to this problem is the use of a recursive function that recursively delves into all the possible
# connections of the components to form various bridges.  Only the strength of the strongest bridge, however, survives.
def attach(remaining, previous, strength):
    global strongest

    for component in remaining:  # it appears the recursive method breaks when all of the components in the inventory
        # have become exhausted.  I.e. when all possible combinations have been considered.
        if component[0] == previous:  # we should not flip the order of the component part, but keep it as it is.
            adjacent = component[1]  # the new open, unconnected side that has the potential of getting connected
            # to another component part.
            re = remaining.copy()  # make a copy of the remaining parts that have not been used up until this point.
            re.remove(component)  # Accordingly remove the component that is under consideration in the if condition.
            st = strength
            st += component[0] + component[1]  # Update the strength by accruing the strength of the component under
            # consideration in the if condition to the cumulative strength.

            if st > strongest:  # We are only interested in the strongest possible bridge.  Hence if st > strongest,
                # we update the value of the strongest possible bridge up until this point.
                strongest = st

            attach(re, adjacent, st)  # recursively call the attach method again.
        elif component[1] == previous:  # we should flip the order of the component part.
            adjacent = component[0]
            re = remaining.copy()
            re.remove(component)
            st = strength
            st += component[0] + component[1]

            if st > strongest:
                strongest = st

            attach(re, adjacent, st)


attach(inventory, 0, 0)
print(str(strongest) + " is the strength of the strongest bridge you can make with the components available.")
# Answer is 1511.
