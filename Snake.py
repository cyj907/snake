# -*- coding: cp936 -*-

#2016_6_22
#by zhs

from Const import *


INIT_V = 1
INIT_DIRECT = 3
INIT_POS = [10,50,200,50]    #pos定义方式，首末两点的坐标
INIT_A = 0.4 #加速度
    

class Snake:
    def __init__(self,pygame,screen):
        self.pygame = pygame
        self.screen = screen
        self.direction = INIT_DIRECT  #0-3 表示上下左右，初始化往上跑
        self.dirChange = False
        self.v = INIT_V             #初始化的速度
        self.snakePoss=[INIT_POS]
        self.applePos = None
        self.myRects = None
        self.additionRect = None
        self.eatApple = False
        self.addSnakeLength_Cache = 0



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
        if (lastPos[1]==lastPos[3]) and (d==2 or d==3):  #蛇的新方向和旧方向都在水平方向
            if self._ToLeft(-1):   
                self.direction = 2
            else:
                self.direction = 3
            self.dirChange = False
        elif (lastPos[0]==lastPos[2]) and (d==0 or d==1):    #都是竖直方向
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
##            if self._ToLeft(i):
##                self.myRects.append(Rect(pos[2],pos[3]-SNAKE_WITH_HALH,pos[0],pos[1]+SNAKE_WITH_HALH))
##            elif self._ToRight(i):
##                self.myRects.append(Rect(pos[0],pos[1]-SNAKE_WITH_HALH,pos[2],pos[3]+SNAKE_WITH_HALH))
##            elif self._ToUp(i):
##                self.myRects.append(Rect(pos[2]-SNAKE_WITH_HALH,pos[3],pos[0]+SNAKE_WITH_HALH,pos[1]))
##            elif self._ToDown(i):
##                self.myRects.append(Rect(pos[0]-SNAKE_WITH_HALH,pos[1],pos[2]+SNAKE_WITH_HALH,pos[3]))
##            else:
##                print "error in _UpdateRects"
            if self._ToLeft(i):
                self.myRects.append((pos[2] , pos[3]-SNAKE_WITH_HALH , pos[0]-pos[2]+1 , 2*SNAKE_WITH_HALH+1))
            elif self._ToRight(i):
                self.myRects.append((pos[0] , pos[1]-SNAKE_WITH_HALH , pos[2]-pos[0]+1 , 2*SNAKE_WITH_HALH+1))
            elif self._ToUp(i):
                self.myRects.append((pos[2]-SNAKE_WITH_HALH , pos[3] , 2*SNAKE_WITH_HALH+1 , pos[1]-pos[3]+1))
            elif self._ToDown(i):
                self.myRects.append((pos[0]-SNAKE_WITH_HALH , pos[1] , 2*SNAKE_WITH_HALH+1 , pos[3]-pos[1]+1))
            else:
                print "error in _UpdateRects"
        self.additionRect = [self.myRects[-1][0], self.myRects[-1][1],
                             self.myRects[-1][0]+self.myRects[-1][2]-1,
                             self.myRects[-1][1]+self.myRects[-1][3]-1]

    def _DrawSnake(self):
        self._UpdateRects()
        for rect in self.myRects:
            self.pygame.draw.rect(self.screen,SNAKE_COLOR,rect)


    def __DeleteTail(self,length):
        if length<2*SNAKE_WITH_HALH+1:
            self.snakePoss.pop(0)
        else:
            return
        if self._ToLeft(0):
            self.snakePoss[0][0]+=length
        elif self._ToRight(0):
            self.snakePoss[0][0]-=length
        elif self._ToUp(0):
            self.snakePoss[0][1]+=length
        elif self._ToDown(0):
            self.snakePoss[0][1]-=length
        else:
            print "error in _UpdateRects"

    def _Decrese(self,decDist):
        while 1:
            if self._ToLeft(0):
                if self.snakePoss[0][0]-self.snakePoss[0][2]>decDist:
                    self.snakePoss[0][0]-=decDist
                    length = self.snakePoss[0][0]-self.snakePoss[0][2]
                    self.__DeleteTail(length)
                    return
                elif self.snakePoss[0][0]-self.snakePoss[0][2]==decDist:
                    self.snakePoss.pop(0)
                    return
                else:
                    decDist-=(self.snakePoss[0][0]-self.snakePoss[0][2])
                    self.snakePoss.pop(0)
            elif self._ToRight(0):
                if self.snakePoss[0][2]-self.snakePoss[0][0]>decDist:
                    self.snakePoss[0][0]+=decDist
                    length = self.snakePoss[0][2]-self.snakePoss[0][0]
                    self.__DeleteTail(length)
                    return
                elif self.snakePoss[0][2]-self.snakePoss[0][0]==decDist:
                    self.snakePoss.pop(0)
                    return
                else:
                    decDist-=(self.snakePoss[0][2]-self.snakePoss[0][0])
                    self.snakePoss.pop(0)
            elif self._ToUp(0):
                if self.snakePoss[0][1]-self.snakePoss[0][3]>decDist:
                    self.snakePoss[0][1]-=decDist
                    length = self.snakePoss[0][1]-self.snakePoss[0][3]
                    self.__DeleteTail(length)
                    return
                elif self.snakePoss[0][1]-self.snakePoss[0][3]==decDist:
                    self.snakePoss.pop(0)
                    return
                else:
                    decDist-=(self.snakePoss[0][1]-self.snakePoss[0][3])
                    self.snakePoss.pop(0)
            elif self._ToDown(0):
                if self.snakePoss[0][3]-self.snakePoss[0][1]>decDist:
                    self.snakePoss[0][1]+=decDist
                    length = self.snakePoss[0][3]-self.snakePoss[0][1]
                    self.__DeleteTail(length)
                    return
                elif self.snakePoss[0][3]-self.snakePoss[0][1]==decDist:
                    self.snakePoss.pop(0)
                    return
                else:
                    decDist-=(self.snakePoss[0][3]-self.snakePoss[0][1])
                    self.snakePoss.pop(0)
            else:
                print "error in _UpdateRects"

            
                            
    #返回值True表示撞死了
    def _SankeGo(self,pass_time):
        moveDist = pass_time*self.v/10.0
        if self.dirChange:
            if self.direction==0:
                if self._ToLeft(-1):
                    self.snakePoss.append([self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH-moveDist])
                else :
                    self.snakePoss.append([self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH-moveDist])
            elif self.direction==1:
                if self._ToLeft(-1):
                    self.snakePoss.append([self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH+moveDist])
                else :
                    self.snakePoss.append([self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH+moveDist])
            elif self.direction==2:
                if self._ToUp(-1):
                    self.snakePoss.append([self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]-SNAKE_WITH_HALH-moveDist,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH])
                else :
                    self.snakePoss.append([self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]-SNAKE_WITH_HALH-moveDist,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH])
            else:
                if self._ToUp(-1):
                    self.snakePoss.append([self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]+SNAKE_WITH_HALH+moveDist,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH])
                else :
                    self.snakePoss.append([self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]+SNAKE_WITH_HALH+moveDist,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH])
        else:
            if self.direction==0:
                self.snakePoss[-1][3]-=moveDist
            elif self.direction==1:
                self.snakePoss[-1][3]+=moveDist
            elif self.direction==2:
                self.snakePoss[-1][2]-=moveDist
            else:
                self.snakePoss[-1][2]+=moveDist

        moveDist-=self.addSnakeLength_Cache
        self.addSnakeLength_Cache=0
        if self.eatApple:
            moveDist-=APPLE_WIDTH
        if moveDist>0:
            self._Decrese(moveDist)
        else:
            self.addSnakeLength_Cache = -moveDist
                            
            
        

    #返回值False表示没吃到苹果
    def _EatApple(self):
        return RectIntersect(self.additionRect,
                             (self.applePos[0],self.applePos[1],self.applePos[0]+APPLE_WIDTH-1,self.applePos[1]+APPLE_HEIGHT-1))
        

    #输入：
        #pass_time：表示相邻相邻帧之间的时间间隔
        #pos：表示苹果的位置，默认为None，即未更新
        #d：表示蛇的新运动方向
    #返回一个tuple(r1,r2),r1=true,表示撞死了，r2=true表示吃到苹果了
    def ForJade(self,pass_time,pos=None,d=None):
        self._DrawSnake()
        # self.pygame.draw.rect(self.screen, SNAKE_COLOR, (100,100,2,2))
        # for l in self.snakePoss:
        #     self.pygame.draw.line(self.screen,SNAKE_COLOR,(l[0],l[1]),(l[2],l[3]),1)
        if d!=None and (d==0 or d==1 or d==2 or d==3):
            self._SetDirection(d)
        if pos!=None:
            self._SetApplePos(pos)


        self.eatApple = False
        if self.applePos!=None:
            self.eatApple = self._EatApple()
        self.v += self.eatApple * INIT_A
        return (self._SankeGo(pass_time),self.eatApple)
