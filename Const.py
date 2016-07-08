# -*- coding: cp936 -*-

import pygame
from sys import exit
from pygame.locals import *
import time
import copy


APPLE_COLOR=(255,0,0) #�����ú�ɫ�İ�
SNAKE_COLOR=(0,255,100) #��ϲ��ӫ���̵���

SCREEN_WITH=300
SCREEN_HEIGHT=300

APPLE_WIDTH=10
APPLE_HEIGHT=10

SNAKE_WITH_HALH = 5

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
