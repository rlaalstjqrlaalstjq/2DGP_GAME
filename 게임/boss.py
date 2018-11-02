from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('stage1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1565 //2, 700//2)

