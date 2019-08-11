import math

from drawers.color_drawer import ColorDrawer
from effecters.patternizer import Patternizer
from figures.circle import Circle
from fillers.wiggle_filler import WiggleFiller
from random import randint as r
from tqdm import tqdm


class WiggleDrawerA(ColorDrawer):
    def draw(self):
        for i in tqdm(range(30)):
            x = r(-self.w // 2, self.w // 2) + self.w // 2
            y = r(-self.h // 2, self.h // 2) + self.h // 2
            sz = max(r(-self.w // 40, self.w // 40) + self.w // 100, 1)

            s = Circle(
                drawer=self.drawer,
                fill_generator=WiggleFiller(*self.random_color()),
                midpt=(x, y),
                size=sz,
                rotation=r(0, 360),
            )
            t = Patternizer(s)
            t.morph(2, 3)
        self.save()

