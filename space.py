import matplotlib.pyplot as plt
import numpy as np


class Space(object):
    def __init__(self, rmax, zmax, h):
        self.rmax = rmax
        self.zmax = zmax
        self.h = h
        self.space = {}
        self.__changeable = []
        self.__set_space()

    def set_point(self, r, z, val, is_changeable=True):
        # Check if the point is changeable:
        if (r, z) in self.space:
            if not self.space[(r, z)]["is_changeable"]:
                raise Exception(f"The point {(r,z)} is not changeable!")

        self.space[(r, z)] = {"potential": val,
                              "is_changeable": is_changeable}
        if is_changeable:
            self.__changeable.append((r, z))

    def get_point(self, r, z):
        if (r, z) not in self.space:
            raise KeyError(f"{(r, z)} is not a in the space")
        return self.space[(r, z)]['potential']

    def __set_space(self):
        for i in np.arange(0, self.rmax, self.h):
            for j in np.arange(0, self.zmax, self.h):
                self.set_point(i, j, 0)

    def get_changeable(self):
        return self.__changeable

    def __convert_space_into_matrix(self):
        matrix = [[0 for i in range(int(self.rmax / self.h))] for i in range(int(self.zmax / self.h))]
        for r, z in self.space:
            r_i = int(r * self.h)
            z_i = int(z * self.h)
            matrix[r_i][z_i] = self.get_point(r, z)
        return matrix

    def create_map(self):
        matrix = self.__convert_space_into_matrix()
        plt.imshow(matrix, cmap='hot', interpolation='nearest')
        plt.show()


#
# if __name__ == '__main__':
#     s = Space(rmax=8, zmax=14, h=0.1)
#     s.set_point(2, 2, 2, is_changeable=False)
#     s.set_point(2, 2, 3)
#     print(s.get_point(2, 2))
