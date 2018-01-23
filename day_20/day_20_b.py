# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | GitHub Repository: https://github.com/HenriBranken/Advent_of_Code_2017_python_3     |
# | My email address:  henri dot branken777 at gmail dot com                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 20:  Particle Swarm, Part 2                                                     |
# | Website: https://adventofcode.com/2017/day/20                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

import numpy as np
from Particle import *

f_name = "day_20_input.txt"  # Your puzzle input.


# retrieve the kinematic information stored between the <> characters.
# The kinematic information relates to either initial position, velocity, or acceleration of a particle.
def get_between(s, begin_char="<", end_char=">"):
    s = s[s.index(begin_char) + 1: s.index(end_char)]
    s = s.split(",")
    for index, element in enumerate(s):
        s[index] = int(element)
    return s


# returns a list of position, velocity and acceleration of a particle.
def get_kinematics(s):
    p_pos, v_pos, a_pos = s.index("p"), s.index("v"), s.index("a")
    p_list = get_between(s[p_pos: v_pos])
    v_list = get_between(s[v_pos: a_pos])
    a_list = get_between(s[a_pos:])
    return list([p_list[0], p_list[1], p_list[2], v_list[0], v_list[1], v_list[2], a_list[0], a_list[1], a_list[2]])


i = 0
kinematics = np.zeros([1, 10], dtype=int)  # row of size 1, and columns of size 10, all zero integers.
f = open(f_name, "r")
for line in f.readlines():
    if line in ["", " ", "\n"]:
        break
    line = line.rstrip("\n")
    k = get_kinematics(line)
    k.insert(0, i)  # insert at the very start of the list the index number (i.e. the particle ID)
    if i == 0:
        kinematics[0:] = k  # the first row of the numpy array.  (currently still nothing to be vstacked.)
    else:
        kinematics = np.vstack((kinematics, k))  # once we have at least one row, we can start vstacking.
    i += 1
f.close()

n_particles = kinematics.shape[0]  # n_particles = number of rows of the kinematics array.

gpu_particles = []  # gpu_particles is a list of Particle objects reflecting the information stored in the
# (initial) kinematics array.
for j in range(n_particles):
    info = list(kinematics[j, :])
    p = Particle(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9])
    gpu_particles.append(p)

# p.condition checks whether the signs of position, velocity and acceleration of a particle "align".
# In the most trivial case: if p, v, and a are all positive (or all negative), then p.condition = True.
# As another example, if a = 0, v = positive, p = positive, then p.condition = True.
# Alternatively, if a = 0, v = negative, p = negative, then also p.condition = True.
# However, if, for example, a = 0, v = positive, p = negative, then p.condition = False.
# Similarly, if a = 0, v = negative, p = positive, then also p.condition = False.
# As a last illustration, if a = 0, v = 0, p = negative/positive, then p.condition = True.
# See the comparison(self) method in the Particle.py class for all the (in)valid cases.
# If condition == n_particles, then we can determine the particle that will always remain the closest to (0, 0, 0) in
# the long-term.
# The logic behind condition == n_particles, is that if all particles move in their final directions as dictated by
# their acceleration or velocity, then the swarm of particles is in a state of constantly expanding from the centre
# (0, 0, 0).
ind = 0
while True:
    n_particles = len(gpu_particles)
    condition = 0
    positions = []
    # the for-loop represents one propagation step for all the particles stored in gpu-particles.
    for p in gpu_particles:
        p.propagate()
        condition += p.condition
        positions.append(p.get_position())
    set_positions = list(set(positions))
    pos_to_be_removed = []
    for elem in set_positions:
        if positions.count(elem) > 1:  # positions that are duplicated indicate particles at that position to be removed
            pos_to_be_removed.append(elem)

    j = 0
    while True:
        if gpu_particles[j].get_position() in pos_to_be_removed:  # be careful not to increment the j index in this if
            # clause.  Otherwise you end up skipping particles to be removed.
            gpu_particles.remove(gpu_particles[j])
        else:
            j += 1
            if j > (len(gpu_particles) - 1):  # j is greater than the maximum index.
                break

    ind += 1
    if condition == n_particles:
        break

print("Number of particles available is: " + str(len(gpu_particles)) + ".")
# Answer is 567.
