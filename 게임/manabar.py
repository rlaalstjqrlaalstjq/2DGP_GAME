from pico2d import *

class Manabar:
    def __init__(self):
        self.image = load_image('mana_bar.png')
        self.font = load_font('ENCR10B.TTF', 50)
        self.x = 0

    def update(self):
        self.x = get_time()

    def do(self):
        pass




    def draw(self):

        self.font.draw(640, 650, 'Time : %3.2f' % get_time(), (0, 0, 0))

        self.image.clip_draw(0, 20, 400, 70, 500, 40)
        if (self.x*19) < 380:
            self.image.clip_draw(0, 0, int(self.x*10), 20, 400, 40)

        if (self.x*19) >= 380:
            self.image.clip_draw(0, 0, 380, 20, 500, 40)

        bar_num = int(self.x/2)
        if bar_num <10:
            self.font.draw(230, 40, '%3.2i' % bar_num, (0, 200, 0))
        else:
            bar_num = 10
            self.font.draw(230, 40, '%3.2i' % bar_num, (0, 200, 0))
            # 마나바 10개에 걸리는 충전시간 20초로 설정


