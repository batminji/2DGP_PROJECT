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

    def handle_events(self, e):
        pass

    def update(self):
        pass
    def draw(self):
        pass