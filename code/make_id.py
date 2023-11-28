from pico2d import *
import game_world
from game_list import Game_List

SCREENX, SCREENY = 1915, 1015

class MakeID:
    def __init__(self):
        self.background = load_image('resource/make_id_background.png')
        self.select_box = load_image('resource/select_box.png')
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'SPACE', 'ENTER']
        self.select = 0
        self.font = load_font('Font/DungGeunMo.ttf', 80)
        self.box_x, self.box_y, self.box_size = 1000, 460, 100
        self.ID = ''
        self.color = 0
        self.bgm = load_music('MUSIC/select_name_bgm.mp3')
        self.bgm.repeat_play()
        pass

    def update(self):
        self.color = (self.color + 1)%4

        match(self.select):
            case 0:
                self.box_x, self.box_y = 1000, 460
                self.box_size = 100
                pass
            case 1:
                self.box_x, self.box_y = 1140, 460
                self.box_size = 100
                pass
            case 2:
                self.box_x, self.box_y = 1280, 460
                self.box_size = 100
            case 3:
                self.box_x, self.box_y = 1420, 460
                self.box_size = 100
            case 4:
                self.box_x, self.box_y = 1560, 460
                self.box_size = 100
            case 5:
                self.box_x, self.box_y = 1680, 420
                self.box_size = 100
            case 6:
                self.box_x, self.box_y = 1740, 360
                self.box_size = 100
            case 7:
                self.box_x, self.box_y = 1800, 300
                self.box_size = 100
            case 8:
                self.box_x, self.box_y = 1800, 200
                self.box_size = 100
            case 9:
                self.box_x, self.box_y = 1740, 120
                self.box_size = 100
            case 10:
                self.box_x, self.box_y = 1660, 80
                self.box_size = 100
            case 11:
                self.box_x, self.box_y = 1520, 80
                self.box_size = 100
            case 12:
                self.box_x, self.box_y = 1380, 80
                self.box_size = 100
            case 13:
                self.box_x, self.box_y = 1240, 80
                self.box_size = 100
            case 14:
                self.box_x, self.box_y = 1100, 80
                self.box_size = 100
            case 15:
                self.box_x, self.box_y = 960, 80
                self.box_size = 100
            case 16:
                self.box_x, self.box_y = 820, 80
                self.box_size = 100
            case 17:
                self.box_x, self.box_y = 670, 80
                self.box_size = 100
            case 18:
                self.box_x, self.box_y = 520, 80
                self.box_size = 100
            case 19:
                self.box_x, self.box_y = 370, 80
                self.box_size = 100
            case 20:
                self.box_x, self.box_y = 230, 80
                self.box_size = 100
            case 21:
                self.box_x, self.box_y = 160, 120
                self.box_size = 100
            case 22:
                self.box_x, self.box_y = 90, 210
                self.box_size = 100
            case 23:
                self.box_x, self.box_y = 90, 300
                self.box_size = 100
            case 24:
                self.box_x, self.box_y = 150, 380
                self.box_size = 100
            case 25:
                self.box_x, self.box_y = 220, 440
                self.box_size = 100
            case 26:
                self.box_x, self.box_y = 450, 460
                self.box_size = 300
            case 27:
                self.box_x, self.box_y = 750, 460
                self.box_size = 300

        pass
    def draw(self):
        self.background.clip_draw(0, 0, 1280, 720, SCREENX / 2, SCREENY / 2, SCREENX, SCREENY)
        self.select_box.clip_draw(0, 0, 35, 35, self.box_x, self.box_y, self.box_size, 100)

        if self.color == 0:
            self.font.draw(650, 600, "ENTER YOUR NAME", (255, 255, 255))
            self.font.draw(1000, 350, "PLAYER", (255, 255, 255))
            self.font.draw(1000, 250, f'{self.ID}', (255, 255, 255))
        elif self.color == 1:
            self.font.draw(650, 600, "ENTER YOUR NAME", (255, 0, 0))
            self.font.draw(1000, 350, "PLAYER", (255, 0, 0))
            self.font.draw(1000, 250, f'{self.ID}', (255, 0, 0))
        elif self.color == 2:
            self.font.draw(650, 600, "ENTER YOUR NAME", (255, 255, 0))
            self.font.draw(1000, 350, "PLAYER", (255, 255, 0))
            self.font.draw(1000, 250, f'{self.ID}', (255, 255, 0))
        elif self.color == 3:
            self.font.draw(650, 600, "ENTER YOUR NAME", (0, 0, 255))
            self.font.draw(1000, 350, "PLAYER", (0, 0, 255))
            self.font.draw(1000, 250, f'{self.ID}', (0, 0, 255))
        pass

    def handle_events(self, e):
        if e.type == SDL_KEYDOWN and e.key == SDLK_LEFT:
            if self.select == 0:
                self.select = 27
            else:
                self.select -= 1
        elif e.type == SDL_KEYDOWN and e.key == SDLK_RIGHT:
            if self.select == 27:
                self.select = 0
            else:
                self.select += 1
        elif e.type == SDL_KEYDOWN and e.key == SDLK_RETURN:
            if self.select == 26:
                self.ID += ' '
            elif self.select == 27:
                game_list = Game_List(self.ID)
                game_world.add_object(game_list, 0)
            else:
                self.ID += self.alphabet[self.select]
        pass

    def get_ID(self):
        return self.ID