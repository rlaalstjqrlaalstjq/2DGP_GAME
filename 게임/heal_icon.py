from pico2d import *

class Heal_Icon:
    def __init__(Heal_Icon):
        Heal_Icon.image = load_image('heal_icon.png')

    def update(Heal_Icon):
        pass

    def draw(Heal_Icon):
        Heal_Icon.image.clip_draw(0, 0, 100, 100, 50, 650)

