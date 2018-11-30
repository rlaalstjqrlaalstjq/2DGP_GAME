import random
import json
import os

from pico2d import *
import game_framework
import game_world
import math

from bazzi import Bazzi
from rodu import Rodu
from dio import Dio
from cappy import Cappy
from grass import Grass
from manabar import Manabar
from boss import Boss
from tower import Tower
from selectplayer import SelectPlayer
from monster import Monster1, Monster2, Monster3, Monster4
from heelitem import HeelItem


name = "MainState"




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

    global dio
    dio = Dio()

    global rodu
    rodu = Rodu()

    global cappy
    cappy = Cappy()

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global manabar
    manabar = Manabar()
    game_world.add_object(manabar, 0)

    global selectplayer
    selectplayer = SelectPlayer()
    game_world.add_object(selectplayer, 0)

    global heelitem
    heelitem = HeelItem()

    global tower
    tower = Tower()
    game_world.add_object(tower, 1)

    global boss
    boss = Boss()
    game_world.add_object(boss, 1)

    global monster1
    monster1 = [Monster1() for i in range(10)]
    game_world.add_objects(monster1, 1)
    global monster2
    monster2 = [Monster2() for i in range(10)]
    game_world.add_objects(monster2, 1)
    global monster3
    monster3 = [Monster3() for i in range(10)]
    game_world.add_objects(monster3, 1)
    global monster4
    monster4 = [Monster4() for i in range(10)]
    game_world.add_objects(monster4, 1)


def exit():
    game_world.clear()

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
            game_world.add_object(bazzi, 1)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            game_world.add_object(dio, 1)
            dio.handle_event(event)
            manabar.bar_num -= dio.Mana
        elif event.type == SDL_KEYDOWN and event.key == SDLK_e:
            game_world.add_object(rodu, 1)
            rodu.handle_event(event)
            manabar.bar_num -= rodu.Mana
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_world.add_object(cappy, 1)
            cappy.handle_event(event)
            manabar.bar_num -= cappy.Mana
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            game_world.add_object(heelitem,0)
            heelitem.handle_event(event)
            tower.HP += 500

