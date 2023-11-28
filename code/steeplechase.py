from pico2d import *

SCREENX, SCREENY = 1915, 1015

cnt = 0

class Steeplechase:
    def __init__(self, ID):
        self.ID = ID
        # sound
        self.game_start_effect = load_music('MUSIC/game_start_bgm.mp3')
        self.game_start_effect.play()
        self.game_over_effect = load_music('MUSIC/game_over_bgm.mp3')
        self.run_sound = load_music('MUSIC/run_sound.mp3')

        # score
        self.score_board = load_image('resource/score_board.png')
        self.score_font = load_font('Font/DungGeunMo.ttf', 60)
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
        self.ai_x, self.ai_y, self.ai_state, self.ai_frame = -400, 325, 'WALK', 0
        self.ai_goal_line = load_image('resource/goal_line_1.png')
        self.ai_goal_line_x = 3200
        self.ai_score = 0
        # player
        self.player_walk = load_image('STEEPLE_PLAYER/player_walk.png')
        self.player_run = load_image('STEEPLE_PLAYER/player_run.png')
        self.player_ready = load_image('STEEPLE_PLAYER/player_ready.png')
        self.player_hurdle = load_image('STEEPLE_PLAYER/player_hurdle.png')
        self.player_falldown = load_image('STEEPLE_PLAYER/player_falldown.png')
        self.player_win = load_image('STEEPLE_PLAYER/player_win.png')
        self.player_lose = load_image('STEEPLE_PLAYER/player_lose.png')
        self.player_x, self.player_y, self.player_state, self.player_frame = -400, 125, 'WALK', 0
        self.player_goal_line = load_image('resource/goal_line_1.png')
        self.player_goal_line_x = 3700
        self.player_score = 0

        # key board
        self.del_key = load_image('KEYBOARD/delete_key.png')
        self.del_key_frame = 0
        self.space_key = load_image('KEYBOARD/space_key.png')
        self.space_key_frame = 0

    def handle_events(self, e):
        if e.type == SDL_KEYDOWN and e.key == SDLK_SPACE:
            if self.player_state == 'RUN':
                self.player_state = 'JUMP'
                self.player_frame = 0
                self.player_score += 150

    def collide_player_hurdle(self):
        left_a, bottom_a, right_a, top_a = self.player_x, self.player_y - 75, self.player_x + 20, self.player_y + 75
        left_b, bottom_b, right_b, top_b = self.player_hurdle_x[0] - 40, 15, self.player_hurdle_x[0], 145

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

        return True

    def update(self):
        global cnt
        # background
        self.background_move()

        # ai player
        if self.ai_state == 'WALK':
            self.ai_walk_move()
        elif self.ai_state == 'READY':
            self.ai_ready_move()
        elif self.ai_state == 'RUN': # 달리기
            cnt += 1
            if cnt % 5 == 0:
                self.space_key_frame = (self.space_key_frame + 1) % 2
                cnt = 0

            self.ai_frame = (self.ai_frame + 1) % 6
            if self.ai_track_x <= 2371:
                self.ai_track_move()
                if self.ai_x + 100 >= self.ai_hurdle_x[0] and not (self.ai_x > self.ai_hurdle_x[0]):
                    self.ai_state, self.ai_frame = 'JUMP', 0
                    self.ai_score += 150
            else: # track 움직이지 않을 때
                self.ai_track_move_fix()
        elif self.ai_state == 'JUMP': # 점프하기
            self.ai_hurdle_delete()
            self.ai_hurdle_jump_frame()
        elif self.ai_state == 'WIN':
            if cnt % 5 == 0:
                self.ai_frame = (self.ai_frame + 1 ) % 2
        elif self.ai_state == 'LOSE':
            if cnt % 5 == 0:
                self.ai_frame = (self.ai_frame + 1 ) % 2

        # player
        if self.player_state == 'WALK':
            self.player_walk_move()
        elif self.player_state == 'READY':
            self.player_ready_move()
        elif self.player_state == 'RUN': # 달리기
            self.player_frame = (self.player_frame + 1) % 6
            if self.player_track_x <= 2371:
                if self.collide_player_hurdle() and self.hurdle_state[0] == 0:
                    self.player_state, self.player_frame = 'FALLDOWN', 0
                    self.hurdle_state[0] = 1
                    self.player_score -= 150
                for i in range (len(self.player_hurdle_x)):
                    self.player_hurdle_x[i] -= 20
                if self.player_hurdle_x[0] <= 0:
                    self.player_hurdle_x.pop(0)
                    self.hurdle_state[0] = 0
                self.player_track_x += 20
                self.player_goal_line_x -= 20
            else: # track 움직이지 않을 때
                if self.player_x + 100 >= self.player_hurdle_x[1] and not (self.player_x > self.player_hurdle_x[1]) and self.hurdle_state[1] == 0:
                    self.player_state, self.player_frame = 'FALLDOWN', 0
                    self.hurdle_state[1] = 1
                    self.player_score -= 150
                if self.player_x >= self.player_goal_line_x - 40 and self.player_x <= self.player_goal_line_x + 40:  # 기록 측정 하기
                    self.player_x += 20
                    self.player_goal_line = load_image('resource/goal_line_2.png')
                elif self.player_x >= self.player_goal_line_x:  # 기록 비교 후 승리 판정
                    self.player_frame = 0
                    if self.player_score >= self.ai_score:
                        self.player_state = 'WIN'
                        self.run_sound.stop()
                        self.game_over_effect.play()
                    else:
                        self.player_state = 'LOSE'
                        self.run_sound.stop()
                        self.game_over_effect.play()
                else:
                    self.player_x += 20
        elif self.player_state == 'JUMP': # 점프하기
            if self.player_track_x <= 2371:
                for i in range (len(self.player_hurdle_x)):
                    self.player_hurdle_x[i] -= 20
                if self.player_hurdle_x[0] <= 0:
                    self.player_hurdle_x.pop(0)
                self.player_track_x += 20
            else:
                self.player_x += 20

            match self.player_frame:
                case 0:
                    self.player_y += 30
                    self.player_frame += 1
                case 1:
                    self.player_y += 30
                    self.player_frame += 1
                case 2:
                    self.player_y += 30
                    self.player_frame += 1
                case 3:
                    self.player_y -= 30
                    self.player_frame += 1
                case 4:
                    self.player_y -= 30
                    self.player_frame += 1
                case 5:
                    self.player_y -= 30
                    self.player_state, self.player_frame = 'RUN', 0
        elif self.player_state == 'FALLDOWN': # 넘어짐
            self.player_frame += 1
            if self.player_frame == 8:
                self.player_state, self.player_frame = 'RUN', 0
        elif self.player_state == 'WIN': # 이김
            cnt += 1
            if cnt % 5 == 0:
                self.player_frame = (self.player_frame + 1 ) % 2
                self.del_key_frame = (self.del_key_frame + 1) % 2
                cnt = 0
        elif self.player_state == 'LOSE': # 짐
            cnt += 1
            if cnt % 5 == 0:
                self.player_frame = (self.player_frame + 1) % 2
                self.del_key_frame = (self.del_key_frame + 1) % 2
                cnt = 0

    def player_ready_move(self):
        delay(0.5)
        self.player_frame += 1
        if self.player_frame == 4:
            self.player_state, self.player_frame = 'RUN', 0
            self.run_sound.repeat_play()

    def player_walk_move(self):
        self.player_frame = (self.player_frame + 1) % 9
        self.player_x += 10
        if self.player_x >= 270:
            self.player_state, self.player_frame = 'READY', 0

    def ai_hurdle_jump_frame(self):
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
                self.ai_state, self.ai_frame = 'RUN', 0

    def ai_hurdle_delete(self):
        if self.ai_track_x <= 2371:
            for i in range(len(self.ai_hurdle_x)):
                self.ai_hurdle_x[i] -= 20
            if self.ai_hurdle_x[0] <= 0:
                self.ai_hurdle_x.pop(0)
            self.ai_track_x += 20
        else:
            self.ai_x += 20

    def ai_track_move_fix(self):
        if self.ai_x + 100 >= self.ai_hurdle_x[1] and not (self.ai_x > self.ai_hurdle_x[1]):
            self.ai_state, self.ai_frame = 'JUMP', 0
            self.ai_score += 150
        if self.ai_x >= self.ai_goal_line_x - 40 and self.ai_x <= self.ai_goal_line_x + 40:  # 기록 측정 하기
            self.ai_x += 20
            self.ai_goal_line = load_image('resource/goal_line_2.png')
        elif self.ai_x >= self.ai_goal_line_x:  # 기록 비교 후 승리 판정
            self.ai_frame = 0
            if self.ai_score > self.player_score:
                self.ai_state = 'WIN'
            else:
                self.ai_state = 'LOSE'
        else:
            self.ai_x += 20

    def ai_track_move(self):
        self.ai_track_x += 20
        self.ai_goal_line_x -= 20
        for i in range(len(self.ai_hurdle_x)):
            self.ai_hurdle_x[i] -= 20
        if self.ai_hurdle_x[0] <= 0:
            self.ai_hurdle_x.pop(0)

    def ai_ready_move(self):
        delay(0.5)
        self.ai_frame += 1
        if self.ai_frame == 4:
            self.ai_state, self.ai_frame = 'RUN', 0

    def ai_walk_move(self):
        self.ai_frame = (self.ai_frame + 1) % 9
        self.ai_x += 10
        if self.ai_x >= 270:
            self.ai_state, self.ai_frame = 'READY', 0

    def background_move(self):
        if self.ai_state == 'RUN' or self.ai_state == 'JUMP' or self.player_state == 'RUN' or self.player_state == 'JUMP':
            if self.ai_track_x <= 2371:
                self.bottom_grass_x = (self.bottom_grass_x + 1) % 177
                self.top_grass_x = (self.top_grass_x + 1) % 80
                self.crowd_x = (self.crowd_x + 1) % 250
                self.sky_x = (self.sky_x + 1) % 1915

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
        self.ai_goal_line.clip_draw(0, 0, 80, 120, self.ai_goal_line_x, 275, 80, 130)

        # player track
        self.track.clip_draw(self.player_track_x, 0, SCREENX, 130, SCREENX / 2, 80, SCREENX, 130)
        for i in range(len(self.player_hurdle_x)):
            if self.hurdle_state[i] == 0:
                self.hurdle.clip_draw(0, 0, 70, 130, self.player_hurdle_x[i], 80, 70, 130)
            elif self.hurdle_state[i] == 1:
                self.hurdle_falldown.clip_draw(0, 0, 127, 130, self.player_hurdle_x[i], 80, 127, 130)
        self.player_goal_line.clip_draw(0, 0, 80, 120, self.player_goal_line_x, 80, 80, 130)

        # ai_player
        if self.ai_state == 'WALK': # 걷기
            self.ai_walk.clip_draw(self.ai_frame * 50, 0, 50, 100, self.ai_x, self.ai_y, 75, 150)
        elif self.ai_state == 'READY': # 준비
            self.ai_ready.clip_draw(self.ai_frame * 96, 0, 96, 96, self.ai_x, self.ai_y, 150, 150)
        elif self.ai_state == 'RUN': # 달리기
            self.ai_run.clip_draw(self.ai_frame * 93, 0, 93, 96, self.ai_x, self.ai_y, 150, 150)
        elif self.ai_state == 'JUMP': # 점프하기
            self.ai_hurdle.clip_draw(self.ai_frame * 78, 0, 78, 96, self.ai_x, self.ai_y, 125, 150)
        elif self.ai_state == 'WIN': # 이김
            self.ai_win.clip_draw(self.ai_frame * 72, 0, 72, 96, self.ai_x, self.ai_y, 125, 150)
        elif self.ai_state == 'LOSE': # 짐
            self.ai_lose.clip_draw(self.ai_frame * 48, 0, 48, 96, self.ai_x, self.ai_y, 75, 150)

        # player
        if self.player_state == 'WALK': # 걷기
            self.player_walk.clip_draw(self.player_frame * 50, 0, 50, 100, self.player_x, self.player_y, 75, 150)
        elif self.player_state == 'READY': # 준비
            self.player_ready.clip_draw(self.player_frame * 96, 0, 96, 96, self.player_x, self.player_y, 150, 150)
        elif self.player_state == 'RUN': # 달리기
            self.space_key.clip_draw(self.space_key_frame * 26, 0, 26, 12, 150, 100, 130, 60)
            self.player_run.clip_draw(self.player_frame * 93, 0, 93, 96, self.player_x, self.player_y, 150, 150)
        elif self.player_state == 'JUMP': # 점프하기
            self.space_key.clip_draw(self.space_key_frame * 26, 0, 26, 12, 150, 100, 130, 60)
            self.player_hurdle.clip_draw(self.player_frame * 78, 0, 78, 96, self.player_x, self.player_y, 125, 150)
        elif self.player_state == 'FALLDOWN': # 넘어지기
            self.space_key.clip_draw(self.space_key_frame * 26, 0, 26, 12, 150, 100, 130, 60)
            self.player_falldown.clip_draw(self.player_frame * 100, 0, 100, 68, self.player_x, self.player_y, 150, 100)
        elif self.player_state == 'WIN': # 이김
            self.player_win.clip_draw(self.player_frame * 72, 0, 72, 96, self.player_x, self.player_y, 125, 150)
            self.del_key.clip_draw(self.del_key_frame * 18, 0, 18, 12, self.player_x + 100, self.player_y - 75, 90, 60)
        elif self.player_state == 'LOSE': # 짐
            self.player_lose.clip_draw(self.player_frame * 48, 0, 48, 96, self.player_x, self.player_y, 75, 150)
            self.del_key.clip_draw(self.del_key_frame * 18, 0, 18, 12, self.player_x + 100, self.player_y - 75, 90, 60)

        # score
        self.score_board.clip_draw(0, 0, 135, 135, 1650, 850, 500, 300)
        self.score_font.draw(1450, 950, "CPU", (255, 255, 255))
        self.score_font.draw(1450, 900, '%d POINT' % self.ai_score, (255, 255, 255))
        self.score_font.draw(1450, 800, f'{self.ID}', (255, 255, 255))
        self.score_font.draw(1450, 750, '%d POINT' % self.player_score, (255, 255, 255))

    def get_ID(self):
        return self.ID