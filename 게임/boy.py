import game_framework
from pico2d import *
from ball import Ball

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
PLAYER1, PLAYER2, PLAYER3, PLAYER4, ITEM = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_q): PLAYER1,
    (SDL_KEYDOWN, SDLK_w): PLAYER2,
    (SDL_KEYUP, SDLK_e): PLAYER3,
    (SDL_KEYUP, SDLK_r): PLAYER4,
    (SDL_KEYDOWN, SDLK_SPACE): ITEM
}

# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == PLAYER1:
            boy.velocity += RUN_SPEED_PPS
        elif event == PLAYER2:
            boy.velocity -= RUN_SPEED_PPS
        elif event == PLAYER3:
            boy.velocity -= RUN_SPEED_PPS
        elif event == PLAYER4:
            boy.velocity += RUN_SPEED_PPS
        boy.timer = 0

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        boy.timer += get_time() - boy.fisrt_time
        boy.fisrt_time = get_time()

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(0, 400, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(100, 400, 100, 100, boy.x, boy.y)

class RunState:

    @staticmethod
    def enter(boy, event):
        if event == PLA:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.dir = clamp(-1, boy.velocity, 1)

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)
        boy.image.opacify(1)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(0, int(boy.frame) * 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(100 , int(boy.frame) * 100, 100, 100, boy.x, boy.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
}


class Boy:
    def __init__(self):
        self.x, self.y = 100, 300
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('unit_48.png')
        self.font = load_font('ENCR10B.TTF', 30)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.fisrt_time = 0




    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)

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
        self.font.draw(720, 650, 'Time : %3.2f' % get_time(), (0, 0, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

            #비공개설정으로 다시 올립니다.