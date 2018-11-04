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

class HeelItem:
    def __init__(HeelItem):
        HeelItem.x, HeelItem.y = 120, 300
        HeelItem.image = load_image('heelitem.png')
        HeelItem.font = load_font('ENCR10B.TTF', 50)
        HeelItem.frame = 0
        HeelItem.bar_num = 0

    def update(HeelItem):
        HeelItem.frame = (HeelItem.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7

    def do(HeelItem):
        pass

    def draw(HeelItem):
        HeelItem.image.clip_draw(0, int(HeelItem.frame) * 150, 200, 150, HeelItem.x, HeelItem.y)


    def handle_event(HeelItem, event):
        pass