from pico2d import *

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
        self.player_state = 0
        # stick

        # crowd
        self.crowd = load_image('resource/crowd_500x15.png')
        self.crowd_x = 0
        self.blue_bar2 = load_image('resource/blue_bar2_500x6.png')
        self.blue_bar = load_image('resource/blue_bar3.png')
        # track
        self.run_track = load_image('resource/throw_run_track.png')
        self.track = load_image('resource/throw_track.png')
        self.run_track_x, self.track_x = 0, 0
        # sky
        self.sky = load_image('resource/sky.png')
        self.sky_x = 0


    def handle_events(self, e):
        pass

    def update(self):
        pass
    def draw(self):
        # sky
        self.sky.clip_draw(self.sky_x, 0, SCREENX, 287, SCREENX / 2, 845, SCREENX, 400)
        # crowd
        self.blue_bar.clip_draw(0, 0, 1921, 249, SCREENX // 2, 405, SCREENX, 250)
        self.crowd.clip_draw(self.crowd_x, 0, 250, 15, SCREENX // 2, 580, SCREENX, 100)
        self.blue_bar2.clip_draw(0, 0, 500, 6, SCREENX // 2, 655, SCREENX, 50)
        # track
        self.run_track.clip_draw(0, 0, 1916, 250, SCREENX // 2, 140, SCREENX, 280)