def update():
    get_time()
    for game_object in game_world.all_objects():
        game_object.update()

    for monster in monster1:
        if collide(bazzi, monster):
            bazzi.colliding = False
            monster.colliding = False
            bazzi.timer -= 1
            if bazzi.timer ==0:
                bazzi.HP -= 10
                monster.HP -=10
                bazzi.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    bazzi.colliding = True
                    monster.colliding = True
                elif bazzi.HP <=0:
                    game_world.remove_object(bazzi)
                    monster.colliding = True
                    bazzi.colliding = True              # 몬스터 1과 배찌의 충돌체크
        if collide(dio, monster):
            dio.colliding = False
            monster.colliding = False
            dio.timer -= 1
            if dio.timer ==0:
                dio.HP -= 10
                monster.HP -=10
                dio.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    dio.colliding = True
                    monster.colliding = True
                elif dio.HP <=0:
                    game_world.remove_object(dio)
                    monster.colliding = True
                    dio.colliding = True             # 몬스터 1과 디오 충돌체크
        if collide(cappy, monster):
            cappy.colliding = False
            monster.colliding = False
            cappy.timer -= 1
            if cappy.timer ==0:
                cappy.HP -= 10
                monster.HP -=10
                cappy.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    cappy.colliding = True
                    monster.colliding = True
                elif cappy.HP <=0:
                    game_world.remove_object(cappy)
                    monster.colliding = True
                    cappy.colliding = True             # 몬스터 1과 캐피 충돌체크
        if collide(rodu, monster):
            rodu.colliding = False
            monster.colliding = False
            rodu.timer -= 1
            if rodu.timer ==0:
                rodu.HP -= 10
                monster.HP -=10
                rodu.timer = 100
                if monster.HP <=0:
                    monster1.remove(monster)
                    game_world.remove_object(monster)
                    rodu.colliding = True
                    monster.colliding = True
                elif rodu.HP <=0:
                    game_world.remove_object(rodu)
                    monster.colliding = True
                    rodu.colliding = True             # 몬스터 1과 로두 충돌체크

    for monster in monster2:
        if collide(bazzi, monster):
            bazzi.colliding = False
            monster.colliding = False
            bazzi.timer -= 1
            if bazzi.timer ==0:
                bazzi.HP -= 10
                monster.HP -=10
                bazzi.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    bazzi.colliding = True
                    monster.colliding = True
                elif bazzi.HP <=0:
                    game_world.remove_object(bazzi)
                    monster.colliding = True
                    bazzi.colliding = True              # 몬스터 2과 배찌의 충돌체크
        if collide(dio, monster):
            dio.colliding = False
            monster.colliding = False
            dio.timer -= 1
            if dio.timer ==0:
                dio.HP -= 10
                monster.HP -=10
                dio.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    dio.colliding = True
                    monster.colliding = True
                elif dio.HP <=0:
                    game_world.remove_object(dio)
                    monster.colliding = True
                    dio.colliding = True             # 몬스터 2과 디오 충돌체크
        if collide(cappy, monster):
            cappy.colliding = False
            monster.colliding = False
            cappy.timer -= 1
            if cappy.timer ==0:
                cappy.HP -= 10
                monster.HP -=10
                cappy.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    cappy.colliding = True
                    monster.colliding = True
                elif cappy.HP <=0:
                    game_world.remove_object(cappy)
                    monster.colliding = True
                    cappy.colliding = True             # 몬스터 2과 캐피 충돌체크
        if collide(rodu, monster):
            rodu.colliding = False
            monster.colliding = False
            rodu.timer -= 1
            if rodu.timer ==0:
                rodu.HP -= 10
                monster.HP -=10
                rodu.timer = 100
                if monster.HP <=0:
                    monster2.remove(monster)
                    game_world.remove_object(monster)
                    rodu.colliding = True
                    monster.colliding = True
                elif rodu.HP <=0:
                    game_world.remove_object(rodu)
                    monster.colliding = True
                    rodu.colliding = True             # 몬스터 2과 로두 충돌체크

    for monster in monster3:
        if collide(bazzi, monster):
            bazzi.colliding = False
            monster.colliding = False
            bazzi.timer -= 1
            if bazzi.timer ==0:
                bazzi.HP -= 10
                monster.HP -=10
                bazzi.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    bazzi.colliding = True
                    monster.colliding = True
                elif bazzi.HP <=0:
                    game_world.remove_object(bazzi)
                    monster.colliding = True
                    bazzi.colliding = True              # 몬스터 3과 배찌의 충돌체크
        if collide(dio, monster):
            dio.colliding = False
            monster.colliding = False
            dio.timer -= 1
            if dio.timer ==0:
                dio.HP -= 10
                monster.HP -=10
                dio.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    dio.colliding = True
                    monster.colliding = True
                elif dio.HP <=0:
                    game_world.remove_object(dio)
                    monster.colliding = True
                    dio.colliding = True             # 몬스터 3과 디오 충돌체크
        if collide(cappy, monster):
            cappy.colliding = False
            monster.colliding = False
            cappy.timer -= 1
            if cappy.timer ==0:
                cappy.HP -= 10
                monster.HP -=10
                cappy.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    cappy.colliding = True
                    monster.colliding = True
                elif cappy.HP <=0:
                    game_world.remove_object(cappy)
                    monster.colliding = True
                    cappy.colliding = True             # 몬스터 3과 캐피 충돌체크
        if collide(rodu, monster):
            rodu.colliding = False
            monster.colliding = False
            rodu.timer -= 1
            if rodu.timer ==0:
                rodu.HP -= 10
                monster.HP -=10
                rodu.timer = 100
                if monster.HP <=0:
                    monster3.remove(monster)
                    game_world.remove_object(monster)
                    rodu.colliding = True
                    monster.colliding = True
                elif rodu.HP <=0:
                    game_world.remove_object(rodu)
                    monster.colliding = True
                    rodu.colliding = True             # 몬스터 3과 로두 충돌체크

    for monster in monster4:
        if collide(bazzi, monster):
            bazzi.colliding = False
            monster.colliding = False
            bazzi.timer -= 1
            if bazzi.timer ==0:
                bazzi.HP -= 10
                monster.HP -=10
                bazzi.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    bazzi.colliding = True
                    monster.colliding = True
                elif bazzi.HP <=0:
                    game_world.remove_object(bazzi)
                    monster.colliding = True
                    bazzi.colliding = True              # 몬스터 4과 배찌의 충돌체크
        if collide(dio, monster):
            dio.colliding = False
            monster.colliding = False
            dio.timer -= 1
            if dio.timer ==0:
                dio.HP -= 10
                monster.HP -=10
                dio.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    dio.colliding = True
                    monster.colliding = True
                elif dio.HP <=0:
                    game_world.remove_object(dio)
                    monster.colliding = True
                    dio.colliding = True             # 몬스터 4과 디오 충돌체크
        if collide(cappy, monster):
            cappy.colliding = False
            monster.colliding = False
            cappy.timer -= 1
            if cappy.timer ==0:
                cappy.HP -= 10
                monster.HP -=10
                cappy.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    cappy.colliding = True
                    monster.colliding = True
                elif cappy.HP <=0:
                    game_world.remove_object(cappy)
                    monster.colliding = True
                    cappy.colliding = True             # 몬스터 4과 캐피 충돌체크
        if collide(rodu, monster):
            rodu.colliding = False
            monster.colliding = False
            rodu.timer -= 1
            if rodu.timer ==0:
                rodu.HP -= 10
                monster.HP -=10
                rodu.timer = 100
                if monster.HP <=0:
                    monster4.remove(monster)
                    game_world.remove_object(monster)
                    rodu.colliding = True
                    monster.colliding = True
                elif rodu.HP <=0:
                    game_world.remove_object(rodu)
                    monster.colliding = True
                    rodu.colliding = True             # 몬스터 4과 로두 충돌체크

def draw():
    clear_canvas()


    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()







