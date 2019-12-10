class Settings():
    def __init__(self):
        #游戏界面大小及背景色
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #飞船速度因子
        self.speed_factor = 2.5
        #飞船数量限制：
        self.ship_limit = 3
        #子弹属性：
        self.bullet_spd = 3
        self.bullet_height = 20
        self.bullet_width = 2000
        self.bullet_color = (60,60,60)
        self.bullet_num = 8 #最大子弹数量
        #外星人属性：
        self.alien_speed_factor = 1#x轴移动速度
        self.fleet_drop_speed = 100#y轴下落速度
        self.fleet_direction = 1#1:表示向右移; -1:表示向左移;
     
        self.alien_points = 3
         
        
        
