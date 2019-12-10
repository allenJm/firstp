import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def event_keydown(event,alien_setting,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.mov_right = True
    if event.key == pygame.K_LEFT:
        ship.mov_left = True    
    elif event.key == pygame.K_SPACE:#空格发射子弹
        fir_bullet(alien_setting,screen,ship,bullets)                
    elif event.key == pygame.K_q:
        sys.exit() 
        
def event_keyup(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.mov_right = False
    if event.key == pygame.K_LEFT:
        ship.mov_left= False 
        
def fir_bullet(alien_setting,screen,ship,bullets):
    if len(bullets) <= alien_setting.bullet_num:
        new_bullet = Bullet(alien_setting,screen,ship)
        bullets.add(new_bullet)   
                 
def check_events(sb,alien_setting,screen,ship,bullets,aliens,
        stats,play_button):
    '''检测键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()            
        elif event.type == pygame.KEYDOWN:
            event_keydown(event,alien_setting,screen,ship,bullets)
                    
        elif event.type == pygame.KEYUP:
            event_keyup(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(sb,alien_setting,screen,ship,aliens,
            bullets,stats,play_button,mouse_x,mouse_y)

def check_play_button(sb,alien_setting,screen,ship,aliens,bullets,
        stats,play_button,mouse_x,mouse_y):
    play_butten_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    ''''''
    if play_butten_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(alien_setting,screen,ship,aliens)
        ship.center_ship()
        
        sb.prep_score()
        sb.prep_ships()
        
def update_screen(sb,alien_setting,screen,ship,bullets,aliens,stats,play_button):
    screen.fill(alien_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()#
    aliens.draw(screen)
    sb.show_score()
    
    if not stats.game_active:
        play_button.draw_button()
        
#    aliens.blitme()#Group 没有blitme()
    pygame.display.flip()#让最新绘制的屏幕可见

def update_bullet(sb,stats,bullets,aliens,alien_setting,ship,screen):
    #update_bullet
    bullets.update()#此处和bullet的update方法不能改为其他名称
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #测试bullets子弹数量
    #print(len(bullets)) 
    check_alien_bullet_collision(sb,stats,alien_setting, screen, ship,
        aliens,bullets)


def check_alien_bullet_collision(sb,stats,alien_setting, screen, ship, 
        aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for alien in collisions.values():
            stats.score += alien_setting.alien_points * len(alien)
            sb.prep_score()
        
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(alien_setting, screen, ship, aliens)    

def get_num_aliens_x(alien_setting,alien_width):
    available_space_x = alien_setting.screen_width - 2 * alien_width
    num_alien_x = int(available_space_x//(2 * alien_width))
    return num_alien_x
            
def get_number_rows(alien_setting, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (alien_setting.screen_height -
    (3 * alien_height) - ship_height)
    number_rows = int(available_space_y // (2 * alien_height))
    return number_rows
    
def create_alien(alien_setting, screen, aliens, alien_num, row_number):
    alien = Alien(alien_setting,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
def create_fleet(alien_setting, screen, ship, aliens):
    alien = Alien(alien_setting,screen)
    num_aliens_x = get_num_aliens_x(alien_setting,alien.rect.width)
    number_rows = get_number_rows(alien_setting, ship.rect.height,
        alien.rect.height)
    # for alien_num in range(5):#num_aliens_x = 1
        # create_alien(alien_setting, screen, aliens, alien_num,
            # row_number = 3)         
    # 创建外星人群

    for row_number in range(number_rows):
        for alien_num in range(num_aliens_x):
            create_alien(alien_setting, screen, aliens, alien_num,
            row_number)
                
def check_fleet_edges(alien_setting,aliens):
    '''检查外星人群是否碰撞边缘并进行相应操作'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(alien_setting,aliens)
            break
        
def change_fleet_direction(alien_setting,aliens):
    '''外星人群整体下落并改变移动方向'''
    for alien in aliens.sprites():
        alien.rect.y += alien_setting.fleet_drop_speed
    alien_setting.fleet_direction *= -1
        
def update_alien(sb,alien_setting,aliens,ship,stats,bullets,screen):
    ''''''
    check_fleet_edges(alien_setting,aliens)
    aliens.update()#
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(sb,alien_setting,aliens,ship,stats,bullets,screen)

def ship_hit(sb,alien_setting,aliens,ship,stats,bullets,screen):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(alien_setting, screen, ship, aliens)
        ship.center_ship()
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        
   
    




