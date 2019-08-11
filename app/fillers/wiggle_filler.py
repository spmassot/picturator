from .filler import Filler
from random import randint as r


class WiggleFiller(Filler):
    def __init__(self, R, G, B):
        self.R, self.G, self.B = R, G, B

    def fill(self):
        while True:
            y = lambda x: x + r(-50, 50)
            yield (y(self.R), y(self.G), y(self.B))
