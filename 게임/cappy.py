import game_framework
from pico2d import *

import game_world
import random
import math

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30cm
RUN_SPEED_KMPH = 20.0  # km / hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
FINISH_SOU = 3 * PIXEL_PER_METER
PIE_SPEED_TIME = 3.141592

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Cappy:
    image = None

    def __init__(Cappy):
        if Cappy.image == None:
            Cappy.image = load_image('Cappy.png')
        Cappy.x, Cappy.y = 150, 270
        Cappy.font = load_font('ENCR10B.TTF', 15)
        Cappy.HP = 120    #체력
        Cappy.Attack = 20  #공격력
        Cappy.Mana = 2  #소환에 필요한 마나 소모량
        Cappy.frame = 0
        Cappy.fisrt_time = 0
        Cappy.timer = 100
        Cappy.colliding = True

    def add_event(Cappy, event):
        pass

    def update(Cappy):
        Cappy.frame = (Cappy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        Cappy.x = clamp(25, Cappy.x, 1600 - 25)

        if Cappy.colliding == True:
            Cappy.x += 2  # 이동속도
        elif Cappy.colliding == False:
            Cappy.x += 0

    def draw(Cappy):
        Cappy.image.clip_draw(0, int(Cappy.frame) * 100, 100, 100, Cappy.x, Cappy.y)
        Cappy.font.draw(Cappy.x - 60, Cappy.y + 50, 'HP : %3.2i/350' % int(Cappy.HP), (0, 0, 0))
        draw_rectangle(*Cappy.get_bb())

    def handle_event(Cappy, event):
        pass

    def get_bb(Cappy):
        return Cappy.x , Cappy.y - 40, Cappy.x + 30, Cappy.y + 40

