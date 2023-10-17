from pico2d import*

SCREENX, SCREENY = 1915, 1015

class Marathon:
    def __init__(self):
        self.track1 = load_image('resource/marathon_track1000x17.png')
        self.track1_x = 0
        self.track2 = load_image('resource/marathon_track1000x17.png')
        self.track2_x = 0
        self.grass1 = load_image('resource/long_grass_2257x24.png')
        self.grass2 = load_image('resource/long_grass2_160x8.png')
    def update(self):
        pass
    def draw(self):
        # track
        self.grass1.clip_draw(0, 0, SCREENX, 24, SCREENX // 2, 153, SCREENX, 116)
        self.grass2.clip_draw(0, 0, 160, 8, SCREENX // 2, 310, SCREENX, 40)
        self.track1.clip_draw(self.track1_x, 0, 500, 17, SCREENX // 2, 55, SCREENX, 80)
        self.track2.clip_draw(self.track2_x, 0, 500, 17, SCREENX // 2, 250, SCREENX, 80)
