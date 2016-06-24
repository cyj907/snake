from Const import *


class AI1:
    def __init__(self,snake,apple):
        self.snake = snake
        self.apple = apple
        self.apple_pos=None
        self.snake_pos=None

    def __AppleIsUp(self):
        return self.apple_pos[1]+APPLE_HEIGHT<self.snake_pos[1]

    def __AppleIsUpWithHalf(self):
        return self.apple_pos[1]+APPLE_HEIGHT<self.snake_pos[1]-SNAKE_WITH_HALH

    def __AppleIsDonw(self):
        return self.apple_pos[1]>self.snake_pos[1]

    def __AppleIsDonwWithHalf(self):
        return self.apple_pos[1]>self.snake_pos[1]+SNAKE_WITH_HALH

    def __AppleIsLeft(self):
        return self.apple_pos[0]+APPLE_WIDTH<self.snake_pos[0]

    def __AppleIsLeftWithHalf(self):
        return self.apple_pos[0]+APPLE_WIDTH<self.snake_pos[0]+SNAKE_WITH_HALH

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
            if headDir==0:
                if self.__AppleIsUp():
                    directions.append(0)
            else:
                if self.__AppleIsDonw():
                    directions.append(1)

            if self.__AppleIsLeftWithHalf():
                directions.append(2)
            elif self.__AppleIsRightWithHalf():
                directions.append(3)
            if not directions:  #apple is down or up
                directions.append(2)
                directions.append(3)
        else:
            if headDir==2:
                if self.__AppleIsLeft():
                    directions.append(2)
            else:
                if self.__AppleIsRight():
                    directions.append(3)

            if self.__AppleIsUpWithHalf():
                directions.append(0)
            elif self.__AppleIsDonwWithHalf():
                directions.append(1)
            if not directions:
                directions.append(0)
                directions.append(1)
        print '------------------------------------'
        print directions
        for d in directions:
            print (d,self.snake.ForTestNewStateWillDead(time_passed,self.apple_pos,d))
            if not self.snake.ForTestNewStateWillDead(time_passed,self.apple_pos,d):
                return d
        for d in set([0,1,2,3])-set(directions):
            print (d,self.snake.ForTestNewStateWillDead(time_passed,self.apple_pos,d))
            if not self.snake.ForTestNewStateWillDead(time_passed,self.apple_pos,d):
                return d
        return None


    def GetDirection(self,time_passed):
        return self._Simple(time_passed)