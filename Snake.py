# -*- coding: cp936 -*-

#2016_6_22
#by zhs


SNAKE_WITH_HALH = 10
INIT_V = 5
INIT_DIRECT = 0
INIT_POS = (10,50,0)    #pos���巽ʽ��2λ��Ϊ����0��ʾˮƽ��1��ʾ��ֱ��0��1λ��Ϊ��ĩ����
SNAKE_COLOR=(0,255,100) #��ϲ��ӫ���̵���

class Snake:
    def __init__(self,pygame,screen):
        self.pygame = pygame
        self.screen = screen
        self.direction = INIT_DIRECT  #0-3 ��ʾ�������ң���ʼ��������
        self.v = INIT_V             #��ʼ�����ٶ�
        self.pos=[INIT_POS]
        self.color = SNAKE_COLOR
        self.applePos = None

    #����ֵFalse��ʾû�Ե�ƻ��
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
        
