import math

from .filler import Filler


class GradientFiller(Filler):
    def __init__(self, *key_frames, rate=1):
        self.key_frames = iter(key_frames)
        self.rate = rate


    def fill(self):
        last_frame = next(self.key_frames)
        try:
            for new_frame in self.key_frames:
                diff = (
                    new_frame[0] - last_frame[0],
                    new_frame[1] - last_frame[1],
                    new_frame[2] - last_frame[2],
                )
                while diff != (0, 0, 0):
                    last_frame = (
                        self.converge(last_frame[0], new_frame[0]),
                        self.converge(last_frame[1], new_frame[1]),
                        self.converge(last_frame[2], new_frame[2]),
                    )
                    diff = (
                        new_frame[0] - last_frame[0],
                        new_frame[1] - last_frame[1],
                        new_frame[2] - last_frame[2],
                    )
                    yield last_frame
        except StopIteration:
            pass
        while True:
            yield last_frame

    def converge(self, number, target):
        if number > target:
            return max(number - self.rate, target)
        elif number < target:
            return min(number + self.rate, target)
        else:
            return target
