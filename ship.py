import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,alien_setting,screen):
        '''初始化飞船并设置初始位置'''
        super(Ship,self).__init__()
        self.screen = screen
        #加载飞船图像并获取其矩形外形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #方向标志
        self.mov_right = False
        self.mov_left = False
        self.alien_setting = alien_setting
        self.center = float(self.rect.centerx)

        #将每艘飞船放在屏幕底部中央
        self.center = self.screen_rect.centerx
#        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
                    
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''刷新位置'''
        if self.mov_right:
            self.center += self.alien_setting.speed_factor
            if self.center > 1200:
                #应该用screen的width值
                self.center = 1200
        if self.mov_left:
            self.center -= self.alien_setting.speed_factor
            if self.center <0:
                self.center = 0
        self.rect.centerx = self.center        

    def center_ship(self):
        self.center = self.screen_rect.centerx
        
        
