from .effecter import Effecter


class Tubifier(Effecter):
    def morph(self, x_offset, y_offset, growth, length, rotation):
        for i in range(length):
            self.target.midpt = (
                self.target.midpt[0] + x_offset,
                self.target.midpt[1] + y_offset
            )
            self.target.size = growth(self.target.size, i)
            self.target.rotation = rotation(self.target.rotation)
            self.target.draw()
