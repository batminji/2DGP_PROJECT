from pico2d import *
import math

SCREENX, SCREENY = 1915, 1015


# state

class LongJump:
    def __init__(self):
        # player
        self.player_walk = load_image('JUMP_PLAYER/player_walk.png')
        self.player_run = load_image('JUMP_PLAYER/player_run.png')
        self.player_longjump = load_image('JUMP_PLAYER/player_longjump.png')
        self.player_win = load_image('JUMP_PLAYER/player_win.png')
        self.player_state = 'WALK'
        self.player_frame, self.player_x, self.player_y = 0, 0, 0

        pass

    def handle_events(self, e):
        pass

    def update(self):
        pass

    def draw(self):
        pass