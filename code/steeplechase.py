from pico2d import *

SCREENX, SCREENY = 1915, 1015


# state
# 0 : 걷기
# 1 : 준비
# 2 : 달리기
# 3 : 점프하기
# 4 : 넘어짐
# 5 : 이김
# 6 : 짐

class Steeplechase:
    def __init__(self):
        # track
        self.track = load_image('resource/steeplechase_track.png')
        self.ai_track_x, self.player_track_x = 0, 0
        self.hurdle = load_image('resource/hurdle.png')
        self.hurdle_falldown = load_image('resource/hurdle_falldown.png')
        self.hurdle_state = []
        self.ai_hurdle_x, self.player_hurdle_x = [], []
        for i in range(5):
            self.hurdle_state.append(0) # 0 : common 1 : fall down
            self.ai_hurdle_x.append(1000 + i * 500)
            self.player_hurdle_x.append(1000 + i * 500)
        # grass
        self.bottom_grass = load_image('resource/long_grass_2257x24.png')
        self.top_grass = load_image('resource/long_grass2_160x8.png')
        self.bottom_grass_x, self.top_grass_x = 0, 0
        # crowd
        self.blue_bar = load_image('resource/blue_bar_500x25.png')
        self.crowd = load_image('resource/crowd_500x15.png')
        self.crowd_x = 0
        self.blue_bar2 = load_image('resource/blue_bar2_500x6.png')
        # sky
        self.sky = load_image('resource/sky.png')
        self.sky_x = 0
        # ai player
        self.ai_walk = load_image('STEEPLE_AI/ai_walk.png')
        self.ai_run = load_image('STEEPLE_AI/ai_run.png')
        self.ai_ready = load_image('STEEPLE_AI/ai_ready.png')
        self.ai_hurdle = load_image('STEEPLE_AI/ai_hurdle.png')
        self.ai_win = load_image('STEEPLE_AI/ai_win.png')
        self.ai_lose = load_image('STEEPLE_AI/ai_lose.png')
        self.ai_x, self.ai_y, self.ai_state, self.ai_frame = 0, 325, 0, 0
        # player
        self.player_walk = load_image('STEEPLE_PLAYER/player_walk.png')
        self.player_run = load_image('STEEPLE_PLAYER/player_run.png')
        self.player_ready = load_image('STEEPLE_PLAYER/player_ready.png')
        self.player_hurdle = load_image('STEEPLE_PLAYER/player_hurdle.png')
        self.player_falldown = load_image('STEEPLE_PLAYER/player_falldown.png')
        self.player_win = load_image('STEEPLE_PLAYER/player_win.png')
        self.player_lose = load_image('STEEPLE_PLAYER/player_lose.png')
        self.player_x, self.player_y, self.player_state, self.player_frame = 0, 325, 0, 0

    def handle_events(self, e):
        pass
    def update(self):
        # background
        if self.ai_state == 2 or self.ai_state == 3 or self.player_state == 2 or self.player_state == 3:
            if self.ai_track_x <= 2371:
                self.bottom_grass_x = (self.bottom_grass_x + 1) % 177
                self.top_grass_x = (self.top_grass_x + 1) % 80
                self.crowd_x = (self.crowd_x + 1) % 250
                self.sky_x = (self.sky_x + 1) % 1915

        # ai player
        if self.ai_state == 0:
            self.ai_frame = (self.ai_frame + 1) % 9
            self.ai_x += 10
            if self.ai_x >= 270:
                self.ai_state, self.ai_frame = 1, 0
        elif self.ai_state == 1:
            delay(0.5)
            self.ai_frame += 1
            if self.ai_frame == 4:
                self.ai_state, self.ai_frame = 2, 0
        elif self.ai_state == 2: # 달리기
            self.ai_frame = (self.ai_frame + 1) % 6

            if self.ai_track_x <= 2371:
                if self.ai_x + 100 >= self.ai_hurdle_x[0] and not (self.ai_x > self.ai_hurdle_x[0]):
                    self.ai_state, self.ai_frame = 3, 0

                for i in range (len(self.ai_hurdle_x)):
                    self.ai_hurdle_x[i] -= 20
                if self.ai_hurdle_x[0] <= 0:
                    self.ai_hurdle_x.pop(0)
                self.ai_track_x += 20
            else:
                if self.ai_x + 100 >= self.ai_hurdle_x[1] and not (self.ai_x > self.ai_hurdle_x[1]):
                    self.ai_state, self.ai_frame = 3, 0
                self.ai_x += 20
        elif self.ai_state == 3: # 점프하기
            if self.ai_track_x <= 2371:
                for i in range (len(self.ai_hurdle_x)):
                    self.ai_hurdle_x[i] -= 20
                if self.ai_hurdle_x[0] <= 0:
                    self.ai_hurdle_x.pop(0)
                self.ai_track_x += 20
            else:
                self.ai_x += 20

            match self.ai_frame:
                case 0:
                    self.ai_y += 30
                    self.ai_frame += 1
                case 1:
                    self.ai_y += 30
                    self.ai_frame += 1
                case 2:
                    self.ai_y += 30
                    self.ai_frame += 1
                case 3:
                    self.ai_y -= 30
                    self.ai_frame += 1
                case 4:
                    self.ai_y -= 30
                    self.ai_frame += 1
                case 5:
                    self.ai_y -= 30
                    self.ai_state, self.ai_frame = 2, 0

    def draw(self):
        # sky
        self.sky.clip_draw(self.sky_x, 0, SCREENX, 287, SCREENX / 2, 845, SCREENX, 400)
        # crowd
        self.blue_bar.clip_draw(0, 0, 500, 25, SCREENX // 2, 430, SCREENX, 200)
        self.crowd.clip_draw(self.crowd_x, 0, 250, 15, SCREENX // 2, 580, SCREENX, 100)
        self.blue_bar2.clip_draw(0, 0, 500, 6, SCREENX // 2, 655, SCREENX, 50)
        # grass
        self.bottom_grass.clip_draw(self.bottom_grass_x, 0, 80, 24, SCREENX // 2, 153, SCREENX, 116)
        self.top_grass.clip_draw(self.top_grass_x, 0, 80, 8, SCREENX // 2, 310, SCREENX, 40)

        # ai_track
        self.track.clip_draw(self.ai_track_x, 0, SCREENX, 130, SCREENX / 2, 275, SCREENX, 130)
        for i in range(len(self.ai_hurdle_x)):
            self.hurdle.clip_draw(0, 0, 70, 130, self.ai_hurdle_x[i], 275, 70, 130)

        # player track
        self.track.clip_draw(self.player_track_x, 0, SCREENX, 130, SCREENX / 2, 80, SCREENX, 130)
        for i in range(len(self.player_hurdle_x)):
            if self.hurdle_state[i] == 0:
                self.hurdle.clip_draw(0, 0, 70, 130, self.player_hurdle_x[i], 80, 70, 130)
            elif self.hurdle_state[i] == 1:
                self.hurdle_falldown.clip_draw(0, 0, 127, 130, self.player_hurdle_x[i], 127, 130)

        # ai_player
        if self.ai_state == 0: # 걷기
            self.ai_walk.clip_draw(self.ai_frame * 50, 0, 50, 100, self.ai_x, self.ai_y, 75, 150)
        elif self.ai_state == 1: # 준비
            self.ai_ready.clip_draw(self.ai_frame * 96, 0, 96, 96, self.ai_x, self.ai_y, 150, 150)
        elif self.ai_state == 2: # 달리기
            self.ai_run.clip_draw(self.ai_frame * 93, 0, 93, 96, self.ai_x, self.ai_y, 150, 150)
        elif self.ai_state == 3: # 점프하기
            self.ai_hurdle.clip_draw(self.ai_frame * 78, 0, 78, 96, self.ai_x, self.ai_y, 125, 150)
        elif self.ai_state == 4: # 넘어지기
            pass
        elif self.ai_state == 5: # 이김
            pass
        elif self.ai_state == 6: # 짐
            pass

        # player
