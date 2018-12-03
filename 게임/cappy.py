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


class Cappy:
    image = None

    def __init__(Cappy):
        if Cappy.image == None:
            Cappy.image = load_image('Cappy.png')
            Cappy.image_attack_motion = load_image ('attack_motion.png')
            Cappy.y = [270, 270, 270]
        Cappy.x, Cappy.y = 150, Cappy.y[random.randint(0, 2)]
        Cappy.font = load_font('ENCR10B.TTF', 15)
        Cappy.HP = 200    #체력
        Cappy.Attack = 20  #공격력
        Cappy.Mana = 2  #소환에 필요한 마나 소모량
        Cappy.frame = 0
        Cappy.fisrt_time = 0
        Cappy.timer = 100
        Cappy.colliding = True

        Cappy.attack_sound = load_wav('army_attack4.ogg')
        Cappy.attack_sound.set_volume(50)

    def attacking(Cappy, monster):
        Cappy.attack_sound.play()

    def add_event(Cappy, event):
        pass

    def update(Cappy):
        Cappy.x = clamp(25, Cappy.x, 1600 - 25)

        if Cappy.colliding == True:
            Cappy.frame = (Cappy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            Cappy.x += 2  # 이동속도
        elif Cappy.colliding == False:
            Cappy.frame = (Cappy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
            Cappy.x += 0

    def draw(Cappy):
        if Cappy.colliding == True:
            Cappy.image.clip_draw(0, int(Cappy.frame) * 100, 100, 100, Cappy.x, Cappy.y)
            Cappy.font.draw(Cappy.x - 60, Cappy.y + 50, 'HP : %3.2i/200' % int(Cappy.HP), (0, 0, 0))
        elif Cappy.colliding == False:
            Cappy.image_attack_motion.clip_draw(200, int(Cappy.frame) * 100, 100, 100, Cappy.x, Cappy.y)
            Cappy.font.draw(Cappy.x - 60, Cappy.y + 50, 'HP : %3.2i/200' % int(Cappy.HP), (0, 0, 0))

        #draw_rectangle(*Cappy.get_bb())

    def handle_event(Cappy, event):
        pass

    def get_bb(Cappy):
        return Cappy.x , Cappy.y - 40, Cappy.x + 30, Cappy.y + 40


class Cappy2:
    image = None

    def __init__(Cappy2):
        if Cappy2.image == None:
            Cappy2.image = load_image('Cappy.png')
            Cappy.image_attack_motion = load_image('attack_motion.png')
            Cappy2.y = [270, 270, 270]
        Cappy2.x, Cappy2.y = 150, Cappy2.y[random.randint(0, 2)]
        Cappy2.font = load_font('ENCR10B.TTF', 15)
        Cappy2.HP = 200    #체력
        Cappy2.Attack = 20  #공격력
        Cappy2.Mana = 2  #소환에 필요한 마나 소모량
        Cappy2.frame = 0
        Cappy2.fisrt_time = 0
        Cappy2.timer = 100
        Cappy2.colliding = True

        Cappy2.attack_sound = load_wav('army_attack4.ogg')
        Cappy2.attack_sound.set_volume(50)

    def attacking(Cappy2, monster):
        Cappy2.attack_sound.play()

    def add_event(Cappy2, event):
        pass

    def update(Cappy2):
        Cappy2.x = clamp(25, Cappy2.x, 1600 - 25)

        if Cappy2.colliding == True:
            Cappy2.frame = (Cappy2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            Cappy2.x += 2  # 이동속도
        elif Cappy2.colliding == False:
            Cappy2.frame = (Cappy2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
            Cappy2.x += 0

    def draw(Cappy2):
        if Cappy2.colliding == True:
            Cappy2.image.clip_draw(0, int(Cappy2.frame) * 100, 100, 100, Cappy2.x, Cappy2.y)
            Cappy2.font.draw(Cappy2.x - 60, Cappy2.y + 50, 'HP : %3.2i/200' % int(Cappy2.HP), (0, 0, 0))
        elif Cappy2.colliding == False:
            Cappy2.image_attack_motion.clip_draw(200, int(Cappy2.frame) * 100, 100, 100, Cappy2.x, Cappy2.y)
            Cappy2.font.draw(Cappy2.x - 60, Cappy2.y + 50, 'HP : %3.2i/200' % int(Cappy2.HP), (0, 0, 0))
        #draw_rectangle(*Cappy2.get_bb())

    def handle_event(Cappy2, event):
        pass

    def get_bb(Cappy2):
        return Cappy2.x , Cappy2.y - 40, Cappy2.x + 30, Cappy2.y + 40

class Cappy3:
    image = None

    def __init__(Cappy3):
        if Cappy3.image == None:
            Cappy3.image = load_image('Cappy.png')
            Cappy.image_attack_motion = load_image('attack_motion.png')
            Cappy3.y = [270, 270, 270]
        Cappy3.x, Cappy3.y = 150, Cappy3.y[random.randint(0, 2)]
        Cappy3.font = load_font('ENCR10B.TTF', 15)
        Cappy3.HP = 200    #체력
        Cappy3.Attack = 20  #공격력
        Cappy3.Mana = 2  #소환에 필요한 마나 소모량
        Cappy3.frame = 0
        Cappy3.fisrt_time = 0
        Cappy3.timer = 100
        Cappy3.colliding = True

        Cappy3.attack_sound = load_wav('army_attack4.ogg')
        Cappy3.attack_sound.set_volume(50)

    def attacking(Cappy3, monster):
        Cappy3.attack_sound.play()

    def add_event(Cappy3, event):
        pass

    def update(Cappy3):
        Cappy3.x = clamp(25, Cappy3.x, 1600 - 25)

        if Cappy3.colliding == True:
            Cappy3.frame = (Cappy3.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            Cappy3.x += 2  # 이동속도
        elif Cappy3.colliding == False:
            Cappy3.frame = (Cappy3.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
            Cappy3.x += 0

    def draw(Cappy3):
        if Cappy3.colliding == True:
            Cappy3.image.clip_draw(0, int(Cappy3.frame) * 100, 100, 100, Cappy3.x, Cappy3.y)
            Cappy3.font.draw(Cappy3.x - 60, Cappy3.y + 50, 'HP : %3.2i/200' % int(Cappy3.HP), (0, 0, 0))
        elif Cappy3.colliding == False:
            Cappy3.image_attack_motion.clip_draw(200, int(Cappy3.frame) * 100, 100, 100, Cappy3.x, Cappy3.y)
            Cappy3.font.draw(Cappy3.x - 60, Cappy3.y + 50, 'HP : %3.2i/200' % int(Cappy3.HP), (0, 0, 0))
        #draw_rectangle(*Cappy3.get_bb())

    def handle_event(Cappy3, event):
        pass

    def get_bb(Cappy3):
        return Cappy3.x , Cappy3.y - 40, Cappy3.x + 30, Cappy3.y + 40

class Cappy4:
    image = None

    def __init__(Cappy4):
        if Cappy4.image == None:
            Cappy4.image = load_image('Cappy.png')
            Cappy.image_attack_motion = load_image('attack_motion.png')
            Cappy4.y = [270, 270, 270]
        Cappy4.x, Cappy4.y = 150, Cappy4.y[random.randint(0, 2)]
        Cappy4.font = load_font('ENCR10B.TTF', 15)
        Cappy4.HP = 200    #체력
        Cappy4.Attack = 20  #공격력
        Cappy4.Mana = 2  #소환에 필요한 마나 소모량
        Cappy4.frame = 0
        Cappy4.fisrt_time = 0
        Cappy4.timer = 100
        Cappy4.colliding = True

        Cappy4.attack_sound = load_wav('army_attack4.ogg')
        Cappy4.attack_sound.set_volume(50)

    def attacking(Cappy4, monster):
        Cappy4.attack_sound.play()

    def add_event(Cappy4, event):
        pass

    def update(Cappy4):
        Cappy4.x = clamp(25, Cappy4.x, 1600 - 25)

        if Cappy4.colliding == True:
            Cappy4.frame = (Cappy4.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            Cappy4.x += 2  # 이동속도
        elif Cappy4.colliding == False:
            Cappy4.frame = (Cappy4.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
            Cappy4.x += 0

    def draw(Cappy4):
        if Cappy4.colliding == True:
            Cappy4.image.clip_draw(0, int(Cappy4.frame) * 100, 100, 100, Cappy4.x, Cappy4.y)
            Cappy4.font.draw(Cappy4.x - 60, Cappy4.y + 50, 'HP : %3.2i/200' % int(Cappy4.HP), (0, 0, 0))
        elif Cappy4.colliding == False:
            Cappy4.image_attack_motion.clip_draw(200, int(Cappy4.frame) * 100, 100, 100, Cappy4.x, Cappy4.y)
            Cappy4.font.draw(Cappy4.x - 60, Cappy4.y + 50, 'HP : %3.2i/200' % int(Cappy4.HP), (0, 0, 0))
        #draw_rectangle(*Cappy4.get_bb())

    def handle_event(Cappy4, event):
        pass

    def get_bb(Cappy4):
        return Cappy4.x , Cappy4.y - 40, Cappy4.x + 30, Cappy4.y + 40