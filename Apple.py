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
        

    def _GenApplePos(self):
        self.x=random.randint(0,SCREEN_WITH-APPLE_WIDTH+1)
        self.y=random.randint(0,SCREEN_HEIGHT-APPLE_HEIGHT+1)

    def SetApple(self):
        self._GenApplePos()

    def ShowApple(self):
        # self.pygame.draw.rect(self.screen,APPLE_COLOR,(self.x,self.y,APPLE_WIDTH,APPLE_HEIGHT))
        self.screen.blit(self.applePic,(self.x,self.y))

    # public method for getting the rectangle of apple
    def getRect(self):
        return (self.x, self.y, self.x + APPLE_WIDTH - 1, self.y + APPLE_HEIGHT - 1)

    def GetApplePos(self):
        return (self.x,self.y)
            
