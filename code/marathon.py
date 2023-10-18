from pico2d import *

SCREENX, SCREENY = 1915, 1015


# state
# 0 : 걷기
# 1 : 준비
# 2 : 달리기
# 3 : 이김
# 4 : 짐

class Marathon:
    def __init__(self):
        # track
        self.track1 = load_image('resource/marathon_track1000x17.png')
        self.track1_x = 0
        self.track2 = load_image('resource/marathon_track1000x17.png')
        self.track2_x = 0
        self.grass1 = load_image('resource/long_grass_2257x24.png')
        self.grass2 = load_image('resource/long_grass2_160x8.png')
        self.grass1_x, self.grass2_x = 0, 0
        # crowd
        self.blue_bar = load_image('resource/blue_bar_500x25.png')
        self.crowd = load_image('resource/crowd_500x15.png')
        self.crowd_x = 0
        self.blue_bar2 = load_image('resource/blue_bar2_500x6.png')
        # ai player
        self.ai_walk = load_image('AI/ai_walk.png')
        self.ai_ready = load_image('AI/ai_ready.png')
        self.ai_run = load_image('AI/ai_run.png')
        self.ai_lose = load_image('AI/ai_lose.png')
        self.ai_win = load_image('AI/ai_win.png')
        self.ai_x = 0
        self.ai_frame = 0
        self.ai_state = 0
        # player
        self.player_walk = load_image('PLAYER/player_walk.png')
        self.player_ready = load_image('PLAYER/player_ready.png')
        self.player_run = load_image('PLAYER/player_run.png')
        self.player_lose = load_image('PLAYER/player_lose.png')
        self.player_win = load_image('PLAYER/player_win.png')
        self.player_x = 0
        self.player_frame = 0
        self.player_state = 0

    def update(self):
        # background
        if self.ai_state == 2:
            self.grass1_x += 1
            if self.grass1_x >= 177: self.grass1_x = 0
            self.grass2_x += 1
            if self.grass2_x >= 80: self.grass2_x = 0
            self.crowd_x += 1
            if self.crowd_x >= 250: self.crowd_x = 0
        # ai player
        if self.ai_state == 0:
            self.ai_frame = (self.ai_frame + 1) % 9
            self.ai_x += 5
            if self.ai_x >= 260:
                self.ai_state, self.ai_frame = 1, 0
        elif self.ai_state == 1:
            self.ai_frame += 1
            if self.ai_frame == 4:
                self.ai_state, self.ai_frame = 2, 0
        elif self.ai_state == 2:
            self.ai_frame = (self.ai_frame + 1) % 6
            if self.track2_x < 500:
                self.track2_x += 10
            else:
                self.ai_x += 10
        # player
        if self.player_state == 0:
            self.player_frame = (self.player_frame + 1) % 9
            self.player_x += 5
            if self.player_x >= 260:
                self.player_state, self.player_frame = 1, 0
        elif self.player_state == 1:
            self.player_frame += 1
            if self.player_frame == 4:
                self.player_state, self.player_frame = 2, 0
        elif self.player_state == 2:
            self.player_frame = (self.player_frame + 1) % 6
            if self.track1_x < 500:
                self.track1_x += 10
            else:
                self.player_x += 10

    def draw(self):
        # track
        self.grass1.clip_draw(self.grass1_x, 0, 80, 24, SCREENX // 2, 153, SCREENX, 116)
        self.grass2.clip_draw(self.grass2_x, 0, 80, 8, SCREENX // 2, 310, SCREENX, 40)

        self.track1.clip_draw(self.track1_x, 0, 500, 17, SCREENX // 2, 55, SCREENX, 80)
        self.track2.clip_draw(self.track2_x, 0, 500, 17, SCREENX // 2, 250, SCREENX, 80)
        # crowd
        self.blue_bar.clip_draw(0, 0, 500, 25, SCREENX // 2, 430, SCREENX, 200)
        self.crowd.clip_draw(self.crowd_x, 0, 250, 15, SCREENX // 2, 580, SCREENX, 100)
        self.blue_bar2.clip_draw(0, 0, 500, 6, SCREENX // 2, 655, SCREENX, 50)
        # ai player
        if self.ai_state == 0:
            self.ai_walk.clip_draw(self.ai_frame * 50, 0, 50, 100, self.ai_x, 300, 50, 100)
        elif self.ai_state == 1:
            self.ai_ready.clip_draw(self.ai_frame * 96, 0, 96, 96, self.ai_x, 300, 96, 100)
        elif self.ai_state == 2:
            self.ai_run.clip_draw(self.ai_frame * 93, 0, 93, 96, self.ai_x, 300, 96, 100)

        # player
        if self.player_state == 0:
            self.player_walk.clip_draw(self.player_frame * 50, 0, 50, 100, self.player_x, 100, 50, 100)
        elif self.player_state == 1:
            self.player_ready.clip_draw(self.player_frame * 96, 0, 96, 96, self.player_x, 100, 96, 100)
        elif self.player_state == 2:
            self.player_run.clip_draw(self.player_frame * 93, 0, 93, 96, self.player_x, 100, 96, 100)
