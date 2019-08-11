from .figure import Figure
from random import randint as rando


def r(a, b):
    if a < b:
        return rando(a, b)
    else:
        return rando(b, a)


class RandomWalk(Figure):
    def prep(self):
        pts = []
        lp = self.midpt
        sz = int(self.size)
        for i in range(r(20, 200)):
            if r(0, 3) > 2:
                if r(0, 3) > 2:
                    np = (
                        r(lp[0], lp[0] + sz),
                        r(lp[1], lp[1] + sz)
                    )
                else:
                    np = (
                        r(lp[0], lp[0] - sz),
                        r(lp[1], lp[1] + sz)
                    )
            else:
                if r(0, 4) > 2:
                    np = (
                        r(lp[0], lp[0] + sz),
                        r(lp[1], lp[1] - sz)
                    )
                else:
                    np = (
                        r(lp[0], lp[0] - sz),
                        r(lp[1], lp[1] - sz)
                    )
            pts.append(np)
            lp = np
        self.opts = pts
        self.origm = self.midpt

    def draw(self):
        diff = (
            self.origm[0] - self.midpt[0],
            self.origm[1] - self.midpt[1],
        )
        self.pts = [
            (p[0] + diff[0], p[1] + diff[1])
            for p in self.opts
        ]
        self.drawer.line((*self.pts,), fill=self.filler)
