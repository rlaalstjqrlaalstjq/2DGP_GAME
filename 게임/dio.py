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


class Dio:
    image = None

    def __init__(Dio):
        if Dio.image == None:
            Dio.image = load_image('Dio.png')
            Dio.y = [270, 170, 370]
        Dio.x, Dio.y = 150, Dio.y[random.randint(0, 2)]
        Dio.font = load_font('ENCR10B.TTF', 15)
        Dio.HP = 200    #체력
        Dio.Attack = 80  #공격력
        Dio.Mana = 5  #소환에 필요한 마나 소모량
        Dio.frame = 0
        Dio.fisrt_time = 0
        Dio.timer = 100
        Dio.colliding = True

    def add_event(Dio, event):
        pass

    def update(Dio):
        Dio.frame = (Dio.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        Dio.x = clamp(25, Dio.x, 1600 - 25)

        if Dio.colliding == True:
            Dio.x += 1.5  # 이동속도
        elif Dio.colliding == False:
            Dio.x += 0

    def draw(Dio):
        Dio.image.clip_draw(0, int(Dio.frame) * 100, 100, 100, Dio.x, Dio.y)
        Dio.font.draw(Dio.x - 60, Dio.y + 50, 'HP : %3.2i/200' % int(Dio.HP), (0, 0, 0))
        draw_rectangle(*Dio.get_bb())

    def handle_event(Dio, event):
        pass

    def get_bb(Dio):
        return Dio.x , Dio.y - 40, Dio.x + 30, Dio.y + 40
