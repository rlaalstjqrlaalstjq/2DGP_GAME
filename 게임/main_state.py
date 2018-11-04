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
from monster import Monster1
from monster import Monster2


name = "MainState"


def enter():
    global bazzi
    global dio
    global rodu
    global cappy
    global grass
    global manabar
    global selectplayer

    bazzi = Bazzi()
    rodu = Rodu()
    cappy = Cappy()
    dio = Dio()
    grass = Grass()
    manabar = Manabar()
    boss = Boss()
    tower = Tower()
    monster1 = Monster1()
    monster2 = Monster2()


    selectplayer = SelectPlayer()

    game_world.add_object(grass, 0)
    game_world.add_object(manabar, 1)
    game_world.add_object(selectplayer, 2)
    game_world.add_object(boss, 3)
    game_world.add_object(tower, 4)
    game_world.add_object(monster1, 6)
    game_world.add_object(monster2, 10)



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
            game_world.add_object(bazzi, 5)
            bazzi.handle_event(event)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            game_world.add_object(dio, 7)
            dio.handle_event(event)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_e:
            game_world.add_object(rodu, 8)
            rodu.handle_event(event)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_world.add_object(cappy, 9)
            cappy.handle_event(event)

def update():

    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()



    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







