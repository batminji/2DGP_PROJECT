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
        self.vault_score = load_image('resource/vault_score.png')
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
        # crowd
        self.blue_bar = load_image('resource/blue_bar_500x25.png')
        self.crowd = load_image('resource/crowd_500x15.png')
        self.crowd_x = 0
        self.blue_bar2 = load_image('resource/blue_bar2_500x6.png')
        # judgement
        self.judge = load_image('resource/judge.png')
        self.judge_clap = load_image('resource/judge_clap.png')
        # score
        self.score_board = load_image('SCORE/score_board.png')

    def update(self):
        if self.player_state == 0:
            self.player_frame = (self.player_frame+1) % 9

            self.player_x += 5
        elif self.player_state == 1:
            self.crowd_x += 2
            if self.crowd_x >= 250: self.crowd_x = 0

    def draw(self):
        # score
        self.score_board.clip_draw(0, 0, 255, 93, SCREENX // 2, 845, SCREENX, 335)
        # crowd
        self.blue_bar.clip_draw(0, 0, 500, 25, SCREENX // 2, 430, SCREENX, 200)
        self.crowd.clip_draw(self.crowd_x, 0, 250, 15, SCREENX // 2, 580, SCREENX, 100)
        self.blue_bar2.clip_draw(0, 0, 500, 6, SCREENX // 2, 655, SCREENX, 50)
        # track
        self.grass.clip_draw(0, 0, 40, 40, SCREENX // 2, 230, SCREENX, 460)
        self.track.clip_draw(0, 0, 1915, 24, SCREENX // 2, 200, SCREENX, 80)
        # player
        if self.player_state == 0: # 걸어가기
            self.player_walk.clip_draw(self.player_frame * 50, 0, 50, 100, self.player_x, self.player_y, 75, 150)