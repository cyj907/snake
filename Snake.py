# -*- coding: cp936 -*-

#2016_6_22
#by cyj

from Const import *
from Direction import Direction, ReverseDir
from random import randint


class Snake:
    def __init__(self):
        self.curDir = Direction.East
        self.bodyHalfWidth = SNAKE_WITH_HALH
        self.initLen = 3
        x = randint(0, Grid_X-1-self.initLen)
        y = randint(0, Grid_Y-1)
        self.body = [(x*APPLE_WIDTH, y*APPLE_HEIGHT+self.bodyHalfWidth, APPLE_WIDTH*(self.initLen+x)-1, y*APPLE_HEIGHT+self.bodyHalfWidth)]     # line from west to east, from north to south
        self.rects = [(0, 0, APPLE_WIDTH*6-1, APPLE_WIDTH-1)]
        self.orientation = [Direction.East]

    def _MoveBody(self, d, dec_len, inc_len):
        # move tail
        x1, y1, x2, y2 = self.body[0]
        orient = self.orientation[0]

        if orient == Direction.North:
            self.body[0] = (x1,y1,x2,y2-dec_len)
        elif orient == Direction.South:
            self.body[0] = (x1,y1+dec_len,x2,y2)
        elif orient == Direction.West:
            self.body[0] = (x1,y1,x2-dec_len,y2)
        else:
            self.body[0] = (x1+dec_len,y1,x2,y2)

        x1, y1, x2, y2 = self.body[0]
        if y1 >= y2-2*self.bodyHalfWidth and (orient == Direction.South or orient == Direction.North):
            body1 = self.body.pop(0)
            orient1 = self.orientation.pop(0)
            i1,j1,i2,j2 = self.body[0]
            if self.orientation[0] == Direction.West: # last piece on the left
                self.body[0] = (i1, j1, i2+2*self.bodyHalfWidth+1, j2)
            else:
                self.body[0] = (i1-2*self.bodyHalfWidth-1,j1,i2,j2)
        elif x1 >= x2-2*self.bodyHalfWidth and (orient == Direction.East or orient == Direction.West):
            body1 = self.body.pop(0)
            orient1 = self.orientation.pop(0)
            i1,j1,i2,j2 = self.body[0]
            if self.orientation[0] == Direction.South:   # the last piece move west
                self.body[0] = (i1, j1-2*self.bodyHalfWidth-1, i2, j2)
            else:   # the last piece move east
                self.body[0] = (i1, j1, i2, j2+2*self.bodyHalfWidth+1)

        """
        # move tail
        x1, y1, x2, y2 = self.body[0]
        #print(x1, y1, x2, y2)
        if x1 == x2:    # vertical
            if y1 >= y2 - 2 * self.bodyHalfWidth:
                self.body.pop(0)
                i1, j1, i2, j2 = self.body[0]
                #print(self.body[0])
                if i1 <= x1 - self.bodyHalfWidth: # last piece on the left
                    self.body[0] = (i1, j1, i2+2*self.bodyHalfWidth+1-dec_len, j2)
                else:
                    self.body[0] = (i1-2*self.bodyHalfWidth-1+dec_len,j1,i2,j2)
            elif len(self.body) == 1:   # one segment in body
                if self.curDir == Direction.North:
                    self.body[0] = (x1, y1, x2, y2-dec_len)
                elif self.curDir == Direction.South:
                    self.body[0] = (x1, y1+dec_len, x2, y2)
            else:
                i1, j1, i2, j2 = self.body[1]   # the previous segment of the last piece
                if j1 == y1 + self.bodyHalfWidth:   # the last piece move north
                    self.body[0] = (x1, y1, x2, y2-dec_len)
                else:   # the last piece move south
                    self.body[0] = (x1, y1+dec_len, x2, y2)
        else:   # horizontal
            if y1 == y2 and x1 >= x2 - 2*self.bodyHalfWidth:
                self.body.pop(0)
                i1, j1, i2, j2 = self.body[0]
                #print(self.body[0])
                if j1 <= y1 + self.bodyHalfWidth:      # last piece on the top
                    self.body[0] = (i1, j1, i2, j2+2*self.bodyHalfWidth+1-dec_len)
                else:
                    self.body[0] = (i1, j1-2*self.bodyHalfWidth-1+dec_len, i2, j2)
            elif len(self.body) == 1:    # one segment in body
                if self.curDir == Direction.West:
                    self.body[0] = (x1, y1, x2-dec_len, y2)
                elif self.curDir == Direction.East:
                    self.body[0] = (x1+dec_len, y1, x2, y2)
            else:
                i1, j1, i2, j2 = self.body[1]   # the previous segment of the last piece
                if i1 == x1 + self.bodyHalfWidth:   # the last piece move west
                    self.body[0] = (x1, y1, x2-dec_len, y2)
                else:   # the last piece move east
                    self.body[0] = (x1+dec_len, y1, x2, y2)
        """

        # move head
        x1, y1, x2, y2 = self.body[-1]
        # keep the original direction
        #print(d, self.curDir)
        if d == self.curDir or d == Direction.Stop or ReverseDir(d) == self.curDir:
            if self.curDir == Direction.West:
                self.body[-1] = (x1-inc_len, y1, x2, y2)
            elif self.curDir == Direction.East:
                self.body[-1] = (x1, y1, x2+inc_len, y2)
            elif self.curDir == Direction.North:
                self.body[-1] = (x1, y1-inc_len, x2, y2)
            elif self.curDir == Direction.South:
                self.body[-1] = (x1, y1, x2, y2+inc_len)
        # change direction, add body segment
        elif self.curDir == Direction.North:
            if d == Direction.West:
                self.body.append((x1-self.bodyHalfWidth-inc_len, y1+self.bodyHalfWidth,
                                  x1-self.bodyHalfWidth-1, y1+self.bodyHalfWidth))
            elif d == Direction.East:
                self.body.append((x1+self.bodyHalfWidth+1, y1+self.bodyHalfWidth,
                                  x1+self.bodyHalfWidth+inc_len, y1+self.bodyHalfWidth))
        elif self.curDir == Direction.South:
            if d == Direction.West:
                self.body.append((x2-self.bodyHalfWidth-inc_len, y2-self.bodyHalfWidth,
                                  x2-self.bodyHalfWidth-1, y2-self.bodyHalfWidth))
            elif d == Direction.East:
                self.body.append((x2+self.bodyHalfWidth+1, y2-self.bodyHalfWidth,
                                  x2+self.bodyHalfWidth+inc_len, y2-self.bodyHalfWidth))
        elif self.curDir == Direction.West:
            if d == Direction.North:
                self.body.append((x1+self.bodyHalfWidth, y1-self.bodyHalfWidth-inc_len,
                                  x1+self.bodyHalfWidth, y1-self.bodyHalfWidth-1))
            elif d == Direction.South:
                self.body.append((x1+self.bodyHalfWidth, y1+self.bodyHalfWidth+1,
                                  x1+self.bodyHalfWidth, y1+self.bodyHalfWidth+inc_len))
        elif self.curDir == Direction.East:
            if d == Direction.North:
                self.body.append((x2-self.bodyHalfWidth, y2-self.bodyHalfWidth-inc_len,
                                  x2-self.bodyHalfWidth, y2-self.bodyHalfWidth-1))
            elif d == Direction.South:
                self.body.append((x2-self.bodyHalfWidth, y2+self.bodyHalfWidth+1,
                                  x2-self.bodyHalfWidth, y2+self.bodyHalfWidth+inc_len))
        # change current direction
        if d != Direction.Stop and ReverseDir(d) != self.curDir:
            self.curDir = d
            if d != self.orientation[-1]:
                self.orientation.append(d)

    def _MoveRects(self, d, dec_len, inc_len):
        # move tail
        x1, y1, x2, y2 = self.rects[0]
        orient = self.orientation[0]

        if orient == Direction.North:
            self.rects[0] = (x1,y1,x2,y2-dec_len)
        elif orient == Direction.South:
            self.rects[0] = (x1,y1+dec_len,x2,y2)
        elif orient == Direction.West:
            self.rects[0] = (x1,y1,x2-dec_len,y2)
        else:
            self.rects[0] = (x1+dec_len,y1,x2,y2)

        x1, y1, x2, y2 = self.rects[0]
        if y1 >= y2-2*self.bodyHalfWidth and (orient == Direction.South or orient == Direction.North):
            self.rects.pop(0)
            self.orientation.pop(0)
            i1,j1,i2,j2 = self.rects[0]
            if self.orientation[0] == Direction.West:
                self.rects[0] = (i1, j1, i2 + 2*self.bodyHalfWidth+1, j2)
            else:
                self.rects[0] = (i1-2*self.bodyHalfWidth-1,j1,i2,j2)
        elif x1 >= x2-2*self.bodyHalfWidth and (orient == Direction.East or orient == Direction.West):
            self.rects.pop(0)
            self.orientation.pop(0)
            i1,j1,i2,j2 = self.rects[0]
            if self.orientation[0] == Direction.North:
                self.rects[0] = (i1,j1,i2,j2+2*self.bodyHalfWidth+1)
            else:
                self.rects[0] = (i1,j1-2*self.bodyHalfWidth-1,i2,j2)

        # move head
        x1, y1, x2, y2 = self.rects[-1]
        # keep the original direction
        #print(d, self.curDir)
        if d == self.orientation[-1] or d == Direction.Stop or ReverseDir(d) == self.orientation[-1]:
            if self.orientation[-1] == Direction.West:
                self.rects[-1] = (x1-inc_len, y1, x2, y2)
            elif self.orientation[-1] == Direction.East:
                self.rects[-1] = (x1, y1, x2+inc_len, y2)
            elif self.orientation[-1] == Direction.North:
                self.rects[-1] = (x1, y1-inc_len, x2, y2)
            elif self.orientation[-1] == Direction.South:
                self.rects[-1] = (x1, y1, x2, y2+inc_len)
        # change direction, add body segment
        elif self.orientation[-1] == Direction.North:
            if d == Direction.West:
                self.rects.append((x1-inc_len, y1,
                                  x1-1, y1+2*self.bodyHalfWidth))
            elif d == Direction.East:
                self.rects.append((x2+1, y1,
                                  x2+inc_len, y1+2*self.bodyHalfWidth))
        elif self.orientation[-1] == Direction.South:
            if d == Direction.West:
                self.rects.append((x1-inc_len, y2-2*self.bodyHalfWidth,
                                  x1-1, y2))
            elif d == Direction.East:
                self.rects.append((x2+1, y2-2*self.bodyHalfWidth,
                                  x2+inc_len, y2))
        elif self.orientation[-1] == Direction.West:
            if d == Direction.North:
                self.rects.append((x1, y1-inc_len,
                                  x1+2*self.bodyHalfWidth, y1-1))
            elif d == Direction.South:
                self.rects.append((x1, y2+1,
                                  x1+2*self.bodyHalfWidth, y2+inc_len))
        elif self.orientation[-1] == Direction.East:
            if d == Direction.North:
                self.rects.append((x2-2*self.bodyHalfWidth, y1-inc_len,
                                  x2, y1-1))
            elif d == Direction.South:
                self.rects.append((x2-2*self.bodyHalfWidth, y2+1,
                                  x2, y2+inc_len))
        # change current direction
        if d != Direction.Stop and ReverseDir(d) != self.orientation[-1]:
            self.curDir = d
            if d != self.orientation[-1]:
                self.orientation.append(d)

    def GoDirection(self, d, dec_len=2*SNAKE_WITH_HALH+1, inc_len=2*SNAKE_WITH_HALH+1):
        self._MoveBody(d, dec_len, inc_len)
        #self._MoveRects(d, dec_len, inc_len)

    def Reset(self):
        self.curDir = Direction.East
        #self.body = [(10, 50, 100, 50)]     # line from west to east, from north to south
        self.orientation = [Direction.East]
        #self.rects = [(10, 50-self.bodyHalfWidth, 100, 50+self.bodyHalfWidth)]
        x = randint(0, Grid_X-1-self.initLen)
        y = randint(0, Grid_Y-1)
        self.body = [(x*APPLE_WIDTH, y*APPLE_HEIGHT+self.bodyHalfWidth, APPLE_WIDTH*(self.initLen+x)-1, y*APPLE_HEIGHT+self.bodyHalfWidth)]     # line from west to east, from north to south
        self.rects = [(0, 0, APPLE_WIDTH*6-1, APPLE_WIDTH-1)]
        #self.body = [(0, self.bodyHalfWidth, APPLE_WIDTH*6-1, self.bodyHalfWidth)]     # line from west to east, from north to south
        self.rects = [(0, 0, APPLE_WIDTH*6-1, APPLE_WIDTH-1)]

    def GetBodyRects2(self):
        return copy.deepcopy(self.rects)

    def GetBodyRects(self):
        rects = []
        for x1, y1, x2, y2 in self.body:
            if x1 == x2: #   vertical
                rects.append((x1 - self.bodyHalfWidth, y1, x2 + self.bodyHalfWidth, y2))
            else: #     horizontal
                rects.append((x1, y1 - self.bodyHalfWidth, x2, y2 + self.bodyHalfWidth))
        return rects

    def HitWall(self):
        x1, y1, x2, y2 = self.body[-1]

        if self.curDir == Direction.North and y1 < 0:
            return True
        elif self.curDir == Direction.South and y2 >= SCREEN_HEIGHT:
            return True
        elif self.curDir == Direction.West and x1 < 0:
            return True
        elif self.curDir == Direction.East and x2 >= SCREEN_WITH:
            return True
        return False

    def HitTail(self):
        rects = self.GetBodyRects()
        for i in range(len(rects) - 1):
            if RectIntersect(rects[-1], rects[i]):
                return True
        return False

    def IsDead(self):
        return self.HitWall() or self.HitTail()

    def __deepcopy__(self, memo):
        newSnake = copy.copy(self)
        newSnake.body = copy.deepcopy(self.body, memo)
        newSnake.rects = copy.deepcopy(self.rects, memo)
        newSnake.orientation = copy.deepcopy(self.orientation, memo)
        return newSnake


