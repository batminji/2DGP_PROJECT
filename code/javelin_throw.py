from pico2d import *
import math

SCREENX, SCREENY = 1915, 1015
PI = 3.141592
cnt = 0

# state
# 0 : 걷기
# 1 : 들고 달리기
# 2 : 던지기 1
# 3 : 던지기 2

class JavelinThrow:
    def __init__(self, ID):
        self.ID = ID
        # sound
        self.game_start_effect = load_music('MUSIC/game_start_bgm.mp3')
        self.game_start_effect.play()
        self.game_over_effect = load_music('MUSIC/game_over_bgm.mp3')
        self.run_sound = load_music('MUSIC/run_alone_sound.mp3')
        self.throw_sound = load_music('MUSIC/long_jump_sound.mp3')
        # score
        self.score_board = load_image('resource/score_board.png')
        self.score_font = load_font('Font/DungGeunMo.ttf', 60)
        self.score = 0
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
        self.angle_cnt = 0
        # key board
        self.del_key = load_image('KEYBOARD/delete_key.png')
        self.del_key_frame = 0

    def handle_events(self, e):
        if self.player_state == 'THROW_READY' and e.type == SDL_KEYDOWN and e.key == SDLK_SPACE:
            self.player_state = 'THROW'
            self.throw_sound.repeat_play()

    def update(self):
        global cnt
        if self.player_state == 'WALK':
            self.player_walk_move()
        elif self.player_state == 'RUN':
            self.player_run_move()
        elif self.player_state == 'THROW_READY':
            self.arrow_angle_move()
            print(self.angle)
        elif self.player_state == 'THROW':
            self.score += 10
            self.stick_angle_move()
            self.stick_landing_judgement()
        elif self.player_state == 'DONE':
            cnt += 1
            if cnt % 5 == 0:
                self.del_key_frame = (self.del_key_frame + 1) % 2
                cnt = 0

        if self.player_state == 'RUN' or self.player_state == 'THROW':
            self.crowd_x = (self.crowd_x + 1) % 250
            self.sky_x = (self.sky_x + 2) % 1915

    def stick_landing_judgement(self):
        not_radian_angle = self.angle * 180 // PI
        if not_radian_angle < 0.0:
            not_radian_angle = -not_radian_angle
        stick_bottom = self.stick_y - math.sin(not_radian_angle) * 150
        if stick_bottom <= 250:
            self.throw_sound.stop()
            self.player_state = 'DONE'
            self.stick_y = stick_bottom + math.sin(not_radian_angle) * 150
            self.game_over_effect.play()

    def stick_angle_move(self):
        if self.angle > 0.0:
            if self.stick_x <= 1700:
                self.stick_x += 10
            self.stick_y += 10
            self.angle -= 0.01
            if self.player_x >= -75:
                self.player_x -= 10
            if self.track_x >= SCREENX // 2:
                self.track_x -= 10
        elif self.angle < 0.0:
            self.stick_y -= 5
            if self.angle > -1.0:
                self.angle -= 0.01
            if self.player_x >= -75:
                self.player_x -= 10
            if self.track_x >= SCREENX // 2:
                self.track_x -= 10

    def arrow_angle_move(self):
        self.arrow_x = self.player_x + 100 * math.cos(self.angle)
        self.arrow_y = 400 + 100 * math.sin(self.angle)
        if self.angle_dir:
            self.angle -= 0.1
            if (self.angle <= -1):
                self.angle_dir = False
        else:
            self.angle += 0.1
            if (self.angle >= 1):
                self.angle_dir = True

    def player_run_move(self):
        self.player_frame = (self.player_frame + 1) % 9
        self.track_x -= 10
        if (self.player_x >= self.track_x - (SCREENX / 2.0) - 50):
            self.run_sound.stop()
            self.player_state = 'THROW_READY'
            self.player_frame = 0
            self.stick_y = 420

    def player_walk_move(self):
        self.player_x += 5
        self.player_frame = (self.player_frame + 1) % 9
        if self.player_x >= 500:
            self.run_sound.repeat_play()
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
        elif self.player_state == 'THROW':
            self.stick.clip_composite_draw(0, 0, 100, 3, self.angle, '', self.stick_x, self.stick_y, 300, 9)
        elif self.player_state == 'DONE':
            self.stick.clip_composite_draw(0, 0, 100, 3, self.angle, '', self.stick_x, self.stick_y, 300, 9)
            self.del_key.clip_draw(self.del_key_frame * 18, 0, 18, 12, self.stick_x + 200, 240, 90, 60)


        # player
        if self.player_state == 'WALK':
            self.player_walk.clip_draw(self.player_frame * 50, 0, 50, 100, self.player_x, 350, 75, 150)
        elif self.player_state == 'RUN':
            self.player_run.clip_draw(self.player_frame * 96, 0, 96, 96, self.player_x, 350, 150, 150)
        elif self.player_state == 'THROW_READY':
            self.player_throw1.clip_draw(0, 0, 96, 96, self.player_x, 350, 150, 150)
        elif self.player_state == 'THROW':
            self.player_throw2.clip_draw(0, 0, 96, 96, self.player_x, 350, 150, 150)

        # score
        self.score_board.clip_draw(0, 0, 135, 135, 1650, 850, 500, 300)
        self.score_font.draw(1450, 950, f'{self.ID}', (255, 255, 255))
        self.score_font.draw(1450, 850, f'{self.score} meter', (255, 255, 255))

    def get_ID(self):
        return self.ID