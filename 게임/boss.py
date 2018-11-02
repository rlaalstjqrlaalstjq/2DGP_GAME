from pico2d import *

class Boss:
    def __init__(self):
        self.image = load_image('boss.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.HP = 2000

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 250, 350, 1455, 350)
        self.font.draw(1350, 500, '(HP: %3.2f/2000.00)' % self.HP, (255, 0, 0))
