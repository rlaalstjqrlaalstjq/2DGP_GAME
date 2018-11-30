import game_framework
from pico2d import *

import game_world
import random
import math

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30cm
RUN_SPEED_KMPH = 20.0  # km / hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
FINISH_SOU = 3 * PIXEL_PER_METER
PIE_SPEED_TIME = 3.141592

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class BrassItem:
    def __init__(BrassItem):
        BrassItem.x, BrassItem.y = 750, 350
        BrassItem.image = load_image('brassitem.png')
        BrassItem.font = load_font('ENCR10B.TTF', 50)
        BrassItem.frame = 0
        BrassItem.timer = 150
        BrassItem.can_use = 1


    def update(BrassItem):
        BrassItem.frame = (BrassItem.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    def do(BrassItem):
        pass

    def draw(BrassItem):
        if BrassItem.timer > 0:
            BrassItem.image.clip_draw(0, int(BrassItem.frame) * 300, 600, 300, BrassItem.x, BrassItem.y)
            BrassItem.timer -= 1

    def handle_event(BrassItem, event):
        pass