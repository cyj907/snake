
from Const import *

class Menu:
    def __init__(self,pygame,screen,screenW,screenH,picList,modeList):
        self.pygame = pygame
        self.screen = screen
        self.sw = screenW
        self.sh = screenH
        self.picList = picList
        self.modeList = modeList

        self.menuLen = len(picList)
        
        self.wList = []
        self.hList = []
        self.rectList = []
        for i,pic in enumerate(picList):
            self.wList.append(pygame.Surface.get_width(pic))
            self.hList.append(pygame.Surface.get_height(pic))
            self.rectList.append(Rect((self.sw-self.wList[i])/2,self.sh*(i+1)/(self.menuLen+1)-self.hList[i]/2,self.wList[i],self.hList[i]))


    def ShowMenu(self):
        for i,pic in enumerate(self.picList):
            self.screen.blit(pic,self.rectList[i][0:2])

    def MouseDown(self,pos=None):
        if pos==None:
            return None
        for i,rect in enumerate(self.rectList):
            if rect.collidepoint(pos):
                return self.modeList[i]
        return None
