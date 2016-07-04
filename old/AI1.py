from Const import *


class AI1:
    def __init__(self,snake,apple):
        self.snake = snake
        self.apple = apple
        self.apple_pos=None
        self.snake_pos=None

    def __AppleIsUp(self):
        return self.apple_pos[1]+APPLE_HEIGHT-1<self.snake_pos[1]

    def __AppleIsUpWithHalf(self):
        return self.apple_pos[1]+APPLE_HEIGHT-1<self.snake_pos[1]-SNAKE_WITH_HALH

    def __AppleIsDown(self):
        return self.apple_pos[1]>self.snake_pos[1]

    def __AppleIsDownWithHalf(self):
        return self.apple_pos[1]>self.snake_pos[1]+SNAKE_WITH_HALH

    def __AppleIsLeft(self):
        return self.apple_pos[0]+APPLE_WIDTH-1<self.snake_pos[0]

    def __AppleIsLeftWithHalf(self):
        return self.apple_pos[0]+APPLE_WIDTH-1<self.snake_pos[0]-SNAKE_WITH_HALH

    def __AppleIsRight(self):
        return self.apple_pos[0]>self.snake_pos[0]

    def __AppleIsRightWithHalf(self):
        return self.apple_pos[0]>self.snake_pos[0]+SNAKE_WITH_HALH


    def _Simple(self,time_passed):
        self.apple_pos=self.apple.GetApplePos()
        self.snake_pos = (self.snake.snakePoss[-1][2],self.snake.snakePoss[-1][3])
        directions = []
        headDir = self.snake.GetNowDirection()
        if headDir==0 or headDir==1:
            # if headDir==0:
            #     if not self.__AppleIsDonw():
            #         directions.append(0)
            # else:
            #     if not self.__AppleIsUp():
            #         directions.append(1)
            if headDir==0:
                if  self.__AppleIsUp():
                    directions.append(0)
            else:
                if  self.__AppleIsDown():
                    directions.append(1)
            if self.__AppleIsLeftWithHalf():
                directions.append(2)
            elif self.__AppleIsRightWithHalf():
                directions.append(3)
            directions.append(headDir)

            """
            if not directions:  #apple is down or up
                directions.append(2)
                directions.append(3)
            """
        else:
        #     if headDir==2:
        #         if not self.__AppleIsRight():
        #             directions.append(2)
        #     else:
        #         if not self.__AppleIsLeft():
        #             directions.append(3)
            if headDir==2:
                if  self.__AppleIsLeft():
                    directions.append(2)
            else:
                if  self.__AppleIsRight():
                    directions.append(3)
            if self.__AppleIsUpWithHalf():
                directions.append(0)
            elif self.__AppleIsDownWithHalf():
                directions.append(1)
            directions.append(headDir)

            """
            if not directions:
                directions.append(0)
                directions.append(1)
            """
        for d in directions:
            dead = self.snake.ForTestNewStateWillDead(time_passed,self.apple_pos,d)
            if dead:
                print '------------------------------------'
                print "headDir=", headDir
                print "direction=", d
                print "apple=", self.apple_pos
                print "snake=", self.snake_pos
            #print "#1 for: ", (d, dead)
            if not dead:
                return d
        for d in set([0,1,2,3])-set(directions):
            dead = self.snake.ForTestNewStateWillDead(time_passed,self.apple_pos,d)
            if dead:
                print '------------------------------------'
                print "headDir=", headDir
                print "direction=", d
                print "apple=", self.apple_pos
                print "snake=", self.snake_pos
            #print "#2 for: ", (d, dead)
            if not dead:
                return d
        return None


    def GetDirection(self,time_passed):
        return self._Simple(time_passed)