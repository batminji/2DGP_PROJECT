from pico2d import *

SCREENX, SCREENY = 1915, 1015

class Vault:
    def __init__(self):
        self.grass = load_image('resource/ground_40x40.png')
        self.track = load_image('resource/vault_track.png')
        self.player_walk = load_image('VAULT_PLAYER/player_walk.png')
        self.player_run = load_image('VAULT_PLAYER/player_run.png')
        self.player_jump = load_image('VAULT_PLAYER/player_vault_jump.png')
        self.player_rotate = load_image('VAULT_PLAYER/player_vault_rotate.png')
        self.player_finish = load_image('VAULT_PLAYER/player_vault_finish.png')
        self.player_win = load_image('VAULT_PLAYER/player_win.png')

    def update(self):
        pass

    def draw(self):
        pass
