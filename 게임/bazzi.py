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


class Bazzi:


    def __init__(Bazzi):
        Bazzi.x, Bazzi.y = 230, 270
        # Boy is only once created, so instance image loading is fine
        Bazzi.image = load_image('Bazzi.png')
        Bazzi.font = load_font('ENCR10B.TTF', 15)
        Bazzi.HP = 350    #체력
        Bazzi.Attack = 50  #공격력
        Bazzi.Mana = 3  #소환에 필요한 마나 소모량

        Bazzi.frame = 0
        Bazzi.fisrt_time = 0
        Bazzi.timer = 100
        Bazzi.colliding = True

    def add_event(Bazzi, event):
        pass

    def update(Bazzi):

            Bazzi.frame = (Bazzi.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            Bazzi.x = clamp(25, Bazzi.x, 1600 - 25)

            if Bazzi.colliding == True:
                Bazzi.x += 3  # 이동속도
            elif Bazzi.colliding == False:
                Bazzi.x += 0




    def draw(Bazzi):
        Bazzi.image.clip_draw(0, int(Bazzi.frame) * 100, 100, 100, Bazzi.x, Bazzi.y)
        Bazzi.font.draw(Bazzi.x - 60, Bazzi.y + 50, 'HP : %3.2i/350' % int(Bazzi.HP), (0, 0, 0))
        draw_rectangle(*Bazzi.get_bb())
    def handle_event(Bazzi, event):
        pass

    def get_bb(self):
        return self.x , self.y - 40, self.x + 30, self.y + 40
