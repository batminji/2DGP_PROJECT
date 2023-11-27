from pico2d import *
import game_world
import time


SCREENX, SCREENY = 1915, 1015

class Score:
    def __init__(self, game_mode, score):
        self.game_mode, self.score = game_mode, score


# state
# 0 : 걷기
# 1 : 준비
# 2 : 달리기
# 3 : 이김
# 4 : 짐

class Marathon:
    def __init__(self):
        # sound
        self.game_start_effect = load_music('MUSIC/game_start_bgm.mp3')
        self.game_start_effect.play()
        self.game_over_effect = load_music('MUSIC/game_over_bgm.mp3')
        # score
        self.score_board = load_image('resource/score_board.png')
        self.score_font = load_font('Font/DungGeunMo.ttf', 60)
        # sky
        self.sky = load_image('resource/sky.png')
        self.sky_x = 0
        # track
        self.track = load_image('resource/marathon_track.png')
        self.player_track_x, self.ai_track_x = 0, 0
        self.grass1 = load_image('resource/long_grass_2257x24.png')
        self.grass2 = load_image('resource/long_grass2_160x8.png')
        self.grass1_x, self.grass2_x = 0, 0
        self.goal_line1 = load_image('resource/goal_line_1.png')
        self.goal_line2 = load_image('resource/goal_line_1.png')
        self.ai_goal_line_x, self.player_goal_line_x = SCREENX + 40, SCREENX + 40
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
        self.ai_x = -500
        self.ai_frame = 0
        self.ai_state = 'WALK'
        # player
        self.player_walk = load_image('PLAYER/player_walk.png')
        self.player_ready = load_image('PLAYER/player_ready.png')
        self.player_run = load_image('PLAYER/player_run.png')
        self.player_lose = load_image('PLAYER/player_lose.png')
        self.player_win = load_image('PLAYER/player_win.png')
        self.player_x = -500
        self.player_frame = 0
        self.player_state = 'WALK'
        self.player_speed = 40
        # timer
        self.ai_timer, self.player_timer = 0, 0
        self.start_time, self.end_time = 0, 0
    def handle_events(self, e):
        if e.type == SDL_KEYDOWN and e.key == SDLK_SPACE:
            if self.player_state == 'RUN':
                if self.player_speed <= 70:
                    self.player_speed += 10


    def update(self):
        self.end_time = get_time()
        # background
        if self.ai_state == 'RUN':
            self.background_move()
        # ai player
        if self.ai_state == 'WALK':
            self.ai_walk_move()
        elif self.ai_state == 'READY':
            self.ai_ready_move()
        elif self.ai_state == 'RUN':
            self.ai_timer = self.end_time - self.start_time
            self.ai_run_move()
        elif self.ai_state == 'WIN':  # 이김
            self.ai_frame = (self.ai_frame + 1) % 2
        elif self.ai_state == 'LOSE':  # 짐
            self.ai_frame = (self.ai_frame + 1) % 2

        # player
        if self.player_state == 'WALK':
            self.player_walk_move()
        elif self.player_state == 'READY':
            self.player_ready_move()
        elif self.player_state == 'RUN':
            self.player_timer = self.end_time - self.start_time
            self.player_frame = (self.player_frame + 1) % 6
            if self.player_track_x < 1450:
                self.player_track_x += self.player_speed
            elif self.player_track_x >= 1450 and self.player_track_x < 1850:
                self.player_track_x += self.player_speed
                self.player_goal_line_x -= self.player_speed * 2.5
            else:
                if self.player_x >= 955 and self.player_x < 1055:  # 기록 측정 하기
                    self.player_x += self.player_speed
                    if self.player_x + 50 >= self.player_goal_line_x:
                        self.goal_line1 = load_image('resource/goal_line_2.png')
                elif self.player_x >= self.player_goal_line_x:  # 기록 비교 후 승리 판정
                    self.player_frame = 0
                    if self.player_timer <= self.ai_timer:
                        self.player_state = 'WIN'
                        self.game_over_effect.play()
                    elif self.player_timer >= self.ai_timer:
                        self.player_state = 'LOSE'
                        self.game_over_effect.play()
                else:
                    self.player_x += 40
        elif self.player_state == 'WIN':
            self.player_frame = (self.player_frame + 1) % 2
        elif self.player_state == 'LOSE':
            self.player_frame = (self.player_frame + 1) % 2

        if self.player_speed >= 20:
            self.player_speed -= 5

    def player_ready_move(self):
        delay(0.5)
        self.player_frame += 1
        if self.player_frame == 4:
            self.player_state, self.player_frame = 'RUN', 0

    def player_walk_move(self):
        self.player_frame = (self.player_frame + 1) % 9
        self.player_x += 10
        if self.player_x >= 330:
            self.player_state, self.player_frame = 'READY', 0

    def ai_run_move(self):
        self.ai_frame = (self.ai_frame + 1) % 6
        if self.ai_track_x < 1450:
            self.ai_track_x += 20
        elif self.ai_track_x >= 1450 and self.ai_track_x < 1850:
            self.ai_track_x += 20
            self.ai_goal_line_x -= 50
        else:
            if self.ai_x >= 955 and self.ai_x < 1055:  # 기록 측정 하기
                self.ai_x += 20
                self.goal_line2 = load_image('resource/goal_line_2.png')
            elif self.ai_x >= self.ai_goal_line_x:  # 기록 비교 후 승리 판정
                self.ai_frame = 0
                if self.ai_timer <= self.player_timer:
                    self.ai_state = 'WIN'
                elif self.ai_timer >= self.player_timer:
                    self.ai_state = 'LOSE'
            else:
                self.ai_x += 20

    def ai_ready_move(self):
        delay(0.5)
        self.ai_frame += 1
        if self.ai_frame == 4:
            self.ai_state, self.ai_frame = 'RUN', 0
            self.start_time = get_time()

    def ai_walk_move(self):
        self.ai_frame = (self.ai_frame + 1) % 9
        self.ai_x += 10
        if self.ai_x >= 330:
            self.ai_state, self.ai_frame = 'READY', 0

    def background_move(self):
        if self.ai_track_x < 1850:
            self.grass1_x = (self.grass1_x + 2) % 177
            self.grass2_x = (self.grass2_x + 2) % 80
            self.crowd_x = (self.crowd_x + 2) % 250
            self.sky_x = (self.sky_x + 2) % 1915

    def draw(self):
        # sky
        self.sky.clip_draw(self.sky_x, 0, SCREENX, 287, SCREENX / 2, 845, SCREENX, 400)
        # crowd
        self.blue_bar.clip_draw(0, 0, 500, 25, SCREENX // 2, 430, SCREENX, 200)
        self.crowd.clip_draw(self.crowd_x, 0, 250, 15, SCREENX // 2, 580, SCREENX, 100)
        self.blue_bar2.clip_draw(0, 0, 500, 6, SCREENX // 2, 655, SCREENX, 50)
        # track
        self.grass1.clip_draw(self.grass1_x, 0, 80, 24, SCREENX // 2, 153, SCREENX, 116)
        self.grass2.clip_draw(self.grass2_x, 0, 80, 8, SCREENX // 2, 310, SCREENX, 40)

        self.track.clip_draw(self.player_track_x, 0, SCREENX, 80, SCREENX // 2, 55, SCREENX, 80)
        self.track.clip_draw(self.ai_track_x, 0, SCREENX, 80, SCREENX // 2, 250, SCREENX, 80)

        self.goal_line1.clip_draw(0, 0, 73, 132, self.player_goal_line_x, 80, 73, 130)
        self.goal_line2.clip_draw(0, 0, 73, 132, self.ai_goal_line_x, 275, 73, 130)

        # ai player
        if self.ai_state == 'WALK':
            self.ai_walk.clip_draw(self.ai_frame * 50, 0, 50, 100, self.ai_x, 325, 75, 150)
        elif self.ai_state == 'READY':
            self.ai_ready.clip_draw(self.ai_frame * 96, 0, 96, 96, self.ai_x, 325, 150, 150)
        elif self.ai_state == 'RUN':
            self.ai_run.clip_draw(self.ai_frame * 93, 0, 93, 96, self.ai_x, 325, 150, 150)
        elif self.ai_state == 'WIN':
            self.ai_win.clip_draw(self.ai_frame * 72, 0, 72, 96, self.ai_x, 325, 100, 150)
        elif self.ai_state == 'LOSE':
            self.ai_lose.clip_draw(self.ai_frame * 48, 0, 48, 96, self.ai_x, 325, 75, 150)

        # player
        if self.player_state == 'WALK':
            self.player_walk.clip_draw(self.player_frame * 50, 0, 50, 100, self.player_x, 125, 75, 150)
        elif self.player_state == 'READY':
            self.player_ready.clip_draw(self.player_frame * 96, 0, 96, 96, self.player_x, 125, 150, 150)
        elif self.player_state == 'RUN':
            self.player_run.clip_draw(self.player_frame * 93, 0, 93, 96, self.player_x, 125, 150, 150)
        elif self.player_state == 'WIN':
            self.player_win.clip_draw(self.player_frame * 72, 0, 72, 96, self.player_x, 125, 100, 150)
        elif self.player_state == 'LOSE':
            self.player_lose.clip_draw(self.player_frame * 48, 0, 48, 96, self.player_x, 125, 75, 150)

        # score
        self.score_board.clip_draw(0, 0, 135, 135, 1650, 850, 500, 300)
        self.score_font.draw(1450, 950, "CPU", (255, 255, 255))
        self.score_font.draw(1450, 900, '%.3f sec'%self.ai_timer, (255, 255, 255))
        self.score_font.draw(1450, 800, "PLAYER", (255, 255, 255))
        self.score_font.draw(1450, 750, '%.3f sec'%self.player_timer, (255, 255, 255))
