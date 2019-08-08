import math


class Figure:
    def __init__(self, drawer, fill_generator, midpt, size, rotation):
        self.drawer = drawer
        self._fill_generator = fill_generator.fill()
        self.midpt = midpt
        self.size = size
        self.rotation = rotation

    @property
    def filler(self):
        fill = next(self._fill_generator)
        return fill

    def draw(self, *args, **kwargs):
        return NotImplemented

    def rotate_points(self, rot, *pts):
        rads = math.radians(rot)

        new_pts = []
        for pt in pts:
            x = pt[0] * math.cos(rads) - pt[1] * math.sin(rads)
            y = pt[1] * math.cos(rads) + pt[0] * math.sin(rads)
            new_pts.append((x, y))
        return new_pts

    def transpose_points(self, x, y, *pts):
        new_pts = []
        for pt in pts:
            new_pts.append((pt[0] + x, pt[1] + y))
        return new_pts
