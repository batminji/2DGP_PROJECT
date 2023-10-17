from pico2d import*

SCREENX, SCREENY = 1915, 1015

class Marathon:
    def __init__(self):
        # track
        self.track1 = load_image('resource/marathon_track1000x17.png')
        self.track1_x = 0
        self.track2 = load_image('resource/marathon_track1000x17.png')
        self.track2_x = 0
        self.grass1 = load_image('resource/long_grass_2257x24.png')
        self.grass2 = load_image('resource/long_grass2_160x8.png')
        # crowd
        self.blue_bar = load_image('resource/blue_bar_500x25.png')
        self.crowd = load_image('resource/crowd_500x15.png')
        self.crowd_x = 0
        self.blue_bar2 = load_image('resource/blue_bar2_500x6.png')
        # ai player
        self.ai_walk = load_image('resource/ai_walk.png')
        self.ai_ready = load_image('resource/ai_ready.png')
        self.ai_run = load_image('resource/ai_run.png')
        self.ai_lose = load_image('resource/ai_lose.png')
        self.ai_win = load_image('resource/ai_win.png')
        self.ai_x = 0
        self.ai_frame = 0
        # player
        self.player_walk = load_image('resource/ai_walk.png')
        self.player_ready = load_image('resource/player_ready.png')
        self.player_run = load_image('resource/player_run.png')
        self.player_lose = load_image('resource/player_lose.png')
        self.player_win = load_image('resource/player_win.png')
        self.player_x = 0
        self.player_frame = 0

    def update(self):
        pass
    def draw(self):
        # track
        self.grass1.clip_draw(0, 0, SCREENX, 24, SCREENX // 2, 153, SCREENX, 116)
        self.grass2.clip_draw(0, 0, 160, 8, SCREENX // 2, 310, SCREENX, 40)
        self.track1.clip_draw(self.track1_x, 0, 500, 17, SCREENX // 2, 55, SCREENX, 80)
        self.track2.clip_draw(self.track2_x, 0, 500, 17, SCREENX // 2, 250, SCREENX, 80)
        # crowd
        self.blue_bar.clip_draw(0, 0, 500, 25, SCREENX // 2, 430, SCREENX, 200)
        self.crowd.clip_draw(self.crowd_x, 0, 250, 15, SCREENX // 2, 580, SCREENX, 100)
        self.blue_bar2.clip_draw(0, 0, 500, 6, SCREENX // 2, 655, SCREENX, 50)