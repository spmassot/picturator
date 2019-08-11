import math

from drawers.color_drawer import ColorDrawer
from effecters.tubifier import Tubifier
from figures.random_walk import RandomWalk
from fillers.gradient_filler import GradientFiller
from random import randint as r
from tqdm import tqdm


class RandomDrawerA(ColorDrawer):
    def draw(self):
        for i in tqdm(range(60)):
            x = r(-self.w // 2, self.w // 2) + self.w // 2
            y = r(-self.h // 2, self.h // 2) + self.h // 2
            sz = max(r(-self.w // 10, self.w // 10) + self.w // 10, 1)

            morph_dir = (r(-10, 10), r(-10, 10))
            growth = r(-10, 10)
            morph_tail = r(5, 100)
            morph_rotation = r(0, 360)

            s = RandomWalk(
                drawer=self.drawer,
                fill_generator=GradientFiller(
                    self.random_color(),
                    self.random_color(),
                    self.random_color(),
                    rate=10
                ),
                midpt=(x, y),
                size=sz,
                rotation=r(0, 360),
            )
            s.prep()
            t = Tubifier(s)
            t.morph(
                morph_dir[0],
                morph_dir[1],
                lambda x, y: math.sin(math.radians(y)) * 300,
                morph_tail,
                lambda x: x + morph_rotation
            )
        self.save()
