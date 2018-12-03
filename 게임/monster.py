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
    image = None

    def __init__(Monster1):
        if Monster1.image == None:
            Monster1.image = load_image('monster1.png')
        Monster1.y = [270, 270, 270]
        Monster1.x, Monster1.y = random.randint(1400, 10000) , Monster1.y[random.randint(0, 2)]

        Monster1.font = load_font('ENCR10B.TTF', 15)
        Monster1.HP = 300
        Monster1.Attack = 30
        Monster1.colliding = True
        Monster1.frame = 0

        Monster1.attack_sound = load_wav('zombie_attack.ogg')
        Monster1.attack_sound.set_volume(50)

    def attacking(Monster1, player):
        Monster1.attack_sound.play()

    def add_event(Monster1, event):
        pass

    def update(Monster1):
        if Monster1.colliding == True:
            Monster1.frame = (Monster1.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
            Monster1.x -= 1  # 이동속도
        elif Monster1.colliding == False:
            Monster1.frame = (Monster1.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            Monster1.x -= 0

        Monster1.x = clamp(25, Monster1.x, 1600 - 25)

    def draw(Monster1):
        if Monster1.x < 1400:
            if Monster1.colliding == True:
                Monster1.image.clip_draw(0, int(Monster1.frame) * 100, 100, 100, Monster1.x, Monster1.y)
                Monster1.font.draw(Monster1.x - 60, Monster1.y + 50, 'HP : %3.2i/300' % int(Monster1.HP), (0, 0, 0))
            elif Monster1.colliding == False:
                Monster1.image.clip_draw(100, int(Monster1.frame) * 100, 100, 100, Monster1.x, Monster1.y)
                Monster1.font.draw(Monster1.x - 60, Monster1.y + 50, 'HP : %3.2i/300' % int(Monster1.HP), (0, 0, 0))
            #draw_rectangle(*Monster1.get_bb())

    def handle_event(Monster1, event):
        pass

    def get_bb(Monster1):
        return Monster1.x - 40, Monster1.y - 50, Monster1.x , Monster1.y + 50


class Monster2:
    image = None

    def __init__(Monster2):
        if Monster2.image == None:
            Monster2.image = load_image('monster2.png')
        Monster2.y = [270, 270, 270]
        Monster2.x, Monster2.y = random.randint(1400, 10000) ,Monster2.y[random.randint(0, 2)]
        Monster2.font = load_font('ENCR10B.TTF', 15)
        Monster2.HP = 400
        Monster2.Attack = 40
        Monster2.frame = 0
        Monster2.colliding = True

        Monster2.attack_sound = load_wav('zombie_attack.ogg')
        Monster2.attack_sound.set_volume(50)

    def attacking(Monster2, player):
        Monster2.attack_sound.play()

    def add_event(Monster2, event):
        pass

    def update(Monster2):
        if Monster2.colliding == True:
            Monster2.frame = (Monster2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
            Monster2.x -= 0.5  # 이동속도
        elif Monster2.colliding == False:
            Monster2.frame = (Monster2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
            Monster2.x -= 0

            Monster2.x = clamp(25, Monster2.x, 1600 - 25)
            Monster2.mana = get_time()


    def draw(Monster2):
        if Monster2.x < 1400:
            if Monster2.colliding == True:
                Monster2.image.clip_draw(0, int(Monster2.frame) * 100, 100, 100, Monster2.x, Monster2.y)
                Monster2.font.draw(Monster2.x - 60, Monster2.y + 50, 'HP : %3.2i/400' % int(Monster2.HP), (0, 0, 0))
            elif Monster2.colliding == False:
                Monster2.image.clip_draw(100, int(Monster2.frame) * 100, 100, 100, Monster2.x, Monster2.y)
                Monster2.font.draw(Monster2.x - 60, Monster2.y + 50, 'HP : %3.2i/400' % int(Monster2.HP), (0, 0, 0))
            #draw_rectangle(*Monster2.get_bb())

    def handle_event(Monster2, event):
        pass

    def get_bb(Monster2):
        return Monster2.x - 50, Monster2.y - 40, Monster2.x + 40, Monster2.y + 40


class Monster3:
    image = None

    def __init__(Monster3):
        if Monster3.image == None:
            Monster3.image = load_image('Monster3.png')
        Monster3.y = [270,270,270]
        Monster3.x, Monster3.y = random.randint(1400, 10000) ,Monster3.y[random.randint(0, 2)]
        Monster3.font = load_font('ENCR10B.TTF', 15)
        Monster3.HP = 200
        Monster3.Attack = 20
        Monster3.colliding = True
        Monster3.frame = 0

        Monster3.attack_sound = load_wav('bomb_attack.ogg')
        Monster3.attack_sound.set_volume(50)

    def attacking(Monster3, player):
        Monster3.attack_sound.play()

    def add_event(Monster3, event):
        pass

    def update(Monster3):
        if Monster3.colliding == True:
            Monster3.frame = (Monster3.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
            Monster3.x -= 0.8  # 이동속도
        elif Monster3.colliding == False:
            Monster3.frame = (Monster3.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
            Monster3.x -= 0

        Monster3.x = clamp(25, Monster3.x, 1600 - 25)
        Monster3.mana = get_time()

    def draw(Monster3):
        if Monster3.x < 1400:
            if Monster3.colliding == True:
                Monster3.image.clip_draw(0, int(Monster3.frame) * 100, 100, 100, Monster3.x, Monster3.y)
                Monster3.font.draw(Monster3.x - 60, Monster3.y + 50, 'HP : %3.2i/200' % int(Monster3.HP), (0, 0, 0))
            elif Monster3.colliding == False:
                Monster3.image.clip_draw(100, int(Monster3.frame) * 100, 100, 100, Monster3.x, Monster3.y)
                Monster3.font.draw(Monster3.x - 60, Monster3.y + 50, 'HP : %3.2i/200' % int(Monster3.HP), (0, 0, 0))

            #draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 30, self.y + 40

class Monster4:
    image = None

    def __init__(Monster4):
        if Monster4.image == None:
            Monster4.image = load_image('Monster4.png')
        Monster4.y = [270, 270, 270]
        Monster4.x, Monster4.y = random.randint(1400, 10000), Monster4.y[random.randint(0, 2)]
        Monster4.colliding = True
        Monster4.font = load_font('ENCR10B.TTF', 15)
        Monster4.HP = 500
        Monster4.Attack = 30
        Monster4.frame = 0

        Monster4.attack_sound = load_wav('bomb_attack.ogg')
        Monster4.attack_sound.set_volume(50)

    def attacking(Monster4, player):
        Monster4.attack_sound.play()

    def add_event(Monster4, event):
        pass

    def update(Monster4):
        Monster4.frame = (Monster4.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        if Monster4.colliding == True:
            Monster4.x -= 1.2  # 이동속도
        elif Monster4.colliding == False:
            Monster4.x -= 0

            Monster4.x = clamp(25, Monster4.x, 1600 - 25)
            Monster4.mana = get_time()

    def draw(Monster4):
        if Monster4.x <1400:
            Monster4.image.clip_draw(0, int(Monster4.frame) * 100, 100, 100, Monster4.x, Monster4.y)
            Monster4.font.draw(Monster4.x - 60, Monster4.y + 50, 'HP : %3.2i/500' % int(Monster4.HP), (0, 0, 0))
            #draw_rectangle(*Monster4.get_bb())

    def handle_event(Monster4, event):
        pass

    def get_bb(Monster4):
        return Monster4.x - 45, Monster4.y - 45, Monster4.x + 35, Monster4.y + 45