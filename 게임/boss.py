from pico2d import *

class Boss:
    def __init__(Boss):
        Boss.x, Boss.y = 1420, 270
        Boss.image = load_image('boss.png')
        Boss.font = load_font('ENCR10B.TTF', 16)
        Boss.HP = 2000

        Boss.timer = 100
    def update(Boss):
        pass

    def draw(Boss):
        Boss.image.clip_draw(0, 0, 250, 350, 1455, 350)
        Boss.font.draw(1350, 500, '(HP: %3.2f/2000.00)' % Boss.HP, (255, 0, 0))
        draw_rectangle(*Boss.get_bb())

    def get_bb(Boss):
        return Boss.x - 100, Boss.y - 200, Boss.x + 100, Boss.y + 250