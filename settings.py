class Settings():
    """存储外星人游戏的设置"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1024
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #飞船的设置
        self.ship_speed_factor = 3
        self.ship_limited = 1

        #子弹设置
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 100

        # 外星人设置
        self.alien_speed_factor = 0.1
        self.alien_drop_speed = 10
        self.fleet_direction = 1

        # 游戏加速度

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏而变化的参数"""
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 0.1
        self.alien_speed_factor = 0.5

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


