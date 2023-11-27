from pico2d import *
import random
import game_world
from make_id import MakeID

SCREENX, SCREENY = 1915, 1015


class Title:
    def __init__(self):
        self.background = load_image('resource/title_background.png')
        self.x, self.y = SCREENX // 2, SCREENY // 2
        self.logo = load_image('resource/title_logo.png')
        self.logo_x = 2500
        self.char1 = load_image('PLAYER/player_run.png')
        self.char2 = load_image('AI/ai_run.png')
        self.frame1, self.frame2 = random.randint(0, 6), random.randint(0, 6)
        self.char1_x, self.char2_x = 0, 0
        self.char1_speed, self.char2_speed = 10, 15
        self.bgm = load_music('MUSIC/title_bgm.mp3')
        self.bgm.repeat_play()

    def update(self):
        self.frame1, self.frame2 = (self.frame1 + 1) % 6, (self.frame2 + 1) % 6
        if self.char1_x > SCREENX:
            self.char1_x = 0
        else:
            self.char1_x += self.char1_speed
        if self.char2_x > SCREENX:
            self.char2_x = 0
        else:
            self.char2_x += self.char2_speed
        if self.logo_x >= 1000:
            self.logo_x -= 20

    def draw(self):
        self.background.clip_draw(0, 0, 724, 384, self.x, self.y, SCREENX, SCREENY)
        self.logo.clip_draw(0, 0, 290, 164, self.logo_x, 750, 650, 420)
        self.char1.clip_draw(self.frame1 * 93, 0, 93, 96, self.char1_x, 275, 186, 192)
        self.char2.clip_draw(self.frame2 * 93, 0, 93, 96, self.char2_x, 275, 186, 192)

    def handle_events(self, e):
        if e.type == SDL_KEYDOWN and e.key == SDLK_RETURN:
            game_world.clear()
            self.bgm.stop()
            makeid = MakeID()
            game_world.add_object(makeid, 0)