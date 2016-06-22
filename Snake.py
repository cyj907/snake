# -*- coding: cp936 -*-

#2016_6_22
#by zhs


SNAKE_WITH_HALH = 10
INIT_V = 5
INIT_DIRECT = 0
INIT_POS = (10,50,50,50)    #pos定义方式，首末两点的坐标
SNAKE_COLOR=(0,255,100) #我喜欢荧光绿的蛇

class Snake:
    def __init__(self,pygame,screen):
        self.pygame = pygame
        self.screen = screen
        self.direction = INIT_DIRECT  #0-3 表示上下左右，初始化往上跑
        self.dirChange = False
        self.v = INIT_V             #初始化的速度
        self.snakePoss=[INIT_POS]
        self.color = SNAKE_COLOR
        self.applePos = None
        self.myRects = None

    #输入：
        #pass_time：表示相邻相邻帧之间的时间间隔
        #pos：表示苹果的位置，默认为None，即未更新
        #d：表示蛇的新运动方向
    #返回一个tuple(r1,r2),r1=true,表示撞死了，r2=true表示吃到苹果了
    def ForJade(self,pass_time,pos=None,d=None):
        if d!=None:
            self._SetDirection(d)
        if pos!=None:
            self._SetApplePos(pos)
        
        if self.applePos!=None:
            return (self._SankeGo(pass_time),self._EatApple())
        else:
            return (self._SankeGo(pass_time),False)

    def _SetDirection(self,d):
        lastPos = self.snakePoss[-1]
        if (lastPos[1]==lastPos[3])&&(d==2||d==3):  #蛇的新方向和旧方向都在水平方向
            if lastPos[0]>lastPos[2]:   
                self.direction = 2
            else:
                self.direction = 3
            self.dirChange = False
        elif (lastPos[0]==lastPos[2])&&(d==0||d==1):    #都是竖直方向
            if lastPos[1]>lastPos[3]:   
                self.direction = 0
            else:
                self.direction = 1
            self.dirChange = False
        else:
            self.direction = d
            self.dirChange = True

    def _SetApplePos(self,pos):
        self.applePos = pos

    #返回值True表示撞死了
    def _SankeGo(self,pass_time):
        moveDist = pass_time*self.v
        if self.dirChange:
            s
        else:
            
        

    #返回值False表示没吃到苹果
    def _EatApple(self):
        return False
        
