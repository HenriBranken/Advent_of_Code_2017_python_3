def read_file_input(filename):
    assembly = list()
    f = open(filename, "r")
    for line in f.readlines():
        line = line.rstrip().split()
        instruction = line[0]
        if instruction == "rcv":
            try:
                x = int(line[1])
            except ValueError:
                x = line[1]
            assembly.append([instruction, x])
        elif instruction == "snd":
            try:
                x = int(line[1])
            except ValueError:
                x = line[1]
            assembly.append([instruction, x])
        else:
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


# As you congratulate yourself for a job well done in Part 1, you notice that the documentation has been on the back of
# the tablet this entire time.  While you actually got most of the instructions correct, there are a few key differences
# This assembly code is not about sound at all - it's meant to be run twice at the same time.
# Each running copy of the program has its own set of registers and follows the code independently - in fact, the
# programs don't even necessarily run at the same speed.  To coordinate, they use the send (snd) and receive (rcv)
# instructions.
class Singer(object):

    # Each program also has its own program ID (0 and the other 1).  The register p should begin with this value.
    def __init__(self, p_val, filename, name):
        self.assembly = read_file_input(filename=filename)
        self.curr_ind_bounds = [0, len(self.assembly) - 1]
        self.my_dict = dict()
        self.my_dict["p"] = p_val
        self.status = "Active"
        self.my_message_queue = list()
        self.curr_ind = 0  # the starting position
        self.my_sends = 0
        self.name = name

    def __str__(self):
        rep = self.name + ".instruct = " + str(self.assembly[self.curr_ind]) + ".  "
        rep += self.name + ".my_dict = " + str(self.my_dict) + "."
        return rep

    def partner(self, other_program):
        self.other_program = other_program

    # sets register X to the value of Y
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

    # increases register X by the value of Y
    def increasing(self, instruction):
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
        self.my_dict[x] = x_val + y_val
        self.curr_ind += 1

    # sets register X to the result of multiplying the value contained in register X by the value of Y
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

    # sets register X to the remainder of dividing the value contained in register X by the value of Y
    # that is, it sets X to the result of X modulo Y.
    def modulo(self, instruction):
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
        self.my_dict[x] = x_val % y_val
        self.curr_ind += 1

    # jumps with an offset of the value of Y, but only if the value of X is greater than zero.
    # an offset of 2 skips the next instruction, and offset of -1 jumps to the previous instruction, and so on.
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
        if x_val > 0:
            self.curr_ind += y_val
        elif x_val <= 0:
            self.curr_ind += 1  # the jump instruction is skipped
        else:
            pass

    # sends the value of X to the other program.  These values wait in a queue until that program is ready to receive
    # them.  Each program has its own message queue, so a program can never receive a message it sent.
    def send(self, other_program, instruction):
        x = instruction[1]
        if type(x) == str:
            try:
                x_val = self.my_dict[x]
            except KeyError:
                self.my_dict[x] = 0
                x_val = 0
        else:
            x_val = x
        other_program.my_message_queue.append(x_val)
        self.my_sends += 1
        self.curr_ind += 1

    # receives the next value and stores it in register X.  If no values are in the queue, the program waits for a
    # value to be sent to it.  Programs do not continue to the next instruction until they have received a value.
    # Values are reived in the order they are sent.
    def receive(self, instruction):
        """
        Receives the next value from self.my_message_queue (x_val), and stores x_val in register x.
        """
        x = instruction[1]  # this x is by this point definitely of type string
        if len(self.my_message_queue) > 0:
            x_val = self.my_message_queue.pop(0)
            self.my_dict[x] = x_val
            self.status = "Active"
            self.curr_ind += 1
        elif len(self.my_message_queue) == 0:
            self.status = "Waiting"

    def index_checker(self):
        if (self.curr_ind < self.curr_ind_bounds[0]) or (self.curr_ind > self.curr_ind_bounds[1]):
            self.status = "Terminated"

    def try_next_iteration(self):
        instruct = self.assembly[self.curr_ind]

        if self.status == "Active":
            if instruct[0] == "set":
                self.setting(instruct)
            elif instruct[0] == "add":
                self.increasing(instruct)
            elif instruct[0] == "mul":
                self.multiply(instruct)
            elif instruct[0] == "mod":
                self.modulo(instruct)
            elif instruct[0] == "jgz":
                self.jumps(instruct)
            elif instruct[0] == "snd":
                self.send(self.other_program, instruct)
            elif instruct[0] == "rcv":
                self.receive(instruct)

        elif self.status == "Waiting":
            if len(self.my_message_queue) == 0:  # Do nothing, and still wait
                pass
            elif len(self.my_message_queue) > 0:
                self.receive(instruct)

        elif self.status == "Terminated":
            pass

        self.index_checker()
