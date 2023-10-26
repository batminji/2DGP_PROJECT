from pico2d import *
import game_world
from marathon import Marathon
from vault import Vault

SCREENX, SCREENY = 1915, 1015


class Game_List:
    def __init__(self):
        self.frame = 0
        self.image = load_image('resource/game_list.png')
        self.star = load_image('resource/star55x383.png')
        self.star_frame = 0

    def update(self):
        self.star_frame = (self.star_frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 723, 0, 723, 383, SCREENX // 2, SCREENY // 2, SCREENX, SCREENY)
        self.star.clip_draw(self.star_frame * 55, 0, 55, 383, 100, SCREENY // 2, 120, SCREENY)
        self.star.clip_draw(self.star_frame * 55, 0, 55, 383, 1815, SCREENY // 2, 120, SCREENY)

    def handle_events(self, e):
        if e.type == SDL_KEYDOWN and e.key == SDLK_UP:
            if self.frame > 0:
                self.frame -= 1
        elif e.type == SDL_KEYDOWN and e.key == SDLK_DOWN:
            if self.frame < 4:
                self.frame += 1
        elif e.type == SDL_KEYDOWN and e.key == SDLK_RETURN:
            if self.frame == 0:
                game_world.clear()
                marathon = Marathon()
                game_world.add_object(marathon, 0)
            elif self.frame == 1:
                game_world.clear()
                vault = Vault()
                game_world.add_object(vault, 0)
            elif self.frame == 2:
                pass
            elif self.frame == 3:
                pass
            elif self.frame == 4:
                pass