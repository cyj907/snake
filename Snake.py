# -*- coding: cp936 -*-

#2016_6_22
#by zhs


SNAKE_WITH_HALH = 10
INIT_V = 5
INIT_DIRECT = 0
INIT_POS = (10,50,0)    #pos定义方式，2位置为方向，0表示水平，1表示竖直，0、1位置为首末坐标
SNAKE_COLOR=(0,255,100) #我喜欢荧光绿的蛇

class Snake:
    def __init__(self,pygame,screen):
        self.pygame = pygame
        self.screen = screen
        self.direction = INIT_DIRECT  #0-3 表示上下左右，初始化往上跑
        self.v = INIT_V             #初始化的速度
        self.pos=[INIT_POS]
        self.color = SNAKE_COLOR
        self.applePos = None

    #返回值False表示没吃到苹果
    def ForJade(self,pass_time,pos=None,d=None):
        if d!=None:
            self._SetDirection(d)
        if pos!=None:
            self._SetApplePos(pos)
        self._SankeGo(pass_time)
        if self.applePos!=None:
            return self._EatApple()
        else:
            return False

    def _SetDirection(self,d):
        self.direction = d

    def _SetApplePos(self,pos):
        self.applePos = pos

    def _SankeGo(self,pass_time):
        moveDist = pass_time*self.v

    def _EatApple(self):
        return False
        
