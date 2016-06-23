# -*- coding: cp936 -*-

#2016_6_22
#by zhs

from Const import *


INIT_V = 1
INIT_DIRECT = 3
INIT_POS = [10,50,200,50]    #pos���巽ʽ����ĩ���������
INIT_A = 0 #���ٶ�


class Snake:
    def __init__(self,pygame,screen):
        self.pygame = pygame
        self.screen = screen
        self.direction = INIT_DIRECT  #0-3 ��ʾ�������ң���ʼ��������
        self.dirChange = False
        self.v = INIT_V             #��ʼ�����ٶ�
        self.snakePoss=[INIT_POS[:]]
        self.applePos = None
        self.myRects = None
        self.additionRect = None
        self.eatApple = False
        self.addSnakeLength_Cache = 0
        self.dead = False

    def Reset(self):
        self.direction = INIT_DIRECT
        self.dirChange = False
        self.v = INIT_V
        self.snakePoss = [INIT_POS[:]]
        self.applePos = None
        self.myRects = None
        self.additionRect = None
        self.eatApple = False
        self.addSnakeLength_Cache = 0
        self.dead = False

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
        if (lastPos[1]==lastPos[3]) and (d==2 or d==3):  #�ߵ��·���;ɷ�����ˮƽ����
            if self._ToLeft(-1):   
                self.direction = 2
            else:
                self.direction = 3
            self.dirChange = False
        elif (lastPos[0]==lastPos[2]) and (d==0 or d==1):    #������ֱ����
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




    def __RectMod(self, id):
        # rect = self.snakePoss[id]
        # if self._ToUp(id):
        #     rect2 = [rect[2]-SNAKE_WITH_HALH, rect[3], rect[0]+SNAKE_WITH_HALH, rect[1]]
        # elif self._ToDown(id):
        #     rect2 = [rect[0]-SNAKE_WITH_HALH, rect[1], rect[2]+SNAKE_WITH_HALH, rect[3]]
        # elif self._ToLeft(id):
        #     rect2 = [rect[2], rect[3]-SNAKE_WITH_HALH, rect[0], rect[1]+SNAKE_WITH_HALH]
        # else:
        #     rect2 = [rect[0], rect[2]-SNAKE_WITH_HALH, rect[2], rect[3]+SNAKE_WITH_HALH]
        # return rect2
        return (self.myRects[id][0], self.myRects[id][1],
         self.myRects[id][0] + self.myRects[id][2] - 1,
         self.myRects[id][1] + self.myRects[id][3] - 1)


    #��������������꣬�ó�����ľ���
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
                self.myRects.append((pos[2]-SNAKE_WITH_HALH , pos[3] , 2*SNAKE_WITH_HALH+1, pos[1]-pos[3]+1))
            elif self._ToDown(i):
                self.myRects.append((pos[0]-SNAKE_WITH_HALH , pos[1] , 2*SNAKE_WITH_HALH+1 , pos[3]-pos[1]+1))
            else:
                print "error in _UpdateRects"
        self.additionRect = self.__RectMod(-1)

    def _DrawSnake(self):
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
                if self.snakePoss[0][0]-self.snakePoss[0][2]+1>decDist:
                    self.snakePoss[0][0]-=decDist
                    length = self.snakePoss[0][0]-self.snakePoss[0][2]+1
                    self.__DeleteTail(length)
                    return
                elif self.snakePoss[0][0]-self.snakePoss[0][2]+1==decDist:
                    self.snakePoss.pop(0)
                    return
                else:
                    decDist-=(self.snakePoss[0][0]-self.snakePoss[0][2]+1)
                    self.snakePoss.pop(0)
            elif self._ToRight(0):
                if self.snakePoss[0][2]-self.snakePoss[0][0]+1>decDist:
                    self.snakePoss[0][0]+=decDist
                    length = self.snakePoss[0][2]-self.snakePoss[0][0]+1
                    self.__DeleteTail(length)
                    return
                elif self.snakePoss[0][2]-self.snakePoss[0][0]+1==decDist:
                    self.snakePoss.pop(0)
                    return
                else:
                    decDist-=(self.snakePoss[0][2]-self.snakePoss[0][0]+1)
                    self.snakePoss.pop(0)
            elif self._ToUp(0):
                if self.snakePoss[0][1]-self.snakePoss[0][3]+1>decDist:
                    self.snakePoss[0][1]-=decDist
                    length = self.snakePoss[0][1]-self.snakePoss[0][3]+1
                    self.__DeleteTail(length)
                    return
                elif self.snakePoss[0][1]-self.snakePoss[0][3]+1==decDist:
                    self.snakePoss.pop(0)
                    return
                else:
                    decDist-=(self.snakePoss[0][1]-self.snakePoss[0][3]+1)
                    self.snakePoss.pop(0)
            elif self._ToDown(0):
                if self.snakePoss[0][3]-self.snakePoss[0][1]+1>decDist:
                    self.snakePoss[0][1]+=decDist
                    length = self.snakePoss[0][3]-self.snakePoss[0][1]+1
                    self.__DeleteTail(length)
                    return
                elif self.snakePoss[0][3]-self.snakePoss[0][1]+1==decDist:
                    self.snakePoss.pop(0)
                    return
                else:
                    decDist-=(self.snakePoss[0][3]-self.snakePoss[0][1]+1)
                    self.snakePoss.pop(0)
            else:
                print "error in _UpdateRects"

            

    def _SankeGo(self,pass_time):
        moveDist = int(pass_time*self.v/10.0)
        if self.dirChange:
            if self.direction==0:
                if self._ToLeft(-1):
                    self.snakePoss.append([self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH-1,
                                          self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH-moveDist])
                else :
                    self.snakePoss.append([self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH-1,
                                          self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH-moveDist])
            elif self.direction==1:
                if self._ToLeft(-1):
                    self.snakePoss.append([self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH+1,
                                          self.snakePoss[-1][2]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH+moveDist])
                else :
                    self.snakePoss.append([self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH+1,
                                          self.snakePoss[-1][2]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH+moveDist])
            elif self.direction==2:
                if self._ToUp(-1):
                    self.snakePoss.append([self.snakePoss[-1][2]-SNAKE_WITH_HALH-1,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]-SNAKE_WITH_HALH-moveDist,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH])
                else :
                    self.snakePoss.append([self.snakePoss[-1][2]-SNAKE_WITH_HALH-1,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]-SNAKE_WITH_HALH-moveDist,
                                          self.snakePoss[-1][3]-SNAKE_WITH_HALH])
            else:
                if self._ToUp(-1):
                    self.snakePoss.append([self.snakePoss[-1][2]+SNAKE_WITH_HALH+1,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH,
                                          self.snakePoss[-1][2]+SNAKE_WITH_HALH+moveDist,
                                          self.snakePoss[-1][3]+SNAKE_WITH_HALH])
                else :
                    self.snakePoss.append([self.snakePoss[-1][2]+SNAKE_WITH_HALH+1,
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
                            
            
        

    #����ֵFalse��ʾû�Ե�ƻ��
    def _EatApple(self):
        return RectIntersect(self.additionRect,
                             (self.applePos[0],self.applePos[1],self.applePos[0]+APPLE_WIDTH-1,self.applePos[1]+APPLE_HEIGHT-1))


    def _IsDead(self):
        headRect = self.snakePoss[-1]

        # hit wall
        if self._ToUp(-1) and headRect[3] < 0:
            return True
        elif self._ToDown(-1) and headRect[3] >= SCREEN_HEIGHT:
            return True
        elif self._ToLeft(-1) and headRect[2] < 0:
            return True
        elif self._ToRight(-1) and headRect[2] >= SCREEN_WITH:
            return True

        # hit tail

        for i in range(len(self.snakePoss) - 1):
            if RectIntersect(self.additionRect, self.__RectMod(i)):
                return True
        return False



    #���룺
        #pass_time����ʾ��������֮֡���ʱ����
        #pos����ʾƻ����λ�ã�Ĭ��ΪNone����δ����
        #d����ʾ�ߵ����˶�����
    #����һ��tuple(r1,r2),r1=true,��ʾײ���ˣ�r2=true��ʾ�Ե�ƻ����
    def ForJade(self,pass_time,pos=None,d=None):
        if self.dead:
            self._UpdateRects()
            self._DrawSnake()
            return (True,False)

        # print self.myRects
        # print '------------------------------------------------------'
        # for l in self.snakePoss:
        #     self.pygame.draw.line(self.screen,SNAKE_COLOR,(l[0],l[1]),(l[2],l[3]),1)
        if d!=None and (d==0 or d==1 or d==2 or d==3):
            self._SetDirection(d)
        if pos!=None:
            self._SetApplePos(pos)

        self._SankeGo(pass_time)
        self._UpdateRects()
        self._DrawSnake()
        self.eatApple = False
        if self.applePos!=None:
            self.eatApple = self._EatApple()
        self.v += self.eatApple * INIT_A

        if self._IsDead():
            self.dead = True
            self.v = 0
            return (True,self.eatApple)
        else:
            return (False,self.eatApple)

