import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    def __init__(self,screen,alien_setting,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.alien_setting = alien_setting
        
        self.prep_ships()
        
        # 得分信息所需的字体设置
        self.font = pygame.font.SysFont(None,48)
        self.text_color = (30,30,30)
        
        self.prep_score()
        
    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,
            self.alien_setting.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top + 20
        
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
#        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

    def prep_ships(self):
        ''''''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.alien_setting,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
            

            
            
            
            
            
