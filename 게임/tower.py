from pico2d import *

class Tower:
    def __init__(Tower):
        Tower.x, Tower.y = 1420, 270
        Tower.image = load_image('tower.png')
        Tower.font = load_font('ENCR10B.TTF', 15)
        Tower.HP = 1000

    def update(Tower):
        pass

    def draw(Tower):
        Tower.image.clip_draw(0, 0, 200, 200, 90, 300)
        Tower.font.draw(30, 420, '(HP: %3.2f/1000.00)' % Tower.HP, (0, 0, 255))
        draw_rectangle(*Tower.get_bb())

    def get_bb(Tower):
        return Tower.x-100, Tower.y - 200, Tower.x + 100, Tower.y + 250