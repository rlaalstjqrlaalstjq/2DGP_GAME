from pico2d import *

class Stage_Midnight:
    def __init__(self):
        self.image = load_image('stage2.png')
        self.bgm = load_music('grondmusic.mp3')
        self.bgm.set_volume(30)
        self.bgm.repeat_play()
        self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        pass

    def draw(self):
        self.image.draw(1565 //2, 700//2)
        self.font.draw(1450, 680, 'Stage 2', (255, 255, 255))

