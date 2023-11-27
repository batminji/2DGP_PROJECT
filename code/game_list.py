from pico2d import *
import game_world
from marathon import Marathon
from vault import Vault
from steeplechase import Steeplechase
from javelin_throw import JavelinThrow
from long_jump import LongJump
from gameover import GameOver

SCREENX, SCREENY = 1915, 1015


class Game_List:
    def __init__(self):
        self.frame = 0
        self.image = load_image('resource/game_list.png')
        self.star = load_image('resource/star55x383.png')
        self.star_frame = 0
        self.game_over_button = load_image('resource/game_over_button.png')
        self.game_select_sound = load_music('MUSIC/game_select_sound.wav')

    def update(self):
        self.star_frame = (self.star_frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 723, 0, 723, 383, SCREENX // 2, SCREENY // 2, SCREENX, SCREENY)
        self.star.clip_draw(self.star_frame * 55, 0, 55, 383, 100, SCREENY // 2, 120, SCREENY)
        self.star.clip_draw(self.star_frame * 55, 0, 55, 383, 1815, SCREENY // 2, 120, SCREENY)
        self.game_over_button.clip_draw(0, 0, 213, 200, 1700, 100, 100, 100)

    def handle_events(self, e):
        # 마우스
        if e.type == SDL_MOUSEBUTTONDOWN:
            if(1650 <= e.x <= 1750) and (50 <= 1015 - e.y + 1 <= 150):
                game_world.clear()
                gameover = GameOver()
                game_world.add_object(gameover, 0)


        # 키보드
        if e.type == SDL_KEYDOWN and e.key == SDLK_UP:
            self.game_select_sound.play()
            if self.frame > 0:
                self.frame -= 1
        elif e.type == SDL_KEYDOWN and e.key == SDLK_DOWN:
            self.game_select_sound.play()
            if self.frame < 4:
                self.frame += 1
        elif e.type == SDL_KEYDOWN and e.key == SDLK_RETURN:
            if self.frame == 0:
                game_world.clear()
                marathon = Marathon()
                game_world.add_object(marathon, 0)
            elif self.frame == 1:
                game_world.clear()
                vault = Vault()
                game_world.add_object(vault, 0)
            elif self.frame == 2:
                game_world.clear()
                steeplechase = Steeplechase()
                game_world.add_object(steeplechase, 0)
            elif self.frame == 3:
                game_world.clear()
                javelinthrow = JavelinThrow()
                game_world.add_object(javelinthrow, 0)
                pass
            elif self.frame == 4:
                game_world.clear()
                longjump = LongJump()
                game_world.add_object(longjump, 0)
