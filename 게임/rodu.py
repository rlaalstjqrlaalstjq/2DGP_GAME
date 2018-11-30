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


class Rodu:
    image = None

    def __init__(Rodu):
        if Rodu.image == None:
            Rodu.image = load_image('Rodu.png')
            Rodu.y = [270, 170, 370]
        Rodu.x, Rodu.y = 150, Rodu.y[random.randint(0, 2)]
        Rodu.font = load_font('ENCR10B.TTF', 15)
        Rodu.HP = 500    #체력
        Rodu.Attack = 30  #공격력
        Rodu.Mana = 7  #소환에 필요한 마나 소모량
        Rodu.frame = 0
        Rodu.fisrt_time = 0
        Rodu.timer = 100
        Rodu.colliding = True

    def add_event(Rodu, event):
        pass

    def update(Rodu):
        Rodu.frame = (Rodu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        Rodu.x = clamp(25, Rodu.x, 1600 - 25)

        if Rodu.colliding == True:
            Rodu.x += 1.7  # 이동속도
        elif Rodu.colliding == False:
            Rodu.x += 0

    def draw(Rodu):
        Rodu.image.clip_draw(0, int(Rodu.frame) * 100, 100, 100, Rodu.x, Rodu.y)
        Rodu.font.draw(Rodu.x - 60, Rodu.y + 50, 'HP : %3.2i/500' % int(Rodu.HP), (0, 0, 0))
        draw_rectangle(*Rodu.get_bb())

    def handle_event(Rodu, event):
        pass

    def get_bb(Cappy):
        return Cappy.x , Cappy.y - 40, Cappy.x + 30, Cappy.y + 40

