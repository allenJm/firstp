import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,alien_setting,screen):
        super().__init__()
        self.alien_setting = alien_setting
        self.screen = screen
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
#    def update_position(self):
#        self.screen.blit(self.image,self.rect)   
  
        
    def update(self):
        #+1和-1乘以移动因子刚好实现左右移动的控制  
        self.x += (self.alien_setting.alien_speed_factor*
                    self.alien_setting.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        '''检测外星人是否碰撞边缘，碰撞返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True
            
        
    
