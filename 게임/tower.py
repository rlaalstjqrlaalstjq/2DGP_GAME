from pico2d import *

class Tower:
    def __init__(self):
        self.image = load_image('tower.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 200, 200, 90, 300)
