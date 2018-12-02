from pico2d import *
import game_framework
import main_state

name = "TitleState"
image = None

class Title:
    def __init__(self):
        self.bgm = load_music('title_bgm.ogg')
        self.bgm.set_volume(30)
        self.bgm.repeat_play()


def enter():
    global image
    image = load_image('title_stage.png')
    global bgm
    bgm = load_music('title_bgm.ogg')
    bgm.set_volume(30)
    bgm.repeat_play()


def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)

def draw():
    clear_canvas()
    image.draw(780,350)
    update_canvas()

def update():
        pass

def pause():
        pass

def resume():
        pass

