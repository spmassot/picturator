from .figure import Figure


class Square(Figure):
    def draw(self):
        pts = [
            (-self.size // 2, -self.size // 2),
            (self.size // 2, -self.size // 2),
            (self.size // 2, self.size // 2),
            (-self.size // 2, self.size // 2),
            (-self.size // 2, -self.size // 2),
        ]

        pts = self.rotate_points(self.rotation, *pts)
        pts = self.transpose_points(self.midpt[0], self.midpt[1], *pts)

        self.drawer.line((*pts,), fill=self.filler)
