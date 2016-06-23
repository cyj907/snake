# -*- coding: cp936 -*-

#2016_6_22
#by zhs

from Const import *
import random



class Apple:
        
    def __init__(self,pygame,screen):
        self.pygame = pygame
        self.screen = screen
        self.x=None
        self.y=None
        

    def _GetApplePos(self):
        self.x=random.randint(0,SCREEN_WITH-APPLE_WIDTH+1)
        self.y=random.randint(0,SCREEN_HEIGHT-APPLE_HEIGHT+1)


    def SetApple(self,eaten=False):
        if eaten:
            self._GetApplePos()
        self.pygame.draw.rect(self.screen,APPLE_COLOR,(self.x,self.y,APPLE_WIDTH,APPLE_HEIGHT))
        return (self.x,self.y)
            
