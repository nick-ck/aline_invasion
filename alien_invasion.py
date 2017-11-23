import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化一个游戏窗口
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Aline Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    #alien = Alien(ai_settings, screen)
    # 创建用于统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一个用于存储子弹的编组、外星人编组
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings,screen,ship,aliens)

    play_button = Button(ai_settings,screen,"Play")
    scoreboard = Scoreboard(ai_settings,screen,stats)

    # 开始程序的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets,stats,scoreboard)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings, screen,stats, ship,aliens,bullets,play_button,scoreboard)

run_game()