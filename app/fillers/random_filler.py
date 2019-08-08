import math

from .filler import Filler
from random import randint as r


class RandomFiller(Filler):
    def __init__(self, R, G, B):
        self.R, self.B, self.G = R, G, B

    def fill(self):
        while True:
            yield (r(*self.R), r(*self.B), r(*self.G))
