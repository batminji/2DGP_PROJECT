from pico2d import *
import game_world
from game_list import Game_List

SCREENX, SCREENY = 1915, 1015

class MakeID:
    def __init__(self):
        self.background = load_image('resource/make_id_background.png')
        pass
    def update(self):
        pass
    def draw(self):
        self.background.clip_draw(0, 0, 1280, 720, SCREENX / 2, SCREENY / 2, SCREENX, SCREENY)

        pass

    def handle_events(self, e):
        pass