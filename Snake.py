# -*- coding: cp936 -*-

#2016_6_22
#by zhs


SNAKE_WITH_HALH = 10
INIT_V = 5
INIT_DIRECT = 0
INIT_POS = (10,50,50,50)    #pos���巽ʽ����ĩ���������
SNAKE_COLOR=(0,255,100) #��ϲ��ӫ���̵���

class Snake:
    def __init__(self,pygame,screen):
        self.pygame = pygame
        self.screen = screen
        self.direction = INIT_DIRECT  #0-3 ��ʾ�������ң���ʼ��������
        self.dirChange = False
        self.v = INIT_V             #��ʼ�����ٶ�
        self.snakePoss=[INIT_POS]
        self.color = SNAKE_COLOR
        self.applePos = None
        self.myRects = None

    #���룺
        #pass_time����ʾ��������֮֡���ʱ����
        #pos����ʾƻ����λ�ã�Ĭ��ΪNone����δ����
        #d����ʾ�ߵ����˶�����
    #����һ��tuple(r1,r2),r1=true,��ʾײ���ˣ�r2=true��ʾ�Ե�ƻ����
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
        if (lastPos[1]==lastPos[3])&&(d==2||d==3):  #�ߵ��·���;ɷ�����ˮƽ����
            if lastPos[0]>lastPos[2]:   
                self.direction = 2
            else:
                self.direction = 3
            self.dirChange = False
        elif (lastPos[0]==lastPos[2])&&(d==0||d==1):    #������ֱ����
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

    #����ֵTrue��ʾײ����
    def _SankeGo(self,pass_time):
        moveDist = pass_time*self.v
        if self.dirChange:
            s
        else:
            
        

    #����ֵFalse��ʾû�Ե�ƻ��
    def _EatApple(self):
        return False
        
