from pico2d import *

from title import Title
from game_list import Game_List

SCREENX, SCREENY = 1915, 1015
GAME_NUM = 0


def handle_events():
    global running
    global screen_num

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN and screen_num == 0:
            world.clear()
            screen_num += 1
            world.append(Game_List())
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN and screen_num == 1:
            world.clear()
            screen_num += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and screen_num == 1:
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN and screen_num == 1:
            pass



def reset_world():
    global running
    global world
    global screen_num
    screen_num = 0

    running = True
    world = []

    world.append(Title())


def handle_world():
    for o in world:
        o.handle_events()


def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas(SCREENX, SCREENY)
reset_world()

while running:
    handle_events()
    handle_world()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
