from uuid import uuid4 as uuid


class Drawer:
    def __init__(self):
        self.img = None
        self.drawer = None

    def save(self):
        file_name = f'./output/{uuid()}.bmp'

        abs_path = f"{file_name.replace('./', 'app/')}"
        with open('log.txt', 'w+') as f:
            print(abs_path, file=f)
        self.img.save(file_name)

    def draw(self):
        return NotImplemented
