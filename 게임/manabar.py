from pico2d import *

class Manabar:
    def __init__(self):
        self.image = load_image('mana_bar.png')
        self.x = 0
    def update(self):
        self.x += 1

    def do(self):
        pass




    def draw(self):
        self.image.clip_draw(0, 20, 400, 70, 400, 40)
        if self.x <380:
            self.image.clip_draw(0, 0, self.x*1, 20, 600, 40)

        if self. x>= 380:
            self.image.clip_draw(0, 0, 380, 20, 700, 40)

