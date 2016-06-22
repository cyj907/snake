# -*- coding: cp936 -*-

#2016_6_22
#by zhs

from Const import *


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



    def _ToLeft(self,index):
        return self.snakePoss[index][0]>self.snakePoss[index][2]
    def _ToRight(self,index):
        return self.snakePoss[index][0]<self.snakePoss[index][2]
    def _ToUp(self,index):
        return self.snakePoss[index][1]>self.snakePoss[index][3]
    def _ToDown(self,index):
        return self.snakePoss[index][1]<self.snakePoss[index][3]




        

    def _SetDirection(self,d):
        lastPos = self.snakePoss[-1]
        if (lastPos[1]==lastPos[3]) and (d==2||d==3):  #蛇的新方向和旧方向都在水平方向
            if self._ToLeft(-1):   
                self.direction = 2
            else:
                self.direction = 3
            self.dirChange = False
        elif (lastPos[0]==lastPos[2]) and (d==0||d==1):    #都是竖直方向
            if self._ToUp(-1):   
                self.direction = 0
            else:
                self.direction = 1
            self.dirChange = False
        else:
            self.direction = d
            self.dirChange = True

    def _SetApplePos(self,pos):
        self.applePos = pos





    #根据蛇身体的坐标，得出身体的矩形
    def _UpdateRects(self):
        self.myRects=[]
        for i,pos in enumerate(self.snakePoss):
            if self._ToLeft(i):
                self.myRects.append((pos[2],pos[3]-SNAKE_WITH_HALH,pos[0],pos[1]+SNAKE_WITH_HALH))
            elif self._ToRight(i):
                self.myRects.append((pos[0],pos[1]-SNAKE_WITH_HALH,pos[2],pos[3]+SNAKE_WITH_HALH))
            elif self._ToUp(i):
                self.myRects.append((pos[2]-SNAKE_WITH_HALH,pos[3],pos[0]+SNAKE_WITH_HALH,pos[1]))
            elif self._ToDown(i):
                self.myRects.append((pos[0]-SNAKE_WITH_HALH,pos[1],pos[2]+SNAKE_WITH_HALH,pos[3]))
            else:
                print "error in _UpdateRects"

    def _DrawSnake(self):
        self._UpdateRects()
        for rect in self.myRects:
            self.pygame.draw.rect(self.screen,SNAKE_COLOR,rect)
            

    def _Decrese(self,decDist):
        while 1:
            for direct0,direct1,diff0,diff1 in [(0,2,1,3),(1,3,0,2)]:
                if self.snakePoss[0][direct0]==self.snakePoss[0][direct1]:
                    if self.snakePoss[0][diff0]>self.snakePoss[0][diff1]:
                        if self.snakePoss[0][diff0]-self.snakePoss[0][diff1]>=moveDist:
                            self.snakePoss[0][diff0]-=moveDist
                            return
                        elif self.snakePoss[0][diff0]-self.snakePoss[0][diff1]==moveDist:
                            self.snakePoss.pop(0)
                            return
                        else:
                            moveDist-=(self.snakePoss[0][diff0]-self.snakePoss[0][diff1])
                            self.snakePoss.pop(0)
                    else:
                        if self.snakePoss[0][diff1]-self.snakePoss[0][diff0]>=moveDist:
                            self.snakePoss[0][diff0]+=moveDist
                            return
                        elif self.snakePoss[0][diff1]-self.snakePoss[0][diff0]==moveDist:
                            self.snakePoss.pop(0)
                            return
                        else:
                            moveDist-=(self.snakePoss[0][diff1]-self.snakePoss[0][diff0])
                            self.snakePoss.pop(0)
            
                            
    #返回值True表示撞死了
    def _SankeGo(self,pass_time):
        moveDist = pass_time*self.v
        if self.dirChange:
            if self.direction==0:
                if self._ToLeft(-1):
                    self.snakePoss.append(self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH-moveDist)
                else :
                    self.snakePoss.append(self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH-moveDist)
            elif self.direction==1:
                if self._ToLeft(-1):
                    self.snakePoss.append(self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH+moveDist)
                else :
                    self.snakePoss.append(self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH+moveDist)
            elif self.direction==2:
                if self._ToUp(-1):
                    self.snakePoss.append(self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]-SNAKE_WITH_HALH-moveDist,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH)
                else :
                    self.snakePoss.append(self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]-SNAKE_WITH_HALH-moveDist,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH)
            else:
                if self._ToUp(-1):
                    self.snakePoss.append(self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]+SNAKE_WITH_HALH+moveDist,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH)
                else :
                    self.snakePoss.append(self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]+SNAKE_WITH_HALH+moveDist,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH)
        else:
            if self.direction==0:
                self.snakePoss[-1][3]-=moveDist
            elif self.direction==1:
                self.snakePoss[-1][3]+=moveDist
            elif self.direction==2:
                self.snakePoss[-1][2]-=moveDist
            else:
                self.snakePoss[-1][2]+=moveDist

        self._Decrese(moveDist)
                            
            
        

    #返回值False表示没吃到苹果
    def _EatApple(self):
        return False
        

    #输入：
        #pass_time：表示相邻相邻帧之间的时间间隔
        #pos：表示苹果的位置，默认为None，即未更新
        #d：表示蛇的新运动方向
    #返回一个tuple(r1,r2),r1=true,表示撞死了，r2=true表示吃到苹果了
    def ForJade(self,pass_time,pos=None,d=None):
        self._DrawSnake()
        
        if d!=None and (d==0 or d==1 or d==2 or d==3):
            self._SetDirection(d)
        if pos!=None:
            self._SetApplePos(pos)
        
        if self.applePos!=None:
            return (self._SankeGo(pass_time),self._EatApple())
        else:
            return (self._SankeGo(pass_time),False)
