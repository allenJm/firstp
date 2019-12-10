class GameStats():
    def __init__(self,alien_setting):
        self.alien_setting = alien_setting
        self.reset_stats()
        self.game_active = False
        
    def reset_stats(self):
        self.ships_left = self.alien_setting.ship_limit
        self.score = 987654321
