class Space:
    def __init__(self, rmax, zmax, h):
        self.rmax = rmax
        self.zmax = zmax
        self.h = h

    def set_value(self, r, z, value, is_changeable):
        pass

    def get_value(self, r, z):
        return 0

    def get_changeable_coordinates(self):
        return [[1, 1]]

    def copy(self):
        return Space()
