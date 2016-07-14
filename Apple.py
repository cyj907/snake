# -*- coding: cp936 -*-

#2016_6_27
#by cyj

from Const import *
import random

class Apple:

    def __init__(self):
        #self.x=random.randint(0,SCREEN_WITH-APPLE_WIDTH+1)
        #self.y=random.randint(0,SCREEN_HEIGHT-APPLE_HEIGHT+1)
        self.x = random.randint(0, Grid_X-1) * APPLE_WIDTH
        self.y = random.randint(0, Grid_Y-1) * APPLE_WIDTH
        #print self.x / APPLE_WIDTH, self.y / APPLE_WIDTH

    def _GenApplePos(self):
        #self.x=random.randint(0,SCREEN_WITH-APPLE_WIDTH+1)
        #self.y=random.randint(0,SCREEN_HEIGHT-APPLE_HEIGHT+1)
        self.x = random.randint(0, Grid_X-1) * APPLE_WIDTH
        self.y = random.randint(0, Grid_Y-1) * APPLE_WIDTH
        #print self.x / APPLE_WIDTH, self.y / APPLE_WIDTH

    def SetApple(self):
        self._GenApplePos()

    # public method for getting the rectangle of apple
    def getRect(self):
        return self.x, self.y, self.x + APPLE_WIDTH - 1, self.y + APPLE_HEIGHT - 1

    def GetApplePos(self):
        return self.x, self.y

