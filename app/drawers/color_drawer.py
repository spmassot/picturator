import math

from tqdm import tqdm
from PIL import Image, ImageDraw
from random import randint as r, choice as c

from effecters.tubifier import Tubifier
from figures.circle import Circle
from figures.square import Square

from fillers.gradient_filler import GradientFiller
from fillers.random_filler import RandomFiller

from drawers.drawer import Drawer


class ColorDrawer(Drawer):
    def __init__(self):
        self.img = Image.new('RGB', (1000, 1000), color=(255, 255, 255))
        self.drawer = ImageDraw.Draw(self.img)

    def draw(self):
        for i in tqdm(range(10)):
            x = r(-500, 500) + 500
            y = r(-500, 500) + 500
            sz = r(-100, 100) + 100

            morph_dir = (r(-1, 1), r(-1, 1))
            growth = r(-10, 10)
            morph_tail = r(5, 100)
            morph_rotation = r(0, 360)

            if r(1, 10) > 5:
                c = Circle(
                    drawer=self.drawer,
                    fill_generator=GradientFiller(
                        (0, 127, 127),
                        (255, 0, 80),
                        (99, 128, 0),
                        rate=10,
                    ),
                    midpt=(x, y),
                    size=sz,
                    rotation=r(0, 360),
                )
                t = Tubifier(c)
                t.morph(
                    morph_dir[0],
                    morph_dir[1],
                    lambda x, y: math.sin(math.radians(y)) * 300,
                    morph_tail,
                    lambda x: x + morph_rotation
                )
            else:
                s = Square(
                    drawer=self.drawer,
                    fill_generator=RandomFiller((0, 255), (0, 255), (0, 255)),
                    midpt=(x, y),
                    size=sz,
                    rotation=r(0, 360),
                )
                t = Tubifier(s)
                t.morph(
                    morph_dir[0],
                    morph_dir[1],
                    lambda x, y: math.sin(math.radians(y)) * 300,
                    morph_tail,
                    lambda x: x + morph_rotation
                )
        self.save()
