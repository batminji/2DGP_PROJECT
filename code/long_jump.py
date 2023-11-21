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

        # track
        self.track = load_image('JUMP_PLAYER/long_jump_track.png')
        self.track_bar = load_image('JUMP_PLAYER/long_jump_track_bar.png')
        self.big_grass = load_image('JUMP_PLAYER/big_grass.png')
        self.small_grass = load_image('JUMP_PLAYER/small_grass.png')
        self.sand = load_image('JUMP_PLAYER/long_jump_sand.png')
        self.track_x, self.grass_x = 0, 0

        pass

    def handle_events(self, e):
        pass

    def update(self):
        pass

    def draw(self):
        pass