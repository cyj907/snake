# -*- coding: cp936 -*-

import pygame
from sys import exit
from pygame.locals import *
import time


APPLE_COLOR=(255,0,0) #姑且用红色的吧
SNAKE_COLOR=(0,255,100) #我喜欢荧光绿的蛇

SCREEN_WITH=500
SCREEN_HEIGHT=500

APPLE_WIDTH=20
APPLE_HEIGHT=20

SNAKE_WITH_HALH = 10

def RectIntersect(rect1,rect2):
    left = max(rect1[0],rect2[0])
    up = max(rect1[1],rect2[1])
    right = min(rect1[2],rect2[2])
    down = min(rect1[3],rect2[3])
    if left<right and up < down:
        return True
    else:
        return False