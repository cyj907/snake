# -*- coding: cp936 -*-

import pygame
from sys import exit
from pygame.locals import *
import time
import copy


APPLE_COLOR=(255,0,0) #�����ú�ɫ�İ�
SNAKE_COLOR=(0,255,100) #��ϲ��ӫ���̵���

SNAKE_WITH_HALH = 20
APPLE_WIDTH= 2*SNAKE_WITH_HALH+1
APPLE_HEIGHT= 2*SNAKE_WITH_HALH+1

Grid_X = 5
Grid_Y = 5
SCREEN_WITH=APPLE_WIDTH * Grid_X
SCREEN_HEIGHT=APPLE_HEIGHT * Grid_Y


def FindIntersectRect(rect1, rect2):
    left = max(rect1[0],rect2[0])
    up = max(rect1[1],rect2[1])
    right = min(rect1[2],rect2[2])
    down = min(rect1[3],rect2[3])
    return left, up, right, down

def RectIntersect(rect1,rect2):
    left, up, right, down = FindIntersectRect(rect1, rect2)
    if left<=right and up <= down:
        return True
    else:
        return False
