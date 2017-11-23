class GameStats():
    """跟踪游戏统计信息"""

    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        # 让游戏一开始出于非活动状态
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limited
        self.score = 0
        self.level = 1
