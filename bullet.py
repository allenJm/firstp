import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,alien_setting,screen,ship):
        ''''''
        super().__init__()
        self.screen = screen
        #
        self.rect = pygame.Rect(0,0,alien_setting.bullet_width,
            alien_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #
        self.y = float(self.rect.y)
        self.color = alien_setting.bullet_color
        self.bullet_spd = alien_setting.bullet_spd

    def update(self):
        self.y -= self.bullet_spd
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
