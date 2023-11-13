from pico2d import *
import math

SCREENX, SCREENY = 1915, 1015


# state
# 0 : 걷기
# 1 : 들고 달리기
# 2 : 던지기 1
# 3 : 던지기 2

class JavelinThrow:
    def __init__(self):
        # player
        self.player_walk = load_image('THROW_PLAYER/player_walk.png')
        self.player_run = load_image('THROW_PLAYER/player_javelin_run.png')
        self.player_throw1 = load_image('THROW_PLAYER/player_throw_1.png')
        self.player_throw2 = load_image('THROW_PLAYER/player_throw_2.png')
        self.player_state, self.player_x , self.player_frame = 'WALK', -50, 0
        # stick
        self.stick = load_image('resource/stick.png')
        self.stick_x, self.stick_y = 0, 0
        # crowd
        self.crowd = load_image('resource/crowd_500x15.png')
        self.crowd_x = 0
        self.blue_bar2 = load_image('resource/blue_bar2_500x6.png')
        self.blue_bar = load_image('resource/blue_bar3.png')
        # track
        self.run_track = load_image('resource/throw_run_track.png')
        self.track = load_image('resource/throw_track.png')
        self.track_x = 2415
        # sky
        self.sky = load_image('resource/sky.png')
        self.sky_x = 0
        # arrow
        self.arrow = load_image('resource/arrow.png')
        self.arrow_x, self.arrow_y, self.angle = 0, 0, 0
        self.angle_dir = True

    def handle_events(self, e):
        if self.player_state == 'THROW_READY' and e.type == SDL_KEYDOWN and e.key == SDLK_SPACE:

            pass

    def update(self):
        if self.player_state == 'WALK':
            self.player_walk_move()
        elif self.player_state == 'RUN':
            self.player_run_move()
        elif self.player_state == 'THROW_READY':
            self.arrow_x = self.player_x + 100 * math.cos(self.angle)
            self.arrow_y = 400 + 100 * math.sin(self.angle)
            if self.angle_dir:
                self.angle -= 0.1
                if(self.angle <= -1):
                    self.angle_dir = False
            else:
                self.angle += 0.1
                if(self.angle >= 1):
                    self.angle_dir = True
        elif self.player_state == 'THROW':
            pass

    def player_run_move(self):
        self.player_frame = (self.player_frame + 1) % 9
        self.track_x -= 10
        if (self.player_x >= self.track_x - (SCREENX / 2.0) - 50):
            self.player_state = 'THROW_READY'
            self.player_frame = 0
            self.stick_y = 420

    def player_walk_move(self):
        self.player_x += 5
        self.player_frame = (self.player_frame + 1) % 9
        if self.player_x >= 500:
            self.player_state = 'RUN'
            self.player_frame = 0
            self.stick_x, self.stick_y = self.player_x - 20, 400

    def draw(self):
        # sky
        self.sky.clip_draw(self.sky_x, 0, SCREENX, 287, SCREENX / 2, 845, SCREENX, 400)
        # crowd
        self.blue_bar.clip_draw(0, 0, 1921, 249, SCREENX // 2, 405, SCREENX, 250)
        self.crowd.clip_draw(self.crowd_x, 0, 250, 15, SCREENX // 2, 580, SCREENX, 100)
        self.blue_bar2.clip_draw(0, 0, 500, 6, SCREENX // 2, 655, SCREENX, 50)
        # track
        self.run_track.clip_draw(0, 0, 1916, 250, SCREENX // 2, 140, SCREENX, 280)
        self.track.clip_draw(0, 0, 1916, 250, self.track_x, 140, SCREENX, 280)

        # stick & arrow
        if self.player_state == 'RUN':
            self.stick.clip_draw(0, 0, 100, 3, self.stick_x, self.stick_y, 300, 9)
        elif self.player_state == 'THROW_READY':
            self.stick.clip_composite_draw(0, 0, 100, 3, 60, '', self.stick_x, self.stick_y, 300, 9)
            self.arrow.clip_composite_draw(0, 0, 120, 120, self.angle, '', self.arrow_x, self.arrow_y, 50, 50)
        # player
        if self.player_state == 'WALK':
            self.player_walk.clip_draw(self.player_frame * 50, 0, 50, 100, self.player_x, 350, 75, 150)
        elif self.player_state == 'RUN':
            self.player_run.clip_draw(self.player_frame * 96, 0, 96, 96, self.player_x, 350, 150, 150)
        elif self.player_state == 'THROW_READY':
            self.player_throw1.clip_draw(0, 0, 96, 96, self.player_x, 350, 150, 150)
        elif self.player_state == 'THROW':
            self.player_throw2.clip_draw(0, 0, 96, 96, self.player_x, 350, 150, 150)