from pico2d import *

SCREENX, SCREENY = 1915, 1015
class Game_List:
    def __init__(self):
        self.frame = 0
        self.image = load_image('game_list.png')
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and event.key == SDLK_UP:
                if self.frame > 0 :
                    self.frame -= 1
            elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
                if self.frame < 4:
                    self.frame += 1
    def update(self):
        pass
    def draw(self):
        self.image.clip_draw(self.frame * 723, 0, 723, 383, SCREENX // 2, SCREENY // 2, SCREENX, SCREENY)