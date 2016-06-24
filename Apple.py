# -*- coding: cp936 -*-

#2016_6_22
#by zhs

from Const import *
import random



class Apple:
        
    def __init__(self,pygame,screen,applePic):
        self.pygame = pygame
        self.screen = screen
        self.x=random.randint(0,SCREEN_WITH-APPLE_WIDTH+1)
        self.y=random.randint(0,SCREEN_HEIGHT-APPLE_HEIGHT+1)
        self.applePic=applePic
        

    def _GetApplePos(self):
        self.x=random.randint(0,SCREEN_WITH-APPLE_WIDTH+1)
        self.y=random.randint(0,SCREEN_HEIGHT-APPLE_HEIGHT+1)


    def SetApple(self,eaten=False):
        if eaten:
            self._GetApplePos()
        # self.pygame.draw.rect(self.screen,APPLE_COLOR,(self.x,self.y,APPLE_WIDTH,APPLE_HEIGHT))
        self.screen.blit(self.applePic,(self.x,self.y))
        return (self.x,self.y)

    def GetApplePos(self):
        return (self.x,self.y)
            
