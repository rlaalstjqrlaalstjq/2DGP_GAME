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

monsters =[]



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
    monster1 = [Monster1()]
    game_world.add_objects(monster1, 1)
    global monster2
    monster2 = [Monster2()]
    game_world.add_objects(monster2, 1)
    global monster3
    monster3 = [Monster3()]
    game_world.add_objects(monster3, 1)
    global monster4
    monster4 = [Monster4()]
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
            bazzi.handle_event(event)
            manabar.bar_num -= bazzi.Mana

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
            monster1.remove(monster)
            game_world.remove_object(monster)

def draw():
    clear_canvas()


    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()







