from .effecter import Effecter
from random import randint as r


class Patternizer(Effecter):
    def morph(self, spread, wiggles):
        s = spread * self.target.size
        o = self.target.midpt
        mp_array = self.make_array(o, s, r(2, 10), r(2, 10))
        for i in range(wiggles):
            for x in mp_array:
                for y in x:
                    self.target.midpt = y
                    self.target.size = self.target.size + r(*self.get_wiggle_range())
                    self.target.draw()

    def make_array(self, o, s, x_d, y_d):
        mp_array = []
        for i in range(y_d):
            row = []
            for j in range(x_d):
                row.append((o[0] + s * j, o[1] + s * i))
            mp_array.append(row)
        return mp_array

    def get_wiggle_range(self):
        m = int(self.target.size * .1)
        return (-m, m)
