# 导入pygame模块
import pygame
# 导入游戏主要函数模块
import game_funtions as gf
# 导入pygame的编组
from pygame.sprite import Group
# 导入设置模块
from settings import Settings
# 导入游戏统计模块
from game_stats import GameStats
# 导入飞船模块
from ship import Ship
# 导入外星人模块
from alien import Alien
# 导入按钮模块
from button import Button
# 导入记分牌模块
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 创建一个设置实例
    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建Play按钮
    play_button = Button(ai_settings,screen,"Play")

    #创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    
    #创建一艘飞船
    ship = Ship(ai_settings,screen)

    #创建一个用于存储子弹的编组
    bullets = Group()

    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)


    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,
                        sb,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,
                              ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
            
        #更新屏幕
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
                         play_button)

run_game()
