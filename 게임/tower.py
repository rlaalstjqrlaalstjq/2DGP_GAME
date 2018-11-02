from pico2d import *

class Tower:
    def __init__(self):
        self.image = load_image('tower.png')
        self.font = load_font('ENCR10B.TTF', 15)
        self.HP = 1000

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 200, 200, 90, 300)
        self.font.draw(30, 420, '(HP: %3.2f/1000.00)' % self.HP, (0, 0, 255))
