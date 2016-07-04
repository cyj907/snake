# -*- coding: cp936 -*-

#2016_6_27
#by cyj

from Const import *
import random

class Apple:

    def __init__(self):
        self.x=random.randint(0,SCREEN_WITH-APPLE_WIDTH+1)
        self.y=random.randint(0,SCREEN_HEIGHT-APPLE_HEIGHT+1)

    def _GenApplePos(self):
        self.x=random.randint(0,SCREEN_WITH-APPLE_WIDTH+1)
        self.y=random.randint(0,SCREEN_HEIGHT-APPLE_HEIGHT+1)

    def SetApple(self):
        self._GenApplePos()

    # public method for getting the rectangle of apple
    def getRect(self):
        return self.x, self.y, self.x + APPLE_WIDTH - 1, self.y + APPLE_HEIGHT - 1

    def GetApplePos(self):
        return self.x, self.y

