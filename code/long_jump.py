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
        self.player_frame, self.player_x, self.player_y = 0, -75, 225

        # track
        self.track = load_image('JUMP_PLAYER/long_jump_track.png')
        self.track_bar = load_image('JUMP_PLAYER/long_jump_track_bar.png')
        self.big_grass = load_image('JUMP_PLAYER/big_grass.png')
        self.small_grass = load_image('JUMP_PLAYER/small_grass.png')
        self.sand = load_image('JUMP_PLAYER/long_jump_sand.png')
        self.track_x, self.grass_x = 0, 0

        # crowd
        self.blue_bar = load_image('resource/blue_bar_500x25.png')
        self.crowd = load_image('resource/crowd_500x15.png')
        self.crowd_x = 0
        self.blue_bar2 = load_image('resource/blue_bar2_500x6.png')

        # sky
        self.sky = load_image('resource/sky.png')
        self.sky_x = 0

        pass

    def handle_events(self, e):
        pass

    def update(self):
        # background

        # player
        if self.player_state == 'WALK':
            self.player_walk_move()

    def player_walk_move(self):
        self.player_frame = (self.player_frame + 1) % 9
        self.player_x += 5
        if self.player_x >= 200:
            self.player_frame = 0
            self.player_state = 'RUN'

    def draw(self):
        # sky
        self.sky.clip_draw(self.sky_x, 0, SCREENX, 287, SCREENX / 2, 880, SCREENX, 300)
        # crowd
        self.blue_bar.clip_draw(0, 0, 500, 25, SCREENX // 2, 500, SCREENX, 200)
        self.crowd.clip_draw(self.crowd_x, 0, 250, 15, SCREENX // 2, 650, SCREENX, 100)
        self.blue_bar2.clip_draw(0, 0, 500, 6, SCREENX // 2, 725, SCREENX, 50)

        # background
        self.big_grass.clip_draw(self.grass_x, 0, 1000, 99, SCREENX // 2, 50, SCREENX, 100)
        self.big_grass.clip_draw(self.grass_x, 0, 1000, 99, SCREENX // 2, 250, SCREENX, 100)
        self.track_bar.clip_draw(0, 0, 1915, 80, SCREENX // 2, 325, SCREENX, 50)
        self.small_grass.clip_draw(0, 0, 1915, 80, SCREENX // 2, 375, SCREENX, 50)

        # track
        self.track.clip_draw(self.track_x, 0, 1915, 80, SCREENX // 2 , 150, SCREENX, 100)

        # player
        if self.player_state == 'WALK':
            self.player_walk.clip_draw(self.player_frame * 50, 0, 50, 100, self.player_x, self.player_y, 75, 150)
