import sys
import pygame
from setting import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_function as gf
from pygame.sprite import Group 
from button import Button
from scoreboard import Scoreboard


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    alien_setting = Settings()#设置实例 
    screen = pygame.display.set_mode(
        (alien_setting.screen_width,alien_setting.screen_height))

    pygame.display.set_caption('Alien Invasion')
    #创建一个飞船
    ship = Ship(alien_setting,screen)
    #creat Group
    bullets = Group()
 #   alien = Alien(alien_setting,screen)
    aliens = Group()
    stats = GameStats(alien_setting)#状态实例
    play_button = Button(alien_setting,screen,"play")
    sb = Scoreboard(screen,alien_setting,stats)   
    gf.create_fleet(alien_setting,screen,ship,aliens)#产生残影，放到主循环外才行    
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(sb,alien_setting,screen,ship,bullets,aliens,
            stats,play_button)
        if stats.game_active :
            ship.update()
            gf.update_bullet(sb,stats,bullets,aliens,alien_setting,ship,screen)
            gf.update_alien(sb,alien_setting,aliens,ship,stats,bullets,screen) 
#gf.create_fleet(alien_setting,screen,ship,aliens)#产生残影，放到主循环外才行        

        #刷新显示屏幕
        gf.update_screen(sb,alien_setting,screen,ship,bullets,
            aliens,stats,play_button)

run_game()                
