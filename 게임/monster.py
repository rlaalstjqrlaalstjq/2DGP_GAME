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




class Monster1:
    def __init__(self):
        self.x, self.y = 1400 , 270
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('monster1.png')

        self.font = load_font('ENCR10B.TTF', 15)
        self.HP = 300
        self.Attack = 30

        self.frame = 0




    def add_event(self, event):
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x -= 2  # 이동속도
        self.x = clamp(25, self.x, 1600 - 25)

        self.mana = get_time()




    def draw(self):

        self.image.clip_draw(0, int(self.frame) * 100, 100, 100, self.x, self.y)


        self.font.draw(self.x - 60, self.y + 50, 'HP : %3.2i/300' % int(self.HP), (0, 0, 0))



    def handle_event(self, event):
        pass



class Monster2:
    def __init__(self):
        self.x, self.y = 1400 , 270
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('monster1.png')

        self.font = load_font('ENCR10B.TTF', 15)
        self.HP = 300
        self.Attack = 30

        self.frame = 0




    def add_event(self, event):
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x -= 2  # 이동속도
        self.x = clamp(25, self.x, 1600 - 25)

        self.mana = get_time()




    def draw(self):

        self.image.clip_draw(0, int(self.frame) * 100, 100, 100, self.x, self.y)


        self.font.draw(self.x - 60, self.y + 50, 'HP : %3.2i/300' % int(self.HP), (0, 0, 0))



    def handle_event(self, event):
        pass

