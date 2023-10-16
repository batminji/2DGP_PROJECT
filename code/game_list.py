from pico2d import *

SCREENX, SCREENY = 1915, 1015
class Game_List:
    def __init__(self):
        self.frame = 0
        self.image = load_image('game_list.png')
    def get_GAME_NUM(self, GAME_NUM):
        self.frame = GAME_NUM
    def update(self):
        pass
    def draw(self):
        self.image.clip_draw(self.frame * 723, 0, 723, 383, SCREENX // 2, SCREENY // 2, SCREENX, SCREENY)