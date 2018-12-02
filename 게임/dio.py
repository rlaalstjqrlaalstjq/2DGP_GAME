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
            Dio.y = [270, 270, 270]
        Dio.x, Dio.y = 150, Dio.y[random.randint(0, 2)]
        Dio.font = load_font('ENCR10B.TTF', 15)
        Dio.HP = 200    #체력
        Dio.Attack = 80  #공격력
        Dio.Mana = 5  #소환에 필요한 마나 소모량
        Dio.frame = 0
        Dio.fisrt_time = 0
        Dio.timer = 100
        Dio.colliding = True

        Dio.attack_sound = load_wav('army_attack2.ogg')
        Dio.attack_sound.set_volume(50)

    def attacking(Dio, monster):
        Dio.attack_sound.play()

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

class Dio2:
    image = None

    def __init__(Dio2):
        if Dio2.image == None:
            Dio2.image = load_image('Dio.png')
            Dio2.y = [270, 270, 270]
        Dio2.x, Dio2.y = 150, Dio2.y[random.randint(0, 2)]
        Dio2.font = load_font('ENCR10B.TTF', 15)
        Dio2.HP = 200    #체력
        Dio2.Attack = 80  #공격력
        Dio2.Mana = 5  #소환에 필요한 마나 소모량
        Dio2.frame = 0
        Dio2.fisrt_time = 0
        Dio2.timer = 100
        Dio2.colliding = True

        Dio2.attack_sound = load_wav('army_attack2.ogg')
        Dio2.attack_sound.set_volume(50)

    def attacking(Dio2, monster):
        Dio2.attack_sound.play()

    def add_event(Dio2, event):
        pass

    def update(Dio2):
        Dio2.frame = (Dio2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        Dio2.x = clamp(25, Dio2.x, 1600 - 25)

        if Dio2.colliding == True:
            Dio2.x += 1.5  # 이동속도
        elif Dio2.colliding == False:
            Dio2.x += 0

    def draw(Dio2):
        Dio2.image.clip_draw(0, int(Dio2.frame) * 100, 100, 100, Dio2.x, Dio2.y)
        Dio2.font.draw(Dio2.x - 60, Dio2.y + 50, 'HP : %3.2i/200' % int(Dio2.HP), (0, 0, 0))
        draw_rectangle(*Dio2.get_bb())

    def handle_event(Dio2, event):
        pass

    def get_bb(Dio2):
        return Dio2.x , Dio2.y - 40, Dio2.x + 30, Dio2.y + 40

class Dio3:
    image = None

    def __init__(Dio3):
        if Dio3.image == None:
            Dio3.image = load_image('Dio.png')
            Dio3.y = [270, 270, 270]
            Dio3.x, Dio3.y = 150, Dio3.y[random.randint(0, 2)]
        Dio3.font = load_font('ENCR10B.TTF', 15)
        Dio3.HP = 200    #체력
        Dio3.Attack = 80  #공격력
        Dio3.Mana = 5  #소환에 필요한 마나 소모량
        Dio3.frame = 0
        Dio3.fisrt_time = 0
        Dio3.timer = 100
        Dio3.colliding = True

        Dio3.attack_sound = load_wav('army_attack2.ogg')
        Dio3.attack_sound.set_volume(50)

    def attacking(Dio3, monster):
        Dio3.attack_sound.play()

    def add_event(Dio3, event):
        pass

    def update(Dio3):
        Dio3.frame = (Dio3.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        Dio3.x = clamp(25, Dio3.x, 1600 - 25)

        if Dio3.colliding == True:
            Dio3.x += 1.5  # 이동속도
        elif Dio3.colliding == False:
            Dio3.x += 0

    def draw(Dio3):
        Dio3.image.clip_draw(0, int(Dio3.frame) * 100, 100, 100, Dio3.x, Dio3.y)
        Dio3.font.draw(Dio3.x - 60, Dio3.y + 50, 'HP : %3.2i/200' % int(Dio3.HP), (0, 0, 0))
        draw_rectangle(*Dio3.get_bb())

    def handle_event(Dio3, event):
        pass

    def get_bb(Dio3):
        return Dio3.x , Dio3.y - 40, Dio3.x + 30, Dio3.y + 40

class Dio4:
    image = None

    def __init__(Dio4):
        if Dio4.image == None:
            Dio4.image = load_image('Dio.png')
            Dio4.y = [270, 270, 270]
            Dio4.x, Dio4.y = 150, Dio4.y[random.randint(0, 2)]
        Dio4.font = load_font('ENCR10B.TTF', 15)
        Dio4.HP = 200    #체력
        Dio4.Attack = 80  #공격력
        Dio4.Mana = 5  #소환에 필요한 마나 소모량
        Dio4.frame = 0
        Dio4.fisrt_time = 0
        Dio4.timer = 100
        Dio4.colliding = True

        Dio4.attack_sound = load_wav('army_attack2.ogg')
        Dio4.attack_sound.set_volume(50)

    def attacking(Dio4, monster):
        Dio4.attack_sound.play()

    def add_event(Dio4, event):
        pass

    def update(Dio4):
        Dio4.frame = (Dio4.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        Dio4.x = clamp(25, Dio4.x, 1600 - 25)

        if Dio4.colliding == True:
            Dio4.x += 1.5  # 이동속도
        elif Dio4.colliding == False:
            Dio4.x += 0

    def draw(Dio4):
        Dio4.image.clip_draw(0, int(Dio4.frame) * 100, 100, 100, Dio4.x, Dio4.y)
        Dio4.font.draw(Dio4.x - 60, Dio4.y + 50, 'HP : %3.2i/200' % int(Dio4.HP), (0, 0, 0))
        draw_rectangle(*Dio4.get_bb())

    def handle_event(Dio4, event):
        pass

    def get_bb(Dio4):
        return Dio4.x , Dio4.y - 40, Dio4.x + 30, Dio4.y + 40

