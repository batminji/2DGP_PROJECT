from pico2d import *
import math

SCREENX, SCREENY = 1915, 1015
PI = 3.141592
Velocity = 8

# state

class LongJump:
    def __init__(self):
        # player
        self.player_walk = load_image('JUMP_PLAYER/player_walk.png')
        self.player_run = load_image('JUMP_PLAYER/player_run.png')
        self.player_longjump = load_image('JUMP_PLAYER/player_longjump.png')
        self.player_win = load_image('JUMP_PLAYER/player_win.png')
        self.player_state = 'WALK'
        self.player_frame, self.player_x, self.player_y, self.player_time = 0, -75, 225, 0
        self.player_frame_cnt = 0

        # track
        self.track = load_image('JUMP_PLAYER/long_jump_track.png')
        self.track_bar = load_image('JUMP_PLAYER/long_jump_track_bar.png')
        self.big_grass = load_image('JUMP_PLAYER/big_grass.png')
        self.small_grass = load_image('JUMP_PLAYER/small_grass.png')
        self.sand = load_image('JUMP_PLAYER/long_jump_sand.png')
        self.record = load_image('JUMP_PLAYER/record.png')
        self.sand_mark = load_image('JUMP_PLAYER/landing_mark.png')
        self.sand_mark_x, self.sand_mark_y = 0, 0
        self.track_x, self.grass_x, self.sand_x, self.record_x = 1333, 0, 3800, 3000

        # crowd
        self.blue_bar = load_image('resource/blue_bar_500x25.png')
        self.crowd = load_image('resource/crowd_500x15.png')
        self.crowd_x = 0
        self.blue_bar2 = load_image('resource/blue_bar2_500x6.png')

        # sky
        self.sky = load_image('resource/sky.png')
        self.sky_x = 0

        # arrow
        self.arrow = load_image('resource/arrow.png')
        self.arrow_x, self.arrow_y, self.angle = 0, 0, 0
        self.angle_dir = True
        self.angle_cnt = 0

    def handle_events(self, e):
        if self.player_state == 'READY' and e.type == SDL_KEYDOWN and e.key == SDLK_SPACE:
            self.player_state = 'JUMP'
            not_radian_angle = self.angle * 180 // PI
            print(not_radian_angle)

    def update(self):
        if self.player_state == 'WALK':
            self.player_walk_move()
        elif self.player_state == 'RUN':
            self.player_run_move()
        elif self.player_state == 'READY':
            self.arrow_move()
        elif self.player_state == 'JUMP':
            self.player_jump_move()
        elif self.player_state == 'LANDING':
            self.player_landing_move()
        elif self.player_state == 'WIN':
            self.player_win_move()

    def player_win_move(self):
        self.player_frame_cnt += 1
        if self.player_frame_cnt > 5:
            self.player_frame = (self.player_frame + 1) % 2
            self.player_frame_cnt = 0

    def player_landing_move(self):
        self.player_frame_cnt += 1
        if self.player_frame_cnt >= 10:
            self.player_state = 'WIN'
            self.player_frame = 0
            self.player_x += 100
            self.player_frame_cnt = 0

    def player_jump_move(self):
        not_radian_angle = self.angle * 180 // PI
        self.player_x = self.player_x + 5 * max(abs(math.cos(not_radian_angle)), 0.1) * self.player_time
        self.player_y = self.player_y + 10 * math.sin(not_radian_angle) - 0.05 * (self.player_time ** 2)
        self.player_time += 1
        if self.player_y <= 225:
            self.player_frame += 1
            self.player_state = 'LANDING'
            self.player_frame_cnt = 0
            self.sand_mark_x = self.player_x
            self.sand_mark_y = self.player_y - 75
        if self.player_frame < 4:
            self.player_frame_cnt += 1
            if self.player_frame_cnt == 5:
                self.player_frame += 1
                self.player_frame_cnt = 0

    def arrow_move(self):
        self.arrow_x = self.player_x + 100 * math.cos(self.angle)
        self.arrow_y = self.player_y + 100 * math.sin(self.angle)
        if self.angle_dir:
            self.angle -= 0.1
            if (self.angle <= -0.5):
                self.angle_dir = False
        else:
            self.angle += 0.1
            if (self.angle >= 1.0):
                self.angle_dir = True

    def player_run_move(self):
        self.player_frame = (self.player_frame + 1) % 6
        if self.track_x >= -900:
            self.track_x -= 20
            self.sand_x -= 20
            self.record_x -= 20
        elif self.track_x <= -900:
            self.player_x += 20
        if self.player_x <= 200:
            self.player_x += 20
        if self.player_x >= 250:
            self.player_state = 'READY'
            self.player_frame = 0

    def player_walk_move(self):
        self.player_frame = (self.player_frame + 1) % 9
        self.player_x += 5
        if self.player_x >= 100:
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
        self.track.clip_draw(0, 0, 2667, 80, self.track_x , 150, 2667, 100)

        # sand
        self.sand.clip_draw(0, 0, 450, 38, self.sand_x, 150, 2700, 228)

        # sand mark
        if self.player_state == 'LANDING' or self.player_state == 'WIN':
            self.sand_mark.clip_draw(0, 0, 51, 24, self.sand_mark_x, self.sand_mark_y, 51, 24)

        # record
        self.record.clip_draw(0, 0, 152, 10, self.record_x, 300, 760, 50)

        # arrow
        if self.player_state == 'READY':
            self.arrow.clip_composite_draw(0, 0, 120, 120, self.angle, '', self.arrow_x, self.arrow_y, 50, 50)

        # player
        if self.player_state == 'WALK':
            self.player_walk.clip_draw(self.player_frame * 50, 0, 50, 100, self.player_x, self.player_y, 75, 150)
        elif self.player_state == 'RUN':
            self.player_run.clip_draw(self.player_frame * 93, 0, 93, 96, self.player_x, self.player_y, 150, 150)
        elif self.player_state == 'READY':
            self.player_longjump.clip_draw(0, 0, 66, 96, self.player_x, self.player_y, 100, 150)
        elif self.player_state == 'JUMP':
            self.player_longjump.clip_draw(self.player_frame * 66, 0, 66, 96, self.player_x, self.player_y, 100, 150)
        elif self.player_state == 'LANDING':
            self.player_longjump.clip_draw(self.player_frame * 66, 0, 66, 96, self.player_x, self.player_y, 100, 150)
        elif self.player_state == 'WIN':
            self.player_win.clip_draw(self.player_frame * 72, 0, 72, 96, self.player_x, self.player_y, 112, 150)