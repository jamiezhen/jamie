import sys

import pygame

from pygame_test.setting import Settings
from pygame_test.ship import Ship

import pygame_test.game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('外星人入侵')

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:

        # 监听键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship)



run_game()