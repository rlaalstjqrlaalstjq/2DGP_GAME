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


class Bazzi:
    image = None

    def __init__(Bazzi):
        if Bazzi.image == None:
            Bazzi.image = load_image('Bazzi.png')

        Bazzi.y = [270, 270, 270]
        Bazzi.x, Bazzi.y = random.randint(0, 150), Bazzi.y[random.randint(0, 2)]
        Bazzi.font = load_font('ENCR10B.TTF', 15)
        Bazzi.HP = 350    #체력
        Bazzi.Attack = 50  #공격력
        Bazzi.Mana = 3  #소환에 필요한 마나 소모량
        Bazzi.frame = 0
        Bazzi.fisrt_time = 0
        Bazzi.timer = 100
        Bazzi.colliding = True
        Bazzi.live_num = 0

        Bazzi.attack_sound = load_wav('army_attack.ogg')
        Bazzi.attack_sound.set_volume(50)

    def attacking(Bazzi, monster):
        Bazzi.attack_sound.play()

    def add_event(Bazzi, event):
        pass

    def update(Bazzi):
         Bazzi.frame = (Bazzi.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
         Bazzi.x = clamp(25, Bazzi.x, 1600 - 25)

         if Bazzi.colliding == True:
             Bazzi.x += 3  # 이동속도
         elif Bazzi.colliding == False:
             Bazzi.x += 0

    def draw(Bazzi):
        Bazzi.image.clip_draw(0, int(Bazzi.frame) * 100, 100, 100, Bazzi.x, Bazzi.y)
        Bazzi.font.draw(Bazzi.x - 60, Bazzi.y + 50, 'HP : %3.2i/350' % int(Bazzi.HP), (0, 0, 0))
        draw_rectangle(*Bazzi.get_bb())

    def handle_event(Bazzi, event):
        pass

    def get_bb(Bazzi):
        return Bazzi.x , Bazzi.y - 40, Bazzi.x + 30, Bazzi.y + 40   #배찌1


class Bazzi2:
    image = None

    def __init__(Bazzi2):
        if Bazzi2.image == None:
            Bazzi2.image = load_image('Bazzi.png')

        Bazzi2.y = [270, 270, 270]
        Bazzi2.x, Bazzi2.y = random.randint(0, 150), Bazzi2.y[random.randint(0, 2)]
        Bazzi2.font = load_font('ENCR10B.TTF', 15)
        Bazzi2.HP = 350  # 체력
        Bazzi2.Attack = 50  # 공격력
        Bazzi2.Mana = 3  # 소환에 필요한 마나 소모량
        Bazzi2.frame = 0
        Bazzi2.fisrt_time = 0
        Bazzi2.timer = 100
        Bazzi2.colliding = True
        Bazzi2.live_num = 0

        Bazzi2.attack_sound = load_wav('army_attack.ogg')
        Bazzi2.attack_sound.set_volume(50)

    def attacking(Bazzi2, monster):
        Bazzi2.attack_sound.play()

    def add_event(Bazzi2, event):
        pass

    def update(Bazzi2):
        Bazzi2.frame = (Bazzi2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        Bazzi2.x = clamp(25, Bazzi2.x, 1600 - 25)

        if Bazzi2.colliding == True:
            Bazzi2.x += 3  # 이동속도
        elif Bazzi2.colliding == False:
            Bazzi2.x += 0

    def draw(Bazzi2):
        Bazzi2.image.clip_draw(0, int(Bazzi2.frame) * 100, 100, 100, Bazzi2.x, Bazzi2.y)
        Bazzi2.font.draw(Bazzi2.x - 60, Bazzi2.y + 50, 'HP : %3.2i/350' % int(Bazzi2.HP), (0, 0, 0))
        draw_rectangle(*Bazzi2.get_bb())

    def handle_event(Bazzi2, event):
        pass

    def get_bb(Bazzi2):
        return Bazzi2.x, Bazzi2.y - 40, Bazzi2.x + 30, Bazzi2.y + 40

class Bazzi3:
    image = None

    def __init__(Bazzi3):
        if Bazzi3.image == None:
            Bazzi3.image = load_image('Bazzi.png')

        Bazzi3.y = [270, 270, 270]
        Bazzi3.x, Bazzi3.y = random.randint(0, 150), Bazzi3.y[random.randint(0, 2)]
        Bazzi3.font = load_font('ENCR10B.TTF', 15)
        Bazzi3.HP = 350  # 체력
        Bazzi3.Attack = 50  # 공격력
        Bazzi3.Mana = 3  # 소환에 필요한 마나 소모량
        Bazzi3.frame = 0
        Bazzi3.fisrt_time = 0
        Bazzi3.timer = 100
        Bazzi3.colliding = True
        Bazzi3.live_num = 0

        Bazzi3.attack_sound = load_wav('army_attack.ogg')
        Bazzi3.attack_sound.set_volume(50)

    def attacking(Bazzi3, monster):
        Bazzi3.attack_sound.play()

    def add_event(Bazzi3, event):
        pass

    def update(Bazzi3):
        Bazzi3.frame = (Bazzi3.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        Bazzi3.x = clamp(25, Bazzi3.x, 1600 - 25)

        if Bazzi3.colliding == True:
            Bazzi3.x += 3  # 이동속도
        elif Bazzi3.colliding == False:
            Bazzi3.x += 0

    def draw(Bazzi3):
        Bazzi3.image.clip_draw(0, int(Bazzi3.frame) * 100, 100, 100, Bazzi3.x, Bazzi3.y)
        Bazzi3.font.draw(Bazzi3.x - 60, Bazzi3.y + 50, 'HP : %3.2i/350' % int(Bazzi3.HP), (0, 0, 0))
        draw_rectangle(*Bazzi3.get_bb())

    def handle_event(Bazzi3, event):
        pass

    def get_bb(Bazzi3):
        return Bazzi3.x, Bazzi3.y - 40, Bazzi3.x + 30, Bazzi3.y + 40

class Bazzi4:
    image = None

    def __init__(Bazzi4):
        if Bazzi4.image == None:
            Bazzi4.image = load_image('Bazzi.png')

        Bazzi4.y = [270, 270, 270]
        Bazzi4.x, Bazzi4.y = random.randint(0, 150), Bazzi4.y[random.randint(0, 2)]
        Bazzi4.font = load_font('ENCR10B.TTF', 15)
        Bazzi4.HP = 350  # 체력
        Bazzi4.Attack = 50  # 공격력
        Bazzi4.Mana = 3  # 소환에 필요한 마나 소모량
        Bazzi4.frame = 0
        Bazzi4.fisrt_time = 0
        Bazzi4.timer = 100
        Bazzi4.colliding = True
        Bazzi4.live_num = 0

        Bazzi4.attack_sound = load_wav('army_attack.ogg')
        Bazzi4.attack_sound.set_volume(50)

    def attacking(Bazzi4, monster):
        Bazzi4.attack_sound.play()

    def add_event(Bazzi4, event):
        pass

    def update(Bazzi4):
        Bazzi4.frame = (Bazzi4.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        Bazzi4.x = clamp(25, Bazzi4.x, 1600 - 25)

        if Bazzi4.colliding == True:
            Bazzi4.x += 3  # 이동속도
        elif Bazzi4.colliding == False:
            Bazzi4.x += 0

    def draw(Bazzi4):
        Bazzi4.image.clip_draw(0, int(Bazzi4.frame) * 100, 100, 100, Bazzi4.x, Bazzi4.y)
        Bazzi4.font.draw(Bazzi4.x - 60, Bazzi4.y + 50, 'HP : %3.2i/350' % int(Bazzi4.HP), (0, 0, 0))
        draw_rectangle(*Bazzi4.get_bb())

    def handle_event(Bazzi4, event):
        pass

    def get_bb(Bazzi4):
        return Bazzi4.x, Bazzi4.y - 40, Bazzi4.x + 30, Bazzi4.y + 40

class Bazzi5:
    image = None

    def __init__(Bazzi5):
        if Bazzi5.image == None:
            Bazzi5.image = load_image('Bazzi.png')

        Bazzi5.y = [270, 270, 270]
        Bazzi5.x, Bazzi5.y = random.randint(0, 150), Bazzi5.y[random.randint(0, 2)]
        Bazzi5.font = load_font('ENCR10B.TTF', 15)
        Bazzi5.HP = 350  # 체력
        Bazzi5.Attack = 50  # 공격력
        Bazzi5.Mana = 3  # 소환에 필요한 마나 소모량
        Bazzi5.frame = 0
        Bazzi5.fisrt_time = 0
        Bazzi5.timer = 100
        Bazzi5.colliding = True
        Bazzi5.live_num = 0

        Bazzi5.attack_sound = load_wav('army_attack.ogg')
        Bazzi5.attack_sound.set_volume(50)

    def attacking(Bazzi5, monster):
        Bazzi5.attack_sound.play()

    def add_event(Bazzi5, event):
        pass

    def update(Bazzi5):
        Bazzi5.frame = ( Bazzi5.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        Bazzi5.x = clamp(25, Bazzi5.x, 1600 - 25)

        if Bazzi5.colliding == True:
            Bazzi5.x += 3  # 이동속도
        elif Bazzi5.colliding == False:
            Bazzi5.x += 0

    def draw(Bazzi5):
        Bazzi5.image.clip_draw(0, int(Bazzi5.frame) * 100, 100, 100, Bazzi5.x, Bazzi5.y)
        Bazzi5.font.draw(Bazzi5.x - 60, Bazzi5.y + 50, 'HP : %3.2i/350' % int(Bazzi5.HP), (0, 0, 0))
        draw_rectangle(*Bazzi5.get_bb())

    def handle_event(Bazzi5, event):
        pass

    def get_bb(Bazzi5):
        return Bazzi5.x, Bazzi5.y - 40, Bazzi5.x + 30, Bazzi5.y + 40
