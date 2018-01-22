def read_file_input(filename):  # reading in the puzzle input.
    assembly = []
    f = open(filename, "r")
    for line in f.readlines():
        line = line.rstrip().split()
        instruction = line[0]
        try:
            x = int(line[1])
        except ValueError:
            x = line[1]
        try:
            y = int(line[2])
        except ValueError:
            y = line[2]
        assembly.append([instruction, x, y])
    f.close()
    return assembly


# This class object is a modification of the Singer.py object from Day 18.  Refer to folder day_18.
class Coprocessor(object):

    def __init__(self, filename, name, a_value):
        self.assembly = read_file_input(filename=filename)
        self.curr_ind_bounds = [0, len(self.assembly) - 1]
        self.my_dict = {"a": a_value, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}
        self.status = "Active"
        self.curr_ind = 0  # the starting position
        self.num_muls = 0
        self.name = name

    def __str__(self):
        rep = self.name + ".instruct = " + str(self.assembly[self.curr_ind]) + ".  "
        rep += self.name + ".my_dict = " + str(self.my_dict) + "."
        return rep

    # sets the register X equal to the value of Y.
    def setting(self, instruction):
        x, y = instruction[1], instruction[2]
        if type(y) == str:
            try:
                y_val = self.my_dict[y]
            except KeyError:
                self.my_dict[y] = 0
                y_val = 0
        else:
            y_val = y
        self.my_dict[x] = y_val
        self.curr_ind += 1

    # decreases register X by the value of Y.
    def subtract(self, instruction):
        x, y = instruction[1], instruction[2]
        try:
            x_val = self.my_dict[x]
        except KeyError:
            self.my_dict[x] = 0
            x_val = 0
        if type(y) == str:
            try:
                y_val = self.my_dict[y]
            except KeyError:
                self.my_dict[y] = 0
                y_val = 0
        else:
            y_val = y
        self.my_dict[x] = x_val - y_val
        self.curr_ind += 1

    # sets register X equal to the result of multiplying the value contained in register X by the value of Y.
    def multiply(self, instruction):
        x, y = instruction[1], instruction[2]
        try:
            x_val = self.my_dict[x]
        except KeyError:
            self.my_dict[x] = 0
            x_val = 0
        if type(y) == str:
            try:
                y_val = self.my_dict[y]
            except KeyError:
                self.my_dict[y] = 0
                y_val = 0
        else:
            y_val = y
        self.my_dict[x] = x_val * y_val
        self.curr_ind += 1
        self.num_muls += 1

    # jumps with an offset of the value of Y, but only if the value of X is not zero.
    # Anb offset of 2 skips dthe next instruction, an offset of -1 jumps to the previous instruction, and so on.
    def jumps(self, instruction):
        x, y = instruction[1], instruction[2]
        if type(x) == str:
            try:
                x_val = self.my_dict[x]
            except KeyError:
                self.my_dict[x] = 0
                x_val = 0
        else:
            x_val = x
        if type(y) == str:
            try:
                y_val = self.my_dict[y]
            except KeyError:
                self.my_dict[y] = 0
                y_val = 0
        else:
            y_val = y
        if abs(x_val) > 0:
            self.curr_ind += y_val
        else:
            self.curr_ind += 1  # the jump instruction is skipped

    # this function checks whether or not the program has continued / jumped outside the acceptable range of index
    # values.
    def index_checker(self):
        if (self.curr_ind < self.curr_ind_bounds[0]) or (self.curr_ind > self.curr_ind_bounds[1]):
            self.status = "Terminated"

    def try_next_iteration(self):
        instruct = self.assembly[self.curr_ind]

        if self.status == "Active":
            if instruct[0] == "set":
                self.setting(instruct)
            elif instruct[0] == "sub":
                self.subtract(instruct)
            elif instruct[0] == "mul":
                self.multiply(instruct)
            else:
                self.jumps(instruct)

        self.index_checker()
