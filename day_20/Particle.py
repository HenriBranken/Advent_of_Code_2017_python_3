class Particle(object):

    # static variables pa, pb, and pc, representing the position of the origin (x=0, y=0, z=0)
    pa, pb, pc = 0, 0, 0

    def __init__(self, id_num, px, py, pz, vx, vy, vz, ax, ay, az):
        self.id_num = id_num
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.__ax = ax
        self.__ay = ay
        self.__az = az
        self.manhat = self.get_manhattan_dist()
        self.__a_state_x, self.__a_state_y, self.__a_state_z = self.get_signs(self.__ax, self.__ay, self.__az)
        self.v_state_x, self.v_state_y, self.v_state_z = self.get_signs(self.vx, self.vy, self.vz)
        self.p_state_x, self.p_state_y, self.p_state_z = self.get_signs(self.px, self.py, self.pz)
        self.correct_initial_signs()  # afterwards a_states are never computed again.  They remain fixed.
        # acceleration influences velocity and position, but not vice versa.
        # alternatively, if the acceleration is 0, then velocity influences position, but not vice versa.
        # lastly, if both acceleration and velocity are both zero, then position remains fixed at its initial
        # configuration.
        self.condition = self.comparison()

    # return the current (x, y, z) position
    def get_position(self):
        return self.px, self.py, self.pz

    # return the current (vx, vy, vz) velocity
    def get_velocity(self):
        return self.vx, self.vy, self.vz

    # return the current (ax, ay, az) acceleration, which should remain fixed throughout the entire computation
    def get_acceleration(self):
        return self.__ax, self.__ay, self.__az

    # return the signs (+ or - or None if 0) of the kinematic (x, y, z) tuple passed to the get_signs method.
    @staticmethod
    def get_signs(kinx, kiny, kinz):
        if kinx == 0:
            pref_x = None
        elif kinx < 0:
            pref_x = "negative"
        else:
            pref_x = "positive"
        if kiny == 0:
            pref_y = None
        elif kiny < 0:
            pref_y = "negative"
        else:
            pref_y = "positive"
        if kinz == 0:
            pref_z = None
        elif kinz < 0:
            pref_z = "negative"
        else:
            pref_z = "positive"
        return pref_x, pref_y, pref_z

    # get the manhattan distance from the current position of the particle to the origin (x=0, y=0, z=0).
    # Notice that we are only interested in the "absolute" value of the distance.
    def get_manhattan_dist(self):
        dist = int(abs(self.px - Particle.pa) + abs(self.py - Particle.pb) + abs(self.pz - Particle.pc))
        return dist

    # determine the initial signs of the initial kinematic configuration for the particle.
    def correct_initial_signs(self):
        if (self.__a_state_x is None) and (self.v_state_x is None):
            self.p_state_x = None
        if (self.__a_state_x is None) and (self.v_state_x == "positive"):
            self.__a_state_x = "positive"
        if (self.__a_state_x is None) and (self.v_state_x == "negative"):
            self.__a_state_x = "negative"

        if (self.__a_state_y is None) and (self.v_state_y is None):
            self.p_state_y = None
        if (self.__a_state_y is None) and (self.v_state_y == "positive"):
            self.__a_state_y = "positive"
        if (self.__a_state_y is None) and (self.v_state_y == "negative"):
            self.__a_state_y = "negative"

        if (self.__a_state_z is None) and (self.v_state_z is None):
            self.p_state_z = None
        if (self.__a_state_z is None) and (self.v_state_z == "positive"):
            self.__a_state_z = "positive"
        if (self.__a_state_z is None) and (self.v_state_z == "negative"):
            self.__a_state_z = "negative"

    # After the particle has propagated one time tick, determine what the new signs from the updated kinematic
    # configuration.
    def update_signs(self):
        if (self.__a_state_x is None) and (self.v_state_x is None):
            self.p_state_x = None
        else:
            if self.vx < 0:
                self.v_state_x = "negative"
            elif self.vx == 0:
                self.v_state_x = "zero"
            else:
                self.v_state_x = "positive"
            if self.px < 0:
                self.p_state_x = "negative"
            elif self.px == 0:
                self.p_state_x = "zero"
            else:
                self.p_state_x = "positive"

        if (self.__a_state_y is None) and (self.v_state_y is None):
            self.p_state_y = None
        else:
            if self.vy < 0:
                self.v_state_y = "negative"
            elif self.vy == 0:
                self.v_state_y = "zero"
            else:
                self.v_state_y = "positive"
            if self.py < 0:
                self.p_state_y = "negative"
            elif self.py == 0:
                self.p_state_y = "zero"
            else:
                self.p_state_y = "positive"

        if (self.__a_state_z is None) and (self.v_state_z is None):
            self.p_state_z = None
        else:
            if self.vz < 0:
                self.v_state_z = "negative"
            elif self.vz == 0:
                self.v_state_z = "zero"
            else:
                self.v_state_z = "positive"
            if self.pz < 0:
                self.p_state_z = "negative"
            elif self.pz == 0:
                self.p_state_z = "zero"
            else:
                self.p_state_z = "positive"

    # evaluate whether the signs of the kinematic configuration align.
    # That is, whether (px, vx, ax), (py, vy, ay), (pz, vz, az) align individually and align as a whole.
    def comparison(self):
        if (self.__a_state_x is None) and (self.v_state_x is None):
            self.p_state_x = None
        if (self.__a_state_x == self.v_state_x) and (self.__a_state_x == self.p_state_x):
            cond_x = True
        else:
            return 0

        if (self.__a_state_y is None) and (self.v_state_y is None):
            self.p_state_y = None
        if (self.__a_state_y == self.v_state_y) and (self.__a_state_y == self.p_state_y):
            cond_y = True
        else:
            return 0

        if (self.__a_state_z is None) and (self.v_state_z is None):
            self.p_state_z = None
        if (self.__a_state_z == self.v_state_z) and (self.__a_state_z == self.p_state_z):
            cond_z = True
        else:
            return 0

        if cond_x and cond_y and cond_z:
            return 1
        else:
            return 0

    # Propagate the particle one time tick.
    def propagate(self):
        self.vx += self.__ax
        self.vy += self.__ay
        self.vz += self.__az
        self.px += self.vx
        self.py += self.vy
        self.pz += self.vz
        self.manhat = self.get_manhattan_dist()
        self.update_signs()
        self.condition = self.comparison()
