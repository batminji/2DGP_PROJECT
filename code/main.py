from pico2d import *

import game_world
from title import Title
from game_list import Game_List
from marathon import Marathon
from vault import Vault

SCREENX, SCREENY = 1915, 1015
GAME_NUM = 0


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            game_world.handle_events(event)

def reset_world():
    global running

    running = True
    title = Title()
    game_world.add_object(title, 0)


def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas(SCREENX, SCREENY)
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
