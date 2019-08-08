from random import randint as r
from .figure import Figure


START = 0
END = 360

class Circle(Figure):
    def draw(self):
        pts = [
            (-self.size // 2, -self.size // 2),
            (self.size // 2, -self.size // 2),
            (self.size // 2, self.size // 2),
            (-self.size // 2, self.size // 2),
        ]

        pts = self.transpose_points(self.midpt[0], self.midpt[1], *pts)

        self.drawer.arc((*pts[0], *pts[2]), start=START, end=END, fill=self.filler)
        self.drawer.arc((*pts[1], *pts[3]), start=START, end=END, fill=self.filler)
