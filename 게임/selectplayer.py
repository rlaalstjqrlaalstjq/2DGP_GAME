from pico2d import *

class SelectPlayer:
    def __init__(self):
        self.image = load_image('select_player.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.HP = 2000

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 414, 71, 900, 40)

