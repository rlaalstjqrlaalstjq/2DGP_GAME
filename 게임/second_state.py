import random
import json
import os

from pico2d import *
import game_framework
import game_world
import math
import last_stage

from bazzi import Bazzi, Bazzi2, Bazzi3, Bazzi4, Bazzi5
from rodu import Rodu, Rodu2, Rodu3, Rodu4
from dio import Dio , Dio2, Dio3, Dio4
from cappy import Cappy , Cappy2, Cappy3, Cappy4
from stage_midnight import Stage_Midnight
from manabar import Manabar
from boss import Boss
from tower import Tower
from selectplayer import SelectPlayer
from monster import Monster1, Monster2, Monster3, Monster4
from heelitem import HeelItem
from brassitem import BrassItem
from heal_icon import Heal_Icon


name = "secondstate"




def collide(a, b):                  # 충돌체크 함수
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global bazzi
    bazzi = Bazzi()
    global bazzi2
    bazzi2 = Bazzi2()
    global bazzi3
    bazzi3 = Bazzi3()
    global bazzi4
    bazzi4 = Bazzi4()
    global bazzi5
    bazzi5 = Bazzi5()

    global dio
    dio = Dio()
    global dio2
    dio2 = Dio2()
    global dio3
    dio3 = Dio3()
    global dio4
    dio4 = Dio4()

    global rodu
    rodu = Rodu()
    global rodu2
    rodu2 = Rodu2()
    global rodu3
    rodu3 = Rodu3()
    global rodu4
    rodu4 = Rodu4()

    global cappy
    cappy = Cappy()
    global cappy2
    cappy2 = Cappy2()
    global cappy3
    cappy3 = Cappy3()
    global cappy4
    cappy4 = Cappy4()

    global stage_midnight
    stage_midnight = Stage_Midnight()
    game_world.add_object(stage_midnight, 0)

    global manabar
    manabar = Manabar()
    game_world.add_object(manabar, 0)

    global selectplayer
    selectplayer = SelectPlayer()
    game_world.add_object(selectplayer, 0)

    global heelitem
    heelitem = HeelItem()

    global heal_icon
    heal_icon = Heal_Icon()
    game_world.add_object(heal_icon, 1)

    global brassitem
    brassitem = BrassItem()

    global tower
    tower = Tower()
    game_world.add_object(tower, 1)

    global boss
    boss = Boss()
    game_world.add_object(boss, 1)

    global monster1
    monster1 = [Monster1() for i in range(20)]
    game_world.add_objects(monster1, 1)
    global monster2
    monster2 = [Monster2() for i in range(15)]
    game_world.add_objects(monster2, 1)
    global monster3
    monster3 = [Monster3() for i in range(10)]
    game_world.add_objects(monster3, 1)
    global monster4
    monster4 = [Monster4() for i in range(5)]
    game_world.add_objects(monster4, 1)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            if manabar.bar_num > 3:
                game_world.add_object(bazzi, 1)
                manabar.bar_num -= 3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            if manabar.bar_num > 3:
                game_world.add_object(bazzi2, 1)
                manabar.bar_num -= 3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            if manabar.bar_num > 3:
                game_world.add_object(bazzi3, 1)
                manabar.bar_num -= 3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            if manabar.bar_num > 3:
                game_world.add_object(bazzi4, 1)
                manabar.bar_num -= 3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
            if manabar.bar_num > 3:
                game_world.add_object(bazzi5, 1)
                manabar.bar_num -= 3
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            if manabar.bar_num > 5:
                game_world.add_object(dio, 1)
                manabar.bar_num -= 5
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_5:
            if manabar.bar_num > 5:
                game_world.add_object(dio2, 1)
                manabar.bar_num -= 5
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_6:
            if manabar.bar_num > 5:
                game_world.add_object(dio3, 1)
                manabar.bar_num -= 5
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_7:
            if manabar.bar_num > 5:
                game_world.add_object(dio4, 1)
                manabar.bar_num -= 5
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_e:
            if manabar.bar_num > 7:
                game_world.add_object(rodu, 1)
                manabar.bar_num -= 7
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            if manabar.bar_num > 7:
                game_world.add_object(rodu2, 1)
                manabar.bar_num -= 7
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
            if manabar.bar_num > 7:
                game_world.add_object(rodu3, 1)
                manabar.bar_num -= 7
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_c:
            if manabar.bar_num > 7:
                game_world.add_object(rodu4, 1)
                manabar.bar_num -= 7
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            if manabar.bar_num > 2:
                game_world.add_object(cappy, 1)
                cappy.handle_event(event)
                manabar.bar_num -= 2
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_v:
            if manabar.bar_num > 2:
                game_world.add_object(cappy2, 1)
                cappy.handle_event(event)
                manabar.bar_num -= 2
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_b:
            if manabar.bar_num > 2:
                game_world.add_object(cappy3, 1)
                cappy.handle_event(event)
                manabar.bar_num -= 2
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            if manabar.bar_num > 2:
                game_world.add_object(cappy4, 1)
                cappy.handle_event(event)
                manabar.bar_num -= 2
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            game_world.add_object(heelitem,1)
            heelitem.handle_event(event)
            if heelitem.can_use == 1:
                tower.HP += 500
                heelitem.can_use -= 1
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_f:
            game_world.add_object(brassitem,1)
            brassitem.handle_event(event)
            if brassitem.can_use == 1:
                boss.HP -= 100
                brassitem.can_use -= 1
            else:
                break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_m:
            game_framework.change_state(last_stage)

