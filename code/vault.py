from pico2d import *

SCREENX, SCREENY = 1915, 1015


# state
# 0 : 걷기
# 1 : 달리기
# 2 : 점프
# 3 : 돌기
# 4 : 도착
# 5 : 이김

class Vault:
    def __init__(self):
        # track
        self.grass = load_image('resource/ground_40x40.png')
        self.track = load_image('resource/vault_track.png')
        self.vault_jump_board1 = load_image('resource/vault_jump_board.png')
        self.vault_jump_board2 = load_image('resource/vault_jump_board_2.png')
        self.vault_landing_board = load_image('resource/vault_landing_board.png')
        self.vault_score = load_image('resource/vault_score.png')
        self.vault_board_x = 2000
        # player
        self.player_walk = load_image('VAULT_PLAYER/player_walk.png')
        self.player_run = load_image('VAULT_PLAYER/player_run.png')
        self.player_jump = load_image('VAULT_PLAYER/player_vault_jump.png')
        self.player_rotate = load_image('VAULT_PLAYER/player_vault_rotate.png')
        self.player_finish = load_image('VAULT_PLAYER/player_vault_finish.png')
        self.player_win = load_image('VAULT_PLAYER/player_win.png')
        self.player_x, self.player_y = -50, 280
        self.player_frame = 0
        self.player_state = 0
        self.player_rad = 0
        # crowd
        self.blue_bar = load_image('resource/blue_bar_500x25.png')
        self.crowd = load_image('resource/crowd_500x15.png')
        self.crowd_x = 0
        self.blue_bar2 = load_image('resource/blue_bar2_500x6.png')
        # judgement
        self.judge = load_image('resource/judge.png')
        self.judge_clap = load_image('resource/judge_clap.png')
        self.judge_x, self.judge_frame = 3200, 0
        # score
        self.score = load_image('resource/number.png')
        self.score_frame = 0
        self.score_x = 3000
        self.player_score = 0
        # sky
        self.sky = load_image('resource/sky.png')
        self.sky_x = 0

        global press_a, press_s, press_d
        press_a, press_s, press_d = False, False, True

    def handle_events(self, e):
        global press_a, press_s, press_d
        if self.player_state == 3 and press_d and e.type == SDL_KEYDOWN and e.key == SDLK_a:
            self.player_rad -= 120
            press_a, press_d = press_d, press_a
        if self.player_state == 3 and press_a and e.type == SDL_KEYDOWN and e.key == SDLK_s:
            self.player_rad -= 120
            press_a, press_s = press_s, press_a
        if self.player_state == 3 and press_s and e.type == SDL_KEYDOWN and e.key == SDLK_d:
            self.player_rad -= 120
            press_s, press_d = press_d, press_s

    def update(self):
        if self.player_state == 0:
            self.player_frame = (self.player_frame + 1) % 9
            self.player_x += 5
            if self.player_x >= 250:
                self.player_state += 1
                self.player_frame = 0
        elif self.player_state == 1:
            self.player_frame = (self.player_frame + 1) % 6
            self.crowd_x = (self.crowd_x + 2) % 250
            self.sky_x = (self.sky_x + 2) % 1915
            self.vault_board_x -= 20
            self.judge_x -= 20
            self.score_x -= 20
            if self.vault_board_x <= 200:
                self.player_state += 1
                self.player_frame = 0
        elif self.player_state == 2:
            if self.player_frame == 0:
                self.player_x += 20
                self.player_y += 20
                if self.player_x >= 600:
                    self.player_frame += 1
            elif self.player_frame == 1:
                self.player_x += 20
                self.player_y -= 20
                if self.player_y <= 400:
                    self.player_frame += 1
            elif self.player_frame == 2:
                delay(0.5)
                self.player_frame += 1
            elif self.player_frame == 3:
                delay(0.5)
                self.player_frame += 1
                self.player_x += 30
                self.player_y += 20
            elif self.player_frame == 4:
                delay(0.5)
                self.player_state += 1
                self.player_frame = 0
        elif self.player_state == 3:
            self.player_score = (-self.player_rad) // 360
            self.score_frame = self.player_score
            if self.player_x <= 1200:
                self.player_x += 10
                self.player_y += 10
            else:
                self.player_x += 10
                self.player_y -= 10
                if self.player_y <= 250:
                    self.player_state += 1
                    self.player_y += 50
        elif self.player_state == 4:
            delay(1.5)
            self.player_state += 1
        elif self.player_state == 5:
            delay(0.1)
            self.player_frame = (self.player_frame + 1) % 2
            self.judge_frame = (self.judge_frame + 1) % 2

    def draw(self):
        # sky
        self.sky.clip_draw(self.sky_x, 0, SCREENX, 287, SCREENX / 2, 845, SCREENX, 400)
        # crowd
        self.blue_bar.clip_draw(0, 0, 500, 25, SCREENX // 2, 430, SCREENX, 200)
        self.crowd.clip_draw(self.crowd_x, 0, 250, 15, SCREENX // 2, 580, SCREENX, 100)
        self.blue_bar2.clip_draw(0, 0, 500, 6, SCREENX // 2, 655, SCREENX, 50)
        # track
        self.grass.clip_draw(0, 0, 40, 40, SCREENX // 2, 230, SCREENX, 460)
        self.track.clip_draw(0, 0, 1915, 24, SCREENX // 2, 200, SCREENX, 80)
        # judgement
        if self.player_state < 5:
            self.judge.clip_draw(0, 0, 94, 51, self.judge_x, 360, 300, 180)
        else:
            self.judge_clap.clip_draw(self.judge_frame * 94, 0, 94, 51, self.judge_x, 360, 300, 180)
        # score
        self.vault_score.clip_draw(0, 0, 80, 64, self.score_x, 305, 80, 64)
        self.score.clip_draw(self.score_frame * 16, 0, 16, 14, self.score_x, 310, 32, 28)
        # jump board
        self.vault_jump_board2.clip_draw(0, 0, 170, 63, self.vault_board_x, 220, 170, 63)
        self.vault_jump_board1.clip_draw(0, 0, 145, 89, self.vault_board_x + 600, 260, 220, 150)
        self.vault_landing_board.clip_draw(0, 0, 572, 48, self.vault_board_x + 1400, 210, 700, 100)
        # player
        if self.player_state == 0:  # 걸어가기
            self.player_walk.clip_draw(self.player_frame * 50, 0, 50, 100, self.player_x, self.player_y, 75, 150)
        elif self.player_state == 1:  # 달리기
            self.player_run.clip_draw(self.player_frame * 93, 0, 93, 96, self.player_x, self.player_y, 150, 150)
        elif self.player_state == 2:  # 점프하기
            if self.player_frame == 4:
                self.player_jump.clip_draw(self.player_frame * 133, 0, 133, 133, self.player_x, self.player_y, 180, 180)
            elif self.player_frame == 0:
                self.player_jump.clip_draw(self.player_frame * 133, 0, 133, 133, self.player_x, self.player_y, 140, 140)
            else:
                self.player_jump.clip_draw(self.player_frame * 133, 0, 133, 133, self.player_x, self.player_y, 150, 150)
        elif self.player_state == 3:  # 돌기
            self.player_rotate.clip_composite_draw(0, 0, 59, 67, self.player_rad, '', self.player_x, self.player_y, 90,
                                                   90)
        elif self.player_state == 4:
            self.player_finish.clip_draw(0, 0, 49, 104, self.player_x, self.player_y, 75, 150)
        elif self.player_state == 5:
            self.player_win.clip_draw(self.player_frame * 72, 0, 72, 96, self.player_x, self.player_y, 100, 150)
