# .-------------------------------------------------------------------------------------.
# | Puzzle Author:  Eric Wastl; http://was.tl/                                          |
# | Python 3 Solution Author:  Henri Branken                                            |
# | Date:  December 2017                                                                |
# | Event:  Advent of Code 2017                                                         |
# | Day 18:  Duet, Part 1                                                               |
# | Website: https://adventofcode.com/2017/day/18                                       |
# |                                                                                     |
# | This does not necessarily represent the most optimized solution to the problem, but |
# | simply the solution that I came up with at the time using Python 3.                 |
# '-------------------------------------------------------------------------------------'

filename = "day_18_input.txt"  # Your puzzle input

assembly = []
f = open(filename, "r")
for line in f.readlines():
    line = line.rstrip().split()
    ins = line[0]
    if ins == "rcv":
        try:
            ex = int(line[1])
        except ValueError:
            ex = line[1]
        assembly.append([ins, ex])
    elif ins == "snd":
        try:
            ex = int(line[1])
        except ValueError:
            ex = line[1]
        assembly.append([ins, ex])
    else:
        try:
            ex = int(line[1])
        except ValueError:
            ex = line[1]
        try:
            why = int(line[2])
        except ValueError:
            why = line[2]
        assembly.append([ins, ex, why])
f.close()  # assembly is a list of lists that contains the assembly instructions in the puzzle input

i_bounds = [0, len(assembly) - 1]

my_dict = dict()
sounds = []
recover = []


# play a sound with a frequency equal to the value of X
def sound(instruction):
    global my_dict, sounds
    x = instruction[1]
    if type(x) == str:
        try:
            x_val = my_dict[x]
        except KeyError:
            my_dict[x] = 0
            x_val = 0
    else:
        x_val = x
    if abs(x_val) > 0:
        sounds.append(x_val)


# sets the register X to the value of Y
def setting(instruction):
    global my_dict
    x, y = instruction[1], instruction[2]
    if type(y) == str:
        try:
            y_val = my_dict[y]
        except KeyError:
            my_dict[y] = 0
            y_val = 0
    else:
        y_val = y
    my_dict[x] = y_val


# increases register X by the value of Y
def increasing(instruction):
    global my_dict
    x, y = instruction[1], instruction[2]
    try:
        x_val = my_dict[x]
    except KeyError:
        my_dict[x] = 0
        x_val = 0
    if type(y) == str:
        try:
            y_val = my_dict[y]
        except KeyError:
            my_dict[y] = 0
            y_val = 0
    else:
        y_val = y
    my_dict[x] = x_val + y_val


# sets register X to the result of multiplying the value contained in register X by the value of Y
def multiply(instruction):
    global my_dict
    x, y = instruction[1], instruction[2]
    try:
        x_val = my_dict[x]
    except KeyError:
        my_dict[x] = 0
        x_val = 0
    if type(y) == str:
        try:
            y_val = my_dict[y]
        except KeyError:
            my_dict[y] = 0
            y_val = 0
    else:
        y_val = y
    my_dict[x] = x_val * y_val
    return


# sets register X to the remainder of dividing the value contained in register X by the value of Y
# that is, it sets X to the result of X modulo Y
def modulo(instruction):
    global my_dict
    x, y = instruction[1], instruction[2]
    try:
        x_val = my_dict[x]
    except KeyError:
        my_dict[x] = 0
        x_val = 0
    if type(y) == str:
        try:
            y_val = my_dict[y]
        except KeyError:
            my_dict[y] = 0
            y_val = 0
    else:
        y_val = y
    my_dict[x] = x_val % y_val


# recovers the frequency of the last sound played, but only when the value of X is not zero.
# if X is zero, the command does nothing.
def recovers(instruction):
    global my_dict, sounds
    x = instruction[1]
    if type(x) == str:
        try:
            x_val = my_dict[x]
        except KeyError:
            my_dict[x] = 0
            x_val = 0
    else:
        x_val = x
    if int(x_val) != 0 and (len(sounds) > 0):
        return sounds[-1]
    else:
        return None


# jumps with an offset of the value of Y, but only if the value of X is greater than zero.
# An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.
def jumps(instruction):
    global my_dict, sounds
    x, y = instruction[1], instruction[2]
    if type(x) == str:
        try:
            x_val = my_dict[x]
        except KeyError:
            my_dict[x] = 0
            x_val = 0
    else:
        x_val = x
    if type(y) == str:
        try:
            y_val = my_dict[y]
        except KeyError:
            my_dict[y] = 0
            y_val = 0
    else:
        y_val = y
    if x_val > 0:
        return y_val
    else:
        return None


curr_ind = 0
while True:
    instruct = assembly[curr_ind]
    if instruct[0] == "snd":
        sound(instruct)
        curr_ind += 1
    elif instruct[0] == "set":
        setting(instruct)
        curr_ind += 1
    elif instruct[0] == "add":
        increasing(instruct)
        curr_ind += 1
    elif instruct[0] == "mul":
        multiply(instruct)
        curr_ind += 1
    elif instruct[0] == "mod":
        modulo(instruct)
        curr_ind += 1
    elif instruct[0] == "rcv":
        freq = recovers(instruct)
        if freq is None:
            curr_ind += 1
        elif type(freq) == int and (abs(freq) > 0):
            recover.append(freq)
            break
    else:
        offset = jumps(instruct)
        if offset is None:
            curr_ind += 1
        else:  # Continuing (or jumping) off either end of the program terminates it.
            curr_ind += offset
            if (curr_ind < i_bounds[0]) or (curr_ind > i_bounds[1]):
                break

print(str(recover[0]) + " is the value of the recovered frequency.")
# Answer is 7071.