def update():

    for game_object in game_world.all_objects():
        game_object.update()

    boss.timer -= 1
    if boss.timer == 0:
        for monster in monster1:
            monster.colliding = True
            monster.stages = 2
        for monster in monster2:
            monster.colliding = True
        for monster in monster3:
            monster.colliding = True
        for monster in monster4:
            monster.colliding = True

        bazzi.colliding = True
        bazzi2.colliding = True
        bazzi3.colliding = True
        bazzi4.colliding = True
        bazzi5.colliding = True
        dio.colliding = True
        dio2.colliding = True
        dio3.colliding = True
        dio4.colliding = True
        cappy.colliding = True
        cappy2.colliding = True
        cappy3.colliding = True
        cappy4.colliding = True
        rodu.colliding = True
        rodu2.colliding = True
        rodu3.colliding = True
        rodu4.colliding = True
        boss.timer = 100


    for monster in monster1:
        if collide(tower, monster):
            monster.colliding = False
            tower.timer -= 1
            if tower.timer == 0:
                monster.attacking(tower)
                tower.HP -= 10
                tower.timer = 100
                if tower.HP <= 0:
                    game_world.remove_object(tower)   # 몬스터 1과 타워 충돌체크
        if collide(bazzi, monster):
            bazzi.colliding = False
            monster.colliding = False
            bazzi.timer -= 1
            if bazzi.timer ==0:
                bazzi.attacking(monster)
                monster.attacking(bazzi)
                bazzi.HP -= 10
                monster.HP -=30
                bazzi.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    bazzi.colliding = True
                elif bazzi.HP <=0:
                    game_world.remove_object(bazzi)

                    monster.colliding = True  # 몬스터 1과 배찌의 충돌체크
        if collide(bazzi2, monster):
            bazzi2.colliding = False
            monster.colliding = False
            bazzi2.timer -= 1
            if bazzi2.timer ==0:
                bazzi2.attacking(monster)
                monster.attacking(bazzi2)
                bazzi2.HP -= 10
                monster.HP -=30
                bazzi2.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    bazzi2.colliding = True
                elif bazzi2.HP <=0:

                    game_world.remove_object(bazzi2)
                    monster.colliding = True    # 배찌2 / 몬스터 1
        if collide(bazzi3, monster):
            bazzi3.colliding = False
            monster.colliding = False
            bazzi3.timer -= 1
            if bazzi3.timer ==0:
                bazzi3.attacking(monster)
                monster.attacking(bazzi3)
                bazzi3.HP -= 10
                monster.HP -=30
                bazzi3.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    bazzi3.colliding = True
                elif bazzi3.HP <=0:
                    game_world.remove_object(bazzi3)
                    # 배찌3 / 몬스터 1
                    monster.colliding = True
        if collide(bazzi4, monster):
            bazzi4.colliding = False
            monster.colliding = False
            bazzi4.timer -= 1
            if bazzi4.timer ==0:
                bazzi4.attacking(monster)
                monster.attacking(bazzi4)
                bazzi4.HP -= 10
                monster.HP -=30
                bazzi4.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    bazzi4.colliding = True
                elif bazzi4.HP <=0:
                    game_world.remove_object(bazzi4)

                    monster.colliding = True      # 배찌4 / 몬스터 1
        if collide(bazzi5, monster):
            bazzi5.colliding = False
            monster.colliding = False
            bazzi5.timer -= 1
            if bazzi5.timer ==0:
                bazzi5.attacking(monster)
                monster.attacking(bazzi5)
                bazzi5.HP -= 10
                monster.HP -=30
                bazzi5.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    bazzi5.colliding = True
                elif bazzi5.HP <=0:
                    game_world.remove_object(bazzi5)

                    monster.colliding = True     # 배찌5 / 몬스터 1
        if collide(dio, monster):
            dio.colliding = False
            monster.colliding = False
            dio.timer -= 1
            if dio.timer ==0:
                dio.attacking(monster)
                monster.attacking(dio)
                dio.HP -= 10
                monster.HP -=50
                dio.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    dio.colliding = True
                elif dio.HP <=0:
                    game_world.remove_object(dio)
                    monster.colliding = True            # 몬스터 1과 디오 충돌체크
        if collide(dio2, monster):
            dio2.colliding = False
            monster.colliding = False
            dio2.timer -= 1
            if dio2.timer ==0:
                dio2.attacking(monster)
                monster.attacking(dio2)
                dio2.HP -= 10
                monster.HP -=50
                dio2.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    dio2.colliding = True
                elif dio2.HP <=0:
                    game_world.remove_object(dio2)
                    monster.colliding = True
        if collide(dio3, monster):
            dio3.colliding = False
            monster.colliding = False
            dio3.timer -= 1
            if dio3.timer ==0:
                dio3.attacking(monster)
                monster.attacking(dio3)
                dio3.HP -= 10
                monster.HP -=50
                dio3.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    dio3.colliding = True
                elif dio3.HP <=0:
                    game_world.remove_object(dio3)
                    monster.colliding = True
        if collide(dio4, monster):
            dio4.colliding = False
            monster.colliding = False
            dio4.timer -= 1
            if dio4.timer ==0:
                dio4.attacking(monster)
                monster.attacking(dio4)
                dio4.HP -= 10
                monster.HP -=50
                dio4.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    dio4.colliding = True
                elif dio4.HP <=0:
                    game_world.remove_object(dio4)
                    monster.colliding = True   # 디오 / 몬스터 1
        if collide(cappy, monster):
            cappy.colliding = False
            monster.colliding = False
            cappy.timer -= 1
            if cappy.timer == 0:
                cappy.attacking(monster)
                monster.attacking(cappy)
                cappy.HP -= 10
                monster.HP -= 20
                cappy.timer = 100
                if monster.HP <= 0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    cappy.colliding = True
                elif cappy.HP <= 0:
                    game_world.remove_object(cappy)
                    monster.colliding = True    # 몬스터 1과 캐피 충돌체크
        if collide(cappy2, monster):
            cappy2.colliding = False
            monster.colliding = False
            cappy2.timer -= 1
            if cappy2.timer == 0:
                cappy2.attacking(monster)
                monster.attacking(cappy2)
                cappy2.HP -= 10
                monster.HP -= 20
                cappy2.timer = 100
                if monster.HP <= 0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    cappy2.colliding = True
                elif cappy2.HP <= 0:
                    game_world.remove_object(cappy2)
                    monster.colliding = True
        if collide(cappy3, monster):
            cappy3.colliding = False
            monster.colliding = False
            cappy3.timer -= 1
            if cappy3.timer == 0:
                cappy3.attacking(monster)
                monster.attacking(cappy3)
                cappy3.HP -= 10
                monster.HP -= 20
                cappy3.timer = 100
                if monster.HP <= 0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    cappy3.colliding = True
                elif cappy3.HP <= 0:
                    game_world.remove_object(cappy3)
                    monster.colliding = True
        if collide(cappy4, monster):
            cappy4.colliding = False
            monster.colliding = False
            cappy4.timer -= 1
            if cappy4.timer == 0:
                cappy4.attacking(monster)
                monster.attacking(cappy4)
                cappy4.HP -= 10
                monster.HP -= 20
                cappy4.timer = 100
                if monster.HP <= 0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    cappy4.colliding = True
                elif cappy4.HP <= 0:
                    game_world.remove_object(cappy4)
                    monster.colliding = True
        if collide(rodu, monster):
            rodu.colliding = False
            monster.colliding = False
            rodu.timer -= 1
            if rodu.timer ==0:
                rodu.attacking(monster)
                monster.attacking(rodu)
                rodu.HP -= 10
                monster.HP -=70
                rodu.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    rodu.colliding = True
                elif rodu.HP <=0:
                    game_world.remove_object(rodu)
                    monster.colliding = True           # 몬스터 1과 로두 충돌체크
        if collide(rodu2, monster):
            rodu2.colliding = False
            monster.colliding = False
            rodu2.timer -= 1
            if rodu2.timer ==0:
                rodu2.attacking(monster)
                monster.attacking(rodu2)
                rodu2.HP -= 10
                monster.HP -=70
                rodu2.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    rodu2.colliding = True
                elif rodu2.HP <=0:
                    game_world.remove_object(rodu2)
                    monster.colliding = True
        if collide(rodu3, monster):
            rodu3.colliding = False
            monster.colliding = False
            rodu3.timer -= 1
            if rodu3.timer ==0:
                rodu3.attacking(monster)
                monster.attacking(rodu3)
                rodu3.HP -= 10
                monster.HP -=70
                rodu3.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    rodu3.colliding = True
                elif rodu3.HP <=0:
                    game_world.remove_object(rodu3)
                    monster.colliding = True
        if collide(rodu4, monster):
            rodu4.colliding = False
            monster.colliding = False
            rodu4.timer -= 1
            if rodu4.timer ==0:
                rodu4.attacking(monster)
                monster.attacking(rodu4)
                rodu4.HP -= 10
                monster.HP -=70
                rodu4.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    rodu4.colliding = True
                elif rodu4.HP <=0:
                    game_world.remove_object(rodu4)
                    monster.colliding = True



    for monster in monster2:
        if collide(tower, monster):
            monster.colliding = False
            tower.timer -= 1
            if tower.timer == 0:
                monster.attacking(tower)
                tower.HP -= 20
                tower.timer = 100
                if tower.HP <= 0:
                    game_world.remove_object(tower)   # 몬스터 2과 타워 충돌체크
        if collide(bazzi, monster):
            bazzi.colliding = False
            monster.colliding = False
            bazzi.timer -= 1
            if bazzi.timer ==0:
                bazzi.attacking(monster)
                monster.attacking(bazzi)
                bazzi.HP -= 20
                monster.HP -=30
                bazzi.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    bazzi.colliding = True
                elif bazzi.HP <=0:
                    game_world.remove_object(bazzi)
                    monster.colliding = True           # 몬스터 2과 배찌의 충돌체크
        if collide(bazzi2, monster):
            bazzi2.colliding = False
            monster.colliding = False
            bazzi2.timer -= 1
            if bazzi2.timer ==0:
                bazzi2.attacking(monster)
                monster.attacking(bazzi2)
                bazzi2.HP -= 20
                monster.HP -=30
                bazzi2.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    bazzi2.colliding = True
                elif bazzi2.HP <=0:
                    game_world.remove_object(bazzi2)
                    monster.colliding = True
        if collide(bazzi3, monster):
            bazzi3.colliding = False
            monster.colliding = False
            bazzi3.timer -= 1
            if bazzi3.timer ==0:
                bazzi3.attacking(monster)
                monster.attacking(bazzi3)
                bazzi3.HP -= 20
                monster.HP -=30
                bazzi3.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    bazzi3.colliding = True
                elif bazzi3.HP <=0:
                    game_world.remove_object(bazzi3)
                    monster.colliding = True
        if collide(bazzi4, monster):
            bazzi4.colliding = False
            monster.colliding = False
            bazzi4.timer -= 1
            if bazzi4.timer ==0:
                bazzi4.attacking(monster)
                monster.attacking(bazzi4)
                bazzi4.HP -= 20
                monster.HP -=30
                bazzi4.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    bazzi4.colliding = True
                elif bazzi4.HP <=0:
                    game_world.remove_object(bazzi4)
                    monster.colliding = True
        if collide(bazzi5, monster):
            bazzi5.colliding = False
            monster.colliding = False
            bazzi5.timer -= 1
            if bazzi5.timer ==0:
                bazzi5.attacking(monster)
                monster.attacking(bazzi5)
                bazzi5.HP -= 20
                monster.HP -=30
                bazzi5.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    bazzi5.colliding = True
                elif bazzi5.HP <=0:
                    game_world.remove_object(bazzi5)
                    monster.colliding = True     # 배찌 5 / 몬스터 2
        if collide(dio, monster):
            dio.colliding = False
            monster.colliding = False
            dio.timer -= 1
            if dio.timer ==0:
                dio.attacking(monster)
                monster.attacking(dio)
                dio.HP -= 20
                monster.HP -=50
                dio.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    dio.colliding = True
                elif dio.HP <=0:
                    game_world.remove_object(dio)
                    monster.colliding = True         # 몬스터 2과 디오 충돌체크
        if collide(dio2, monster):
            dio2.colliding = False
            monster.colliding = False
            dio2.timer -= 1
            if dio2.timer ==0:
                dio2.attacking(monster)
                monster.attacking(dio2)
                dio2.HP -= 20
                monster.HP -=50
                dio2.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    dio2.colliding = True
                elif dio2.HP <=0:
                    game_world.remove_object(dio2)
                    monster.colliding = True
        if collide(dio3, monster):
            dio3.colliding = False
            monster.colliding = False
            dio3.timer -= 1
            if dio3.timer ==0:
                dio3.attacking(monster)
                monster.attacking(dio3)
                dio3.HP -= 20
                monster.HP -=50
                dio3.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    dio3.colliding = True
                elif dio3.HP <=0:
                    game_world.remove_object(dio3)
                    monster.colliding = True
        if collide(dio4, monster):
            dio4.colliding = False
            monster.colliding = False
            dio4.timer -= 1
            if dio4.timer ==0:
                dio4.attacking(monster)
                monster.attacking(dio4)
                dio4.HP -= 20
                monster.HP -=50
                dio4.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    dio4.colliding = True
                elif dio4.HP <=0:
                    game_world.remove_object(dio4)
                    monster.colliding = True      # 디오4/ 몬스터 2
        if collide(cappy, monster):
            cappy.colliding = False
            monster.colliding = False
            cappy.timer -= 1
            if cappy.timer ==0:
                cappy.attacking(monster)
                monster.attacking(cappy)
                cappy.HP -= 20
                monster.HP -=20
                cappy.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    cappy.colliding = True
                elif cappy.HP <=0:
                    game_world.remove_object(cappy)
                    monster.colliding = True           # 몬스터 2과 캐피 충돌체크
        if collide(cappy2, monster):
            cappy2.colliding = False
            monster.colliding = False
            cappy2.timer -= 1
            if cappy2.timer ==0:
                cappy2.attacking(monster)
                monster.attacking(cappy2)
                cappy2.HP -= 20
                monster.HP -=20
                cappy2.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    cappy2.colliding = True
                elif cappy2.HP <=0:
                    game_world.remove_object(cappy2)
                    monster.colliding = True
        if collide(cappy3, monster):
            cappy3.colliding = False
            monster.colliding = False
            cappy3.timer -= 1
            if cappy3.timer ==0:
                cappy3.attacking(monster)
                monster.attacking(cappy3)
                cappy3.HP -= 20
                monster.HP -=20
                cappy3.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    cappy3.colliding = True
                elif cappy3.HP <=0:
                    game_world.remove_object(cappy3)
                    monster.colliding = True
        if collide(cappy4, monster):
            cappy4.colliding = False
            monster.colliding = False
            cappy4.timer -= 1
            if cappy4.timer ==0:
                cappy4.attacking(monster)
                monster.attacking(cappy4)
                cappy4.HP -= 20
                monster.HP -=20
                cappy4.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    cappy4.colliding = True
                elif cappy4.HP <=0:
                    game_world.remove_object(cappy4)
                    monster.colliding = True
        if collide(rodu, monster):
            rodu.colliding = False
            monster.colliding = False
            rodu.timer -= 1
            if rodu.timer ==0:
                rodu.attacking(monster)
                monster.attacking(rodu)
                rodu.HP -= 20
                monster.HP -=70
                rodu.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    rodu.colliding = True
                elif rodu.HP <=0:
                    game_world.remove_object(rodu)
                    monster.colliding = True           # 몬스터 2과 로두 충돌체크
        if collide(rodu2, monster):
            rodu2.colliding = False
            monster.colliding = False
            rodu2.timer -= 1
            if rodu2.timer ==0:
                rodu2.attacking(monster)
                monster.attacking(rodu2)
                rodu2.HP -= 20
                monster.HP -=70
                rodu2.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    rodu2.colliding = True
                elif rodu2.HP <=0:
                    game_world.remove_object(rodu2)
                    monster.colliding = True
        if collide(rodu3, monster):
            rodu3.colliding = False
            monster.colliding = False
            rodu3.timer -= 1
            if rodu3.timer ==0:
                rodu3.attacking(monster)
                monster.attacking(rodu3)
                rodu3.HP -= 20
                monster.HP -=70
                rodu3.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    rodu3.colliding = True
                elif rodu3.HP <=0:
                    game_world.remove_object(rodu3)
                    monster.colliding = True
        if collide(rodu4, monster):
            rodu4.colliding = False
            monster.colliding = False
            rodu4.timer -= 1
            if rodu4.timer ==0:
                rodu4.attacking(monster)
                monster.attacking(rodu4)
                rodu4.HP -= 20
                monster.HP -=70
                rodu4.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    rodu4.colliding = True
                elif rodu4.HP <=0:
                    game_world.remove_object(rodu4)
                    monster.colliding = True

    for monster in monster3:
        if collide(tower, monster):
            monster.colliding = False
            tower.timer -= 1
            if tower.timer == 0:
                monster.attacking(tower)
                tower.HP -= 20
                tower.timer = 100
                if tower.HP <= 0:
                    game_world.remove_object(tower)   # 몬스터 3과 타워 충돌체크
        if collide(bazzi, monster):
            bazzi.colliding = False
            monster.colliding = False
            bazzi.timer -= 1
            if bazzi.timer ==0:
                bazzi.attacking(monster)
                monster.attacking(bazzi)
                bazzi.HP -= 20
                monster.HP -=30
                bazzi.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    bazzi.colliding = True
                elif bazzi.HP <=0:
                    game_world.remove_object(bazzi)
                    monster.colliding = True            # 몬스터 3과 배찌의 충돌체크
        if collide(bazzi2, monster):
            bazzi2.colliding = False
            monster.colliding = False
            bazzi2.timer -= 1
            if bazzi2.timer ==0:
                bazzi2.attacking(monster)
                monster.attacking(bazzi2)
                bazzi2.HP -= 20
                monster.HP -=30
                bazzi2.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    bazzi2.colliding = True
                elif bazzi2.HP <=0:
                    game_world.remove_object(bazzi2)
                    monster.colliding = True
        if collide(bazzi3, monster):
            bazzi3.colliding = False
            monster.colliding = False
            bazzi3.timer -= 1
            if bazzi3.timer ==0:
                bazzi3.attacking(monster)
                monster.attacking(bazzi3)
                bazzi3.HP -= 20
                monster.HP -=30
                bazzi3.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    bazzi3.colliding = True
                elif bazzi3.HP <=0:
                    game_world.remove_object(bazzi3)
                    monster.colliding = True
        if collide(bazzi4, monster):
            bazzi4.colliding = False
            monster.colliding = False
            bazzi4.timer -= 1
            if bazzi4.timer ==0:
                bazzi4.attacking(monster)
                monster.attacking(bazzi4)
                bazzi4.HP -= 20
                monster.HP -=30
                bazzi4.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    bazzi4.colliding = True
                elif bazzi4.HP <=0:
                    game_world.remove_object(bazzi4)
                    monster.colliding = True
        if collide(bazzi5, monster):
            bazzi5.colliding = False
            monster.colliding = False
            bazzi5.timer -= 1
            if bazzi5.timer ==0:
                bazzi5.attacking(monster)
                monster.attacking(bazzi5)
                bazzi5.HP -= 20
                monster.HP -=30
                bazzi5.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    bazzi5.colliding = True
                elif bazzi5.HP <=0:
                    game_world.remove_object(bazzi5)
                    monster.colliding = True             # 배찌 5 / 몬스터 3
        if collide(dio, monster):
            dio.colliding = False
            monster.colliding = False
            dio.timer -= 1
            if dio.timer ==0:
                dio.attacking(monster)
                monster.attacking(dio)
                dio.HP -= 20
                monster.HP -=50
                dio.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    dio.colliding = True
                elif dio.HP <=0:
                    game_world.remove_object(dio)
                    monster.colliding = True           # 몬스터 3과 디오 충돌체크
        if collide(dio2, monster):
            dio2.colliding = False
            monster.colliding = False
            dio2.timer -= 1
            if dio2.timer ==0:
                dio2.attacking(monster)
                monster.attacking(dio2)
                dio2.HP -= 20
                monster.HP -=50
                dio2.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    dio2.colliding = True
                elif dio2.HP <=0:
                    game_world.remove_object(dio2)
                    monster.colliding = True
        if collide(dio3, monster):
            dio3.colliding = False
            monster.colliding = False
            dio3.timer -= 1
            if dio3.timer ==0:
                dio3.attacking(monster)
                monster.attacking(dio3)
                dio3.HP -= 20
                monster.HP -=50
                dio3.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    dio3.colliding = True
                elif dio3.HP <=0:
                    game_world.remove_object(dio3)
                    monster.colliding = True
        if collide(dio4, monster):
            dio4.colliding = False
            monster.colliding = False
            dio4.timer -= 1
            if dio4.timer ==0:
                dio4.attacking(monster)
                monster.attacking(dio4)
                dio4.HP -= 20
                monster.HP -=50
                dio4.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    dio4.colliding = True
                elif dio4.HP <=0:
                    game_world.remove_object(dio4)
                    monster.colliding = True   # 디오 4/ 몬스터 3
        if collide(cappy, monster):
            cappy.colliding = False
            monster.colliding = False
            cappy.timer -= 1
            if cappy.timer ==0:
                cappy.attacking(monster)
                monster.attacking(cappy)
                cappy.HP -= 20
                monster.HP -=20
                cappy.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    cappy.colliding = True
                elif cappy.HP <=0:
                    game_world.remove_object(cappy)
                    monster.colliding = True           # 몬스터 3과 캐피 충돌체크
        if collide(cappy2, monster):
            cappy2.colliding = False
            monster.colliding = False
            cappy2.timer -= 1
            if cappy2.timer ==0:
                cappy2.attacking(monster)
                monster.attacking(cappy2)
                cappy2.HP -= 20
                monster.HP -=20
                cappy2.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    cappy2.colliding = True
                elif cappy2.HP <=0:
                    game_world.remove_object(cappy2)
                    monster.colliding = True
        if collide(cappy3, monster):
            cappy3.colliding = False
            monster.colliding = False
            cappy3.timer -= 1
            if cappy3.timer ==0:
                monster.attacking(cappy3)
                cappy3.attacking(monster)
                cappy3.HP -= 20
                monster.HP -=20
                cappy3.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    cappy3.colliding = True
                elif cappy3.HP <=0:
                    game_world.remove_object(cappy3)
                    monster.colliding = True
        if collide(cappy4, monster):
            cappy4.colliding = False
            monster.colliding = False
            cappy4.timer -= 1
            if cappy4.timer ==0:
                cappy4.attacking(monster)
                monster.attacking(cappy4)
                cappy4.HP -= 20
                monster.HP -=20
                cappy4.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    cappy4.colliding = True
                elif cappy4.HP <=0:
                    game_world.remove_object(cappy4)
                    monster.colliding = True
        if collide(rodu, monster):
            rodu.colliding = False
            monster.colliding = False
            rodu.timer -= 1
            if rodu.timer ==0:
                rodu.attacking(monster)
                monster.attacking(rodu)
                rodu.HP -= 20
                monster.HP -=70
                rodu.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    rodu.colliding = True
                elif rodu.HP <=0:
                    game_world.remove_object(rodu)
                    monster.colliding = True           # 몬스터 3과 로두 충돌체크
        if collide(rodu2, monster):
            rodu2.colliding = False
            monster.colliding = False
            rodu2.timer -= 1
            if rodu2.timer ==0:
                rodu2.attacking(monster)
                monster.attacking(rodu2)
                rodu2.HP -= 20
                monster.HP -=70
                rodu2.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    rodu2.colliding = True
                elif rodu2.HP <=0:
                    game_world.remove_object(rodu2)
                    monster.colliding = True
        if collide(rodu3, monster):
            rodu3.colliding = False
            monster.colliding = False
            rodu3.timer -= 1
            if rodu3.timer ==0:
                rodu3.attacking(monster)
                monster.attacking(rodu3)
                rodu3.HP -= 20
                monster.HP -=70
                rodu3.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    rodu3.colliding = True
                elif rodu3.HP <=0:
                    game_world.remove_object(rodu3)
                    monster.colliding = True
        if collide(rodu4, monster):
            rodu4.colliding = False
            monster.colliding = False
            rodu4.timer -= 1
            if rodu4.timer ==0:
                rodu4.attacking(monster)
                monster.attacking(rodu4)
                rodu4.HP -= 20
                monster.HP -=70
                rodu4.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    rodu4.colliding = True
                elif rodu4.HP <=0:
                    game_world.remove_object(rodu4)
                    monster.colliding = True

    for monster in monster4:
        if collide(tower, monster):
            monster.colliding = False
            tower.timer -= 1
            if tower.timer == 0:
                monster.attacking(tower)
                tower.HP -= 40
                tower.timer = 100
                if tower.HP <= 0:
                    game_world.remove_object(tower)   # 몬스터 4과 타워 충돌체크
        if collide(bazzi, monster):
            bazzi.colliding = False
            monster.colliding = False
            bazzi.timer -= 1
            if bazzi.timer ==0:
                bazzi.attacking(monster)
                monster.attacking(bazzi)
                bazzi.HP -= 40
                monster.HP -=30
                bazzi.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    bazzi.colliding = True
                elif bazzi.HP <=0:
                    game_world.remove_object(bazzi)
                    monster.colliding = True           # 몬스터 4과 배찌의 충돌체크
        if collide(bazzi2, monster):
            bazzi2.colliding = False
            monster.colliding = False
            bazzi2.timer -= 1
            if bazzi2.timer ==0:
                bazzi2.attacking(monster)
                monster.attacking(bazzi2)
                bazzi2.HP -= 40
                monster.HP -=30
                bazzi2.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    bazzi2.colliding = True
                elif bazzi2.HP <=0:
                    game_world.remove_object(bazzi2)
                    monster.colliding = True
        if collide(bazzi3, monster):
            bazzi3.colliding = False
            monster.colliding = False
            bazzi3.timer -= 1
            if bazzi3.timer ==0:
                bazzi3.attacking(monster)
                monster.attacking(bazzi3)
                bazzi3.HP -= 40
                monster.HP -=30
                bazzi3.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    monster4.remove_object(monster)
                    bazzi3.colliding = True
                elif bazzi.HP <=0:
                    game_world.remove_object(bazzi3)
                    monster.colliding = True
        if collide(bazzi4, monster):
            bazzi4.colliding = False
            monster.colliding = False
            bazzi4.timer -= 1
            if bazzi4.timer ==0:
                bazzi4.attacking(monster)
                monster.attacking(bazzi4)
                bazzi4.HP -= 40
                monster.HP -=30
                bazzi4.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    bazzi4.colliding = True
                elif bazzi4.HP <=0:
                    game_world.remove_object(bazzi4)
                    monster.colliding = True
        if collide(bazzi5, monster):
            bazzi5.colliding = False
            monster.colliding = False
            bazzi5.timer -= 1
            if bazzi5.timer ==0:
                bazzi5.attacking(monster)
                monster.attacking(bazzi5)
                bazzi5.HP -= 40
                monster.HP -=30
                bazzi5.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    bazzi5.colliding = True
                elif bazzi5.HP <=0:
                    game_world.remove_object(bazzi5)  #배찌5 / 몬스터 4
                    monster.colliding = True
        if collide(dio, monster):
            dio.colliding = False
            monster.colliding = False
            dio.timer -= 1
            if dio.timer ==0:
                dio.attacking(monster)
                monster.attacking(dio)
                dio.HP -= 40
                monster.HP -=50
                dio.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    dio.colliding = True
                elif dio.HP <=0:
                    game_world.remove_object(dio)
                    monster.colliding = True         # 몬스터 4과 디오 충돌체크
        if collide(dio2, monster):
            dio2.colliding = False
            monster.colliding = False
            dio2.timer -= 1
            if dio2.timer ==0:
                dio2.attacking(monster)
                monster.attacking(dio2)
                dio2.HP -= 40
                monster.HP -=50
                dio2.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    dio2.colliding = True
                elif dio2.HP <=0:
                    game_world.remove_object(dio2)
                    monster.colliding = True
        if collide(dio4, monster):
            dio4.colliding = False
            monster.colliding = False
            dio4.timer -= 1
            if dio4.timer ==0:
                dio4.attacking(monster)
                monster.attacking(dio4)
                dio4.HP -= 40
                monster.HP -=50
                dio4.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    dio4.colliding = True
                elif dio4.HP <=0:
                    game_world.remove_object(dio4)
                    monster.colliding = True
        if collide(dio3, monster):
            dio3.colliding = False
            monster.colliding = False
            dio3.timer -= 1
            if dio3.timer ==0:
                dio3.attacking(monster)
                monster.attacking(dio3)
                dio3.HP -= 40
                monster.HP -=50
                dio3.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    dio3.colliding = True
                elif dio3.HP <=0:
                    game_world.remove_object(dio3)
                    monster.colliding = True   # 몬스터 4 / 디오 4
        if collide(cappy, monster):
            cappy.colliding = False
            monster.colliding = False
            cappy.timer -= 1
            if cappy.timer ==0:
                cappy.attacking(monster)
                monster.attacking(cappy)
                cappy.HP -= 40
                monster.HP -=20
                cappy.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    cappy.colliding = True
                elif cappy.HP <=0:
                    game_world.remove_object(cappy)
                    monster.colliding = True             # 몬스터 4과 캐피 충돌체크
        if collide(cappy2, monster):
            cappy2.colliding = False
            monster.colliding = False
            cappy2.timer -= 1
            if cappy2.timer ==0:
                cappy2.attacking(monster)
                monster.attacking(cappy2)
                cappy2.HP -= 40
                monster.HP -=20
                cappy2.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    cappy2.colliding = True
                elif cappy2.HP <=0:
                    game_world.remove_object(cappy2)
                    monster.colliding = True
        if collide(cappy3, monster):
            cappy3.colliding = False
            monster.colliding = False
            cappy3.timer -= 1
            if cappy3.timer ==0:
                cappy3.attacking(monster)
                monster.attacking(cappy3)
                cappy3.HP -= 40
                monster.HP -=20
                cappy3.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    cappy3.colliding = True
                elif cappy3.HP <=0:
                    game_world.remove_object(cappy3)
                    monster.colliding = True
        if collide(cappy4, monster):
            cappy4.colliding = False
            monster.colliding = False
            cappy4.timer -= 1
            if cappy4.timer ==0:
                cappy4.attacking(monster)
                monster.attacking(cappy4)
                cappy4.HP -= 40
                monster.HP -=20
                cappy4.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    cappy4.colliding = True
                elif cappy4.HP <=0:
                    game_world.remove_object(cappy4)
                    monster.colliding = True
        if collide(rodu, monster):
            rodu.colliding = False
            monster.colliding = False
            rodu.timer -= 1
            if rodu.timer ==0:
                rodu.attacking(monster)
                monster.attacking(rodu)
                rodu.HP -= 40
                monster.HP -=70
                rodu.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    rodu.colliding = True
                elif rodu.HP <=0:
                    game_world.remove_object(rodu)
                    monster.colliding = True          # 몬스터 4과 로두 충돌체크
        if collide(rodu2, monster):
            rodu2.colliding = False
            monster.colliding = False
            rodu2.timer -= 1
            if rodu2.timer ==0:
                rodu2.attacking(monster)
                monster.attacking(rodu2)
                rodu2.HP -= 40
                monster.HP -=70
                rodu2.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    rodu2.colliding = True
                elif rodu2.HP <=0:
                    game_world.remove_object(rodu2)
                    monster.colliding = True
        if collide(rodu3, monster):
            rodu3.colliding = False
            monster.colliding = False
            rodu3.timer -= 1
            if rodu3.timer ==0:
                rodu3.attacking(monster)
                monster.attacking(rodu3)
                rodu3.HP -= 40
                monster.HP -=70
                rodu3.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    rodu3.colliding = True
                elif rodu3.HP <=0:
                    game_world.remove_object(rodu3)
                    monster.colliding = True
        if collide(rodu4, monster):
            rodu4.colliding = False
            monster.colliding = False
            rodu4.timer -= 1
            if rodu4.timer ==0:
                rodu4.attacking(monster)
                monster.attacking(rodu4)
                rodu4.HP -= 40
                monster.HP -=70
                rodu4.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    rodu4.colliding = True
                elif rodu4.HP <=0:
                    game_world.remove_object(rodu4)
                    monster.colliding = True

    if collide(bazzi, boss):
        bazzi.colliding = False
        bazzi.timer -= 1
        if bazzi.timer == 0:
            bazzi.attacking(monster)
            boss.HP -= 30
            bazzi.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)    # 배찌와 보스의 충돌체크
    if collide(bazzi2, boss):
        bazzi2.colliding = False
        bazzi2.timer -= 1
        if bazzi2.timer == 0:
            bazzi2.attacking(monster)
            boss.HP -= 30
            bazzi2.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)
    if collide(bazzi3, boss):
        bazzi3.colliding = False
        bazzi3.timer -= 1
        if bazzi3.timer == 0:
            bazzi3.attacking(monster)
            boss.HP -= 30
            bazzi3.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)
    if collide(bazzi4, boss):
        bazzi4.colliding = False
        bazzi4.timer -= 1
        if bazzi4.timer == 0:
            bazzi4.attacking(monster)
            boss.HP -= 30
            bazzi4.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)
    if collide(bazzi5, boss):
        bazzi5.colliding = False
        bazzi5.timer -= 1
        if bazzi5.timer == 0:
            bazzi5.attacking(monster)
            boss.HP -= 30
            bazzi5.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)
    if collide(dio, boss):
        dio.colliding = False
        dio.timer -= 1
        if dio.timer == 0:
            dio.attacking(monster)
            boss.HP -= 50
            dio.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)    # 다오 보스의 충돌체크
    if collide(dio2, boss):
        dio2.colliding = False
        dio2.timer -= 1
        if dio2.timer == 0:
            dio2.attacking(monster)
            boss.HP -= 50
            dio2.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)
    if collide(dio3, boss):
        dio3.colliding = False
        dio3.timer -= 1
        if dio3.timer == 0:
            dio3.attacking(monster)
            boss.HP -= 50
            dio3.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)
    if collide(dio4, boss):
        dio4.colliding = False
        dio4.timer -= 1
        if dio4.timer == 0:
            dio4.attacking(monster)
            boss.HP -= 50
            dio4.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)
    if collide(cappy, boss):
        cappy.colliding = False
        cappy.timer -= 1
        if cappy.timer == 0:
            cappy.attacking(monster)
            boss.HP -= 20
            cappy.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)    # 캐피와 보스의 충돌체크
    if collide(cappy2, boss):
        cappy2.colliding = False
        cappy2.timer -= 1
        if cappy2.timer == 0:
            cappy2.attacking(monster)
            boss.HP -= 20
            cappy2.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)
    if collide(cappy3, boss):
        cappy3.colliding = False
        cappy3.timer -= 1
        if cappy3.timer == 0:
            cappy3.attacking(monster)
            boss.HP -= 20
            cappy3.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)
    if collide(cappy4, boss):
        cappy4.colliding = False
        cappy4.timer -= 1
        if cappy4.timer == 0:
            cappy4.attacking(monster)
            boss.HP -= 20
            cappy4.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)
    if collide(rodu, boss):
        rodu.colliding = False
        rodu.timer -= 1
        if rodu.timer == 0:
            rodu.attacking(monster)
            boss.HP -= 70
            rodu.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)    # 로두와 보스의 충돌체크
    if collide(rodu2, boss):
        rodu2.colliding = False
        rodu2.timer -= 1
        if rodu2.timer == 0:
            rodu2.attacking(monster)
            boss.HP -= 70
            rodu2.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)
    if collide(rodu3, boss):
        rodu3.colliding = False
        rodu3.timer -= 1
        if rodu3.timer == 0:
            rodu3.attacking(monster)
            boss.HP -= 70
            rodu3.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)
    if collide(rodu4, boss):
        rodu4.colliding = False
        rodu4.timer -= 1
        if rodu4.timer == 0:
            rodu4.attacking(monster)
            boss.HP -= 70
            rodu4.timer = 100
            if boss.HP <= 0:
                game_world.remove_object(boss)

    if boss.HP <= 0:
        game_framework.change_state(last_stage)


def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()


def exit():
    game_world.clear()




