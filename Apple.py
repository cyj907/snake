# -*- coding: cp936 -*-

#2016_6_22
#by zhs

from Const import *
import random

SNAKE_COLOR=(255,0,0) #姑且用红色的吧
APPLE_RADIUS=10


class Apple:
        
    def __init__(self,pygame,screen):
        self.pygame = pygame
        self.screen = screen
        self.x=random.randint(APPLE_RADIUS,SCREEN_WITH-APPLE_RADIUS)
        self.y=random.randint(APPLE_RADIUS,SCREEN_HEIGHT-APPLE_RADIUS)
        

    def _GetApplePos(self):
        self.x=random.randint(APPLE_RADIUS,SCREEN_WITH-APPLE_RADIUS)
        self.Y=random.randint(APPLE_RADIUS,SCREEN_HEIGHT-APPLE_RADIUS)


    def SetApple(self,eaten=False):
        if eaten:
            self._GetApplePos()
        self.pygame.draw.circle(self.screen,SNAKE_COLOR,(self.x,self.y),APPLE_RADIUS)
            
