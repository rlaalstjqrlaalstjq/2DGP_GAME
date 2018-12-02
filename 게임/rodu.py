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
            Rodu.y = [270, 270, 270]
        Rodu.x, Rodu.y = 150, Rodu.y[random.randint(0, 2)]
        Rodu.font = load_font('ENCR10B.TTF', 15)
        Rodu.HP = 500    #체력
        Rodu.Attack = 30  #공격력
        Rodu.Mana = 7  #소환에 필요한 마나 소모량
        Rodu.frame = 0
        Rodu.fisrt_time = 0
        Rodu.timer = 100
        Rodu.colliding = True

        Rodu.attack_sound = load_wav('army_attack3.ogg')
        Rodu.attack_sound.set_volume(50)

    def attacking(Rodu, monster):
        Rodu.attack_sound.play()

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

    def get_bb(Rodu):
        return Rodu.x , Rodu.y - 40, Rodu.x + 30, Rodu.y + 40


class Rodu2:
    image = None

    def __init__(Rodu2):
        if Rodu2.image == None:
            Rodu2.image = load_image('Rodu.png')
            Rodu2.y = [270, 270, 270]
        Rodu2.x, Rodu2.y = 150, Rodu2.y[random.randint(0, 2)]
        Rodu2.font = load_font('ENCR10B.TTF', 15)
        Rodu2.HP = 500    #체력
        Rodu2.Attack = 30  #공격력
        Rodu2.Mana = 7  #소환에 필요한 마나 소모량
        Rodu2.frame = 0
        Rodu2.fisrt_time = 0
        Rodu2.timer = 100
        Rodu2.colliding = True

        Rodu2.attack_sound = load_wav('army_attack3.ogg')
        Rodu2.attack_sound.set_volume(50)

    def attacking(Rodu2, monster):
        Rodu2.attack_sound.play()

    def add_event(Rodu2, event):
        pass

    def update(Rodu2):
        Rodu2.frame = (Rodu2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        Rodu2.x = clamp(25, Rodu2.x, 1600 - 25)

        if Rodu2.colliding == True:
            Rodu2.x += 1.7  # 이동속도
        elif Rodu2.colliding == False:
            Rodu2.x += 0

    def draw(Rodu2):
        Rodu2.image.clip_draw(0, int(Rodu2.frame) * 100, 100, 100, Rodu2.x, Rodu2.y)
        Rodu2.font.draw(Rodu2.x - 60, Rodu2.y + 50, 'HP : %3.2i/500' % int(Rodu2.HP), (0, 0, 0))
        draw_rectangle(*Rodu2.get_bb())

    def handle_event(Rodu2, event):
        pass

    def get_bb(Rodu2):
        return Rodu2.x , Rodu2.y - 40, Rodu2.x + 30, Rodu2.y + 40

class Rodu3:
    image = None

    def __init__(Rodu3):
        if Rodu3.image == None:
            Rodu3.image = load_image('Rodu.png')
            Rodu3.y = [270, 270, 270]
        Rodu3.x, Rodu3.y = 150, Rodu3.y[random.randint(0, 2)]
        Rodu3.font = load_font('ENCR10B.TTF', 15)
        Rodu3.HP = 500    #체력
        Rodu3.Attack = 30  #공격력
        Rodu3.Mana = 7  #소환에 필요한 마나 소모량
        Rodu3.frame = 0
        Rodu3.fisrt_time = 0
        Rodu3.timer = 100
        Rodu3.colliding = True

        Rodu3.attack_sound = load_wav('army_attack3.ogg')
        Rodu3.attack_sound.set_volume(50)

    def attacking(Rodu3, monster):
        Rodu3.attack_sound.play()

    def add_event(Rodu3, event):
        pass

    def update(Rodu3):
        Rodu3.frame = (Rodu3.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        Rodu3.x = clamp(25, Rodu3.x, 1600 - 25)

        if Rodu3.colliding == True:
            Rodu3.x += 1.7  # 이동속도
        elif Rodu3.colliding == False:
            Rodu3.x += 0

    def draw(Rodu3):
        Rodu3.image.clip_draw(0, int(Rodu3.frame) * 100, 100, 100, Rodu3.x, Rodu3.y)
        Rodu3.font.draw(Rodu3.x - 60, Rodu3.y + 50, 'HP : %3.2i/500' % int(Rodu3.HP), (0, 0, 0))
        draw_rectangle(*Rodu3.get_bb())

    def handle_event(Rodu3, event):
        pass

    def get_bb(Rodu3):
        return Rodu3.x , Rodu3.y - 40, Rodu3.x + 30, Rodu3.y + 40

class Rodu4:
    image = None

    def __init__(Rodu4):
        if Rodu4.image == None:
            Rodu4.image = load_image('Rodu.png')
            Rodu4.y = [270, 270, 270]
        Rodu4.x, Rodu4.y = 150, Rodu4.y[random.randint(0, 2)]
        Rodu4.font = load_font('ENCR10B.TTF', 15)
        Rodu4.HP = 500    #체력
        Rodu4.Attack = 30  #공격력
        Rodu4.Mana = 7  #소환에 필요한 마나 소모량
        Rodu4.frame = 0
        Rodu4.fisrt_time = 0
        Rodu4.timer = 100
        Rodu4.colliding = True

        Rodu4.attack_sound = load_wav('army_attack3.ogg')
        Rodu4.attack_sound.set_volume(50)

    def attacking(Rodu4, monster):
        Rodu4.attack_sound.play()

    def add_event(Rodu4, event):
        pass

    def update(Rodu4):
        Rodu4.frame = (Rodu4.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        Rodu4.x = clamp(25, Rodu4.x, 1600 - 25)

        if Rodu4.colliding == True:
            Rodu4.x += 1.7  # 이동속도
        elif Rodu4.colliding == False:
            Rodu4.x += 0

    def draw(Rodu4):
        Rodu4.image.clip_draw(0, int(Rodu4.frame) * 100, 100, 100, Rodu4.x, Rodu4.y)
        Rodu4.font.draw(Rodu4.x - 60, Rodu4.y + 50, 'HP : %3.2i/500' % int(Rodu4.HP), (0, 0, 0))
        draw_rectangle(*Rodu4.get_bb())

    def handle_event(Rodu4, event):
        pass

    def get_bb(Rodu4):
        return Rodu4.x , Rodu4.y - 40, Rodu4.x + 30, Rodu4.y + 40

