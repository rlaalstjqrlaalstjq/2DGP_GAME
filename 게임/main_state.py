import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from manabar import Manabar
from boss import Boss
from tower import Tower
from selectplayer import SelectPlayer


name = "MainState"

boy = None

def enter():
    global boy
    boy = Boy()
    grass = Grass()
    manabar = Manabar()
    boss = Boss()
    tower = Tower()
    selectplayer = SelectPlayer()
    game_world.add_object(grass, 0)
    game_world.add_object(manabar, 1)
    game_world.add_object(selectplayer, 2)
    game_world.add_object(boss, 3)
    game_world.add_object(tower, 4)
    game_world.add_object(boy, 5)


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
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






