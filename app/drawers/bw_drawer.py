from tqdm import tqdm
from .drawer import Drawer
from PIL import Image, ImageDraw
from uuid import uuid4 as uuid
from random import randint as r, choice as c


class BWDrawer(Drawer):
    def __init__(self):
        self.img = Image.new('L', (1000, 1000), color=255)
        self.drawer = ImageDraw.Draw(self.img)

    def reflect_points(self, *pts):
        # y = mx + b
        m = r(-800, 800) * .01
        if m == 0:
            m = .01
        b = r(-200, 200)

        new_points = []
        for pt in pts:
            x, y = pt[0], pt[1]
            m_p = -1 / m
            b_p = y - m_p * x

            # 0 = m * x + b - y
            # 0 = m_p * x + b_p - y
            # m * x + b - y = m_p * x + b_p - y
            # m * x = m_p * x + b_p - b
            # m * x - m_p * x = b_p - b
            # (m - m_p) * x = b_p - b

            n_x = (b_p - b)/(m - m_p)
            n_y = m_p * n_x + b_p
            new_points.append((n_x, n_y))
        return new_points

    def draw(self):
        for i in tqdm(range(100)):
            x = r(-500, 500) + 500
            y = r(-500, 500) + 500
            sz = r(-100, 100) + 100
            if r(1, 10) > 9:
                self.gradient(x, y, sz)
            elif r(1, 10) > 5:
                self.binger(x, y, sz)
            else:
                self.square(x, y, sz)
            # self.img = self.img.rotate(r(0,360), resample=Image.BILINEAR)
            # self.drawer = ImageDraw.Draw(self.img)
        self.save()

    def square(self, x, y, size):
        pt1 = (x - size//2, y - size//2)
        pt2 = (x + size//2, y - size//2)
        pt3 = (x + size//2, y + size//2)
        pt4 = (x - size//2, y + size//2)

        fill = r(0, 255)

        pt1, pt2, pt3, pt4 = self.reflect_points(pt1, pt2, pt3, pt4)

        self.drawer.line((*pt1, *pt2, *pt3, *pt4, *pt1), fill=fill)

        for j, i in enumerate(range(fill)):
            p0 = (p - j%5 for p in pt1)
            p1 = (p - j%2 for p in pt2)
            p2 = (p - j%4 for p in pt3)
            p3 = (p - j%3 for p in pt4)

            self.drawer.line((*p0, *p1, *p2, *p3, *p0), fill=fill-i)

    def binger(self, x, y, size):
        pt1 = (x - size//2, y - size//2)
        pt2 = (x + size//2, y - size//2)
        pt3 = (x + size//2, y + size//2)
        pt4 = (x - size//2, y + size//2)

        fill = r(0, 255)
        s1, s2, e1, e2 = (r(0, 360), r(0, 360), r(0, 360), r(0, 360))

        pt1, pt2, pt3, pt4 = self.reflect_points(pt1, pt2, pt3, pt4)

        self.drawer.arc((*pt1, *pt3), start=s1, end=e1, fill=fill)
        self.drawer.arc((*pt2, *pt4), start=s2, end=e2, fill=fill)

        for j, i in enumerate(range(fill)):
            p0 = (p - j%2 for p in pt1)
            p1 = (p - j%3 for p in pt3)
            start = c((s1, s2))
            end = c((e1, e2))
            self.drawer.arc((*p0, *p1), start=start, end=end, fill=fill-i)

    def gradient(self, x, y, size):
        pt1 = (x - size//2, y + size//2)
        pt2 = (x + size//2, y - size//2)

        pt1, pt2 = self.reflect_points(pt1, pt2)

        fill = r(0, 255)
        for j, i in enumerate(range(fill)):
            p1 = (p - j*2 for p in pt1)
            p2 = (p - j for p in pt2)
            self.drawer.line((*p1, *p2), fill=fill-i)
