from pico2d import *

class Manabar:
    def __init__(Manabar):
        Manabar.image = load_image('mana_bar.png')
        Manabar.font = load_font('ENCR10B.TTF', 50)
        Manabar.x = 0
        Manabar.bar_num = 0
        Manabar.timer = 60
    def update(Manabar):
        Manabar.x = get_time()
        Manabar.timer -= 1
        if Manabar.timer == 0:
            Manabar.bar_num += 1
            Manabar.timer = 60

    def do(Manabar):
        pass




    def draw(Manabar):

        Manabar.font.draw(640, 650, 'Time : %3.2f' % Manabar.x, (0, 0, 0))

        Manabar.image.clip_draw(0, 20, 400, 70, 500, 40)
        if (Manabar.bar_num*19) < 380:
            Manabar.image.clip_draw(0, 0, int(Manabar.bar_num*20), 20, 400, 40)

        if (Manabar.bar_num*19) >= 380:
            Manabar.image.clip_draw(0, 0, 380, 20, 500, 40)


        if Manabar.bar_num <10:
            Manabar.font.draw(210, 40, '%3.2i' % Manabar.bar_num, (0, 200, 0))
        else:
            Manabar.bar_num = 10
            Manabar.font.draw(210, 40, '%3.2i' % Manabar.bar_num, (0, 200, 0))
            # 마나바 10개에 걸리는 충전시간 20초로 설정


