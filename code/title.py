from pico2d import*
import random

from main import SCREENX, SCREENY

class Title:
    def __init__(self):
        self.background = load_image('title_background.png')
        self.x, self.y = SCREENX // 2, SCREENY // 2
        self.logo = load_image('title_logo.png')
        self.logo_x = 1200
        self.char1 = load_image('player_run.png')
        self.char2 = load_image('ai_run.png')
        self.frame1, self.frame2 = random.randint(0, 6), random.randint(0,6)
        self.char1_x, self.char2_x = 0, 0
        self.char1_speed, self.char2_speed = 10, 20
    def update(self):
        self.frame1, self.frame2 = (self.frame1 + 1) % 6, (self.frame2 + 1) % 6
        self.char1_x += self.char1_speed
        self.char2_x += self.char2_speed
    def handle_event(self):
        pass
    def draw(self):
        self.background.clip_draw(0, 0, 724, 384, self.x, self.y, SCREENX, SCREENY)
        self.logo.clip_draw(0, 0, 290, 164, self.logo_x, 1500, 870, 492)
        self.char1.clip_draw(self.frame1 * 93, 0, 93, 96, self.char1_x, 100, 279, 288)
        self.char2.clip_draw(self.frame2 * 93, 0, 93, 96, self.char2_x, 200, 279, 288)