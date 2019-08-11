from drawers.drawer import Drawer
from PIL import Image, ImageDraw
from random import randint as r


class ColorDrawer(Drawer):
    def __init__(self, width):
        self.w = width
        self.h = int(self.w / (16 / 9))
        self.img = Image.new(
            'RGB',
            (self.w, self.h),
            color=self.random_color(),
        )
        self.drawer = ImageDraw.Draw(self.img)

    def random_color(self):
        return (r(0, 255), r(0, 255), r(0, 255))
