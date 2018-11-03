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

# Boy Event
CREATE_BAZZI,CREATE_DIO = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_q): CREATE_BAZZI,
(SDL_KEYDOWN, SDLK_w): CREATE_DIO
}

# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        pass

    @staticmethod
    def exit(boy, event):
       pass

    @staticmethod
    def do(Monster1):
        Monster1.frame = (Monster1.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        Monster1.x -= 2
        Monster1.x = clamp(25, Monster1.x, 1600 - 25)
        timer = get_time()

    @staticmethod
    def draw(Monster1):

        Monster1.image.clip_draw(0, int(Monster1.frame) * 100, 100, 100, Monster1.x, Monster1.y)




next_state_table = {
    IdleState: {},


}


class Monster1:
    def __init__(self):
        self.x, self.y = 1400 , 270
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('monster1.png')

        self.font = load_font('ENCR10B.TTF', 15)
        self.HP = 200

        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.fisrt_time = 0



    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, 'HP : %3.2i/200' % int(self.HP), (0, 0, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

class Dio:
    def __init__(self):
        self.x, self.y = 230 , 270
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('Dio.png')
        self.font = load_font('ENCR10B.TTF', 15)
        self.HP = 350

        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.fisrt_time = 0



    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, 'HP : %3.2i/350' % int(self.HP), (0, 0, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)