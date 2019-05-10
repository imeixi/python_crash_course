#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame


class Ship():
    """初始化飞船并设置其初始位置"""

    def __init__(self, ai_settings, screen):
        # 初始化飞船并设置其初始化位置
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船方在屏幕底部重要
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 移动标志
        self.move_right = False
        self.move_left = False
        # 在飞船的属性center中存储小数值
        # self.center = float(self.rect.centerx)

    def update(self):
        if self.move_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.move_left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
