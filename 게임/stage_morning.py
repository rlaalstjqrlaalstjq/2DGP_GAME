from pico2d import *

class Stage_Morning:
    def __init__(self):
        self.image = load_image('stage1.png')
        self.bgm = load_music('grondmusic.mp3')
        self.bgm.set_volume(50)
        self.bgm.repeat_play()
    def update(self):
        pass

    def draw(self):
        self.image.draw(1565 //2, 700//2)

