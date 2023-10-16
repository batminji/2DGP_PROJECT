from pico2d import *

from title import Title
from game_list import Game_List

SCREENX, SCREENY = 1915, 1015
GAME_NUM = 0


def handle_events():
    global running
    global screen_num
    global game_list
    global GAME_NUM

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        # game start
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN and screen_num == 0:
            world.clear()
            screen_num += 1
            game_list = Game_List()
            world.append(game_list)
        # game choose
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN and screen_num == 1:
            world.clear()
            screen_num += 1
        # game list up down
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and screen_num == 1:
            if GAME_NUM == 0:
                pass
            else:
                GAME_NUM -= 1
                game_list.get_GAME_NUM(GAME_NUM)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN and screen_num == 1:
            if GAME_NUM == 4:
                pass
            else:
                GAME_NUM += 1
                game_list.get_GAME_NUM(GAME_NUM)




def reset_world():
    global running
    global world
    global screen_num
    screen_num = 0

    running = True
    world = []

    world.append(Title())

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
    update_world()
    render_world()
    delay(0.05)

close_canvas()
