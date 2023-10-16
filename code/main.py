from pico2d import *

from title import Title

SCREENX, SCREENY = 1915, 1015


def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            world.remove(title)

def reset_world():
    global running
    global world

    global title

    running = True
    world = []

    title = Title()
    world.append(title)


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
