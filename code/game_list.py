from pico2d import *

SCREENX, SCREENY = 1915, 1015


class Game_List:
    def __init__(self):
        self.frame = 0
        self.image = load_image('game_list.png')
        self.star = load_image('star55x383.png')
        self.star_frame = 0

    def get_GAME_NUM(self, GAME_NUM):
        self.frame = GAME_NUM

    def update(self):
        self.star_frame = (self.star_frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 723, 0, 723, 383, SCREENX // 2, SCREENY // 2, SCREENX, SCREENY)
        self.star.clip_draw(self.star_frame * 55, 0, 55, 383, 100, SCREENY // 2, 120, SCREENY)
        self.star.clip_draw(self.star_frame * 55, 0, 55, 383, 1815, SCREENY // 2, 120, SCREENY)
