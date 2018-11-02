from pico2d import *

class Boss:
    def __init__(self):
        self.image = load_image('boss.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 250, 350, 1455, 350)
