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
    def __init__(Monster1):
        Monster1.y = [270, 170, 370]
        Monster1.x, Monster1.y = random.randint(1400, 2000) , Monster1.y[random.randint(0, 2)]
        # Boy is only once created, so instance image loading is fine
        Monster1.image = load_image('monster1.png')

        Monster1.font = load_font('ENCR10B.TTF', 15)
        Monster1.HP = 300
        Monster1.Attack = 30
        Monster1.colliding = True
        Monster1.frame = 0




    def add_event(Monster1, event):
        pass

    def update(Monster1):
        Monster1.frame = (Monster1.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        if Monster1.colliding == True:
            Monster1.x -= 1  # 이동속도
        elif Monster1.colliding == False:
            Monster1.x -= 0

        Monster1.x = clamp(25, Monster1.x, 1600 - 25)



    def draw(Monster1):
        if Monster1.x < 1400:
            Monster1.image.clip_draw(0, int(Monster1.frame) * 100, 100, 100, Monster1.x, Monster1.y)
            Monster1.font.draw(Monster1.x - 60, Monster1.y + 50, 'HP : %3.2i/300' % int(Monster1.HP), (0, 0, 0))
            draw_rectangle(*Monster1.get_bb())

    def handle_event(Monster1, event):
        pass

    def get_bb(Monster1):
        return Monster1.x - 40, Monster1.y - 50, Monster1.x , Monster1.y + 50

class Monster2:
    def __init__(self):
        self.y = [270, 170, 370]
        self.x, self.y = random.randint(1400, 5000) ,self.y[random.randint(0, 2)]
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('monster2.png')

        self.font = load_font('ENCR10B.TTF', 15)
        self.HP = 400
        self.Attack = 40

        self.frame = 0




    def add_event(self, event):
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.x -= 0.5  # 이동속도
        self.x = clamp(25, self.x, 1600 - 25)

        self.mana = get_time()




    def draw(self):
        if self.x < 1400:
            self.image.clip_draw(0, int(self.frame) * 100, 100, 100, self.x, self.y)
            self.font.draw(self.x - 60, self.y + 50, 'HP : %3.2i/400' % int(self.HP), (0, 0, 0))
            draw_rectangle(*self.get_bb())


    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 50, self.y - 40, self.x + 40, self.y + 40
class Monster3:
    def __init__(self):
        self.y = [270,170,370]
        self.x, self.y = random.randint(1400, 5000) ,self.y[random.randint(0, 2)]
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('Monster3.png')

        self.font = load_font('ENCR10B.TTF', 15)
        self.HP = 200
        self.Attack = 20

        self.frame = 0




    def add_event(self, event):
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.x -= 0.8  # 이동속도
        self.x = clamp(25, self.x, 1600 - 25)

        self.mana = get_time()




    def draw(self):
        if self.x < 1400:
            self.image.clip_draw(0, int(self.frame) * 100, 100, 100, self.x, self.y)
            self.font.draw(self.x - 60, self.y + 50, 'HP : %3.2i/200' % int(self.HP), (0, 0, 0))
            draw_rectangle(*self.get_bb())


    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 30, self.y + 40

class Monster4:
    def __init__(self):
        self.y = [270, 170, 370]
        self.x, self.y = random.randint(1400, 5000), self.y[random.randint(0, 2)]
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('Monster4.png')

        self.font = load_font('ENCR10B.TTF', 15)
        self.HP = 500
        self.Attack = 30

        self.frame = 0




    def add_event(self, event):
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.x -= 0.3  # 이동속도
        self.x = clamp(25, self.x, 1600 - 25)

        self.mana = get_time()




    def draw(self):
        if self.x <1400:
            self.image.clip_draw(0, int(self.frame) * 100, 100, 100, self.x, self.y)
            self.font.draw(self.x - 60, self.y + 50, 'HP : %3.2i/500' % int(self.HP), (0, 0, 0))
            draw_rectangle(*self.get_bb())


    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 45, self.y - 45, self.x + 35, self.y + 45