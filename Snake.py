# -*- coding: cp936 -*-

#2016_6_22
#by cyj

from Const import *
from Direction import Direction, ReverseDir


class Snake:
    def __init__(self):
        self.curDir = Direction.East
        self.bodyHalfWidth = SNAKE_WITH_HALH
        self.body = [(10, 50, 100, 50)]     # line from west to east, from north to south

    def _MoveBody(self, d, dec_len=1, inc_len=1):
        # move tail
        x1, y1, x2, y2 = self.body[0]
        print(x1, y1, x2, y2)
        if x1 == x2:    # vertical
            if y1 >= y2 - 2 * self.bodyHalfWidth:
                print(self.body.pop(0))
                i1, j1, i2, j2 = self.body[0]
                print(self.body[0])
                if i1 <= x1 - self.bodyHalfWidth: # last piece on the left
                    self.body[0] = (i1, j1, i2+2*self.bodyHalfWidth, j2)
                else:
                    self.body[0] = (i1-2*self.bodyHalfWidth,j1,i2,j2)
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
                print(self.body.pop(0))
                i1, j1, i2, j2 = self.body[0]
                print(self.body[0])
                if j1 <= y1 + self.bodyHalfWidth:       # last piece on the top
                    self.body[0] = (i1, j1, i2, j2 + 2*self.bodyHalfWidth)
                else:
                    self.body[0] = (i1, j1-2*self.bodyHalfWidth, i2, j2)
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

        # move head
        x1, y1, x2, y2 = self.body[-1]
        # keep the original direction
        print(d, self.curDir)
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
                self.body.append((x1-self.bodyHalfWidth-inc_len-1, y1+self.bodyHalfWidth,
                                  x1-self.bodyHalfWidth-1, y1+self.bodyHalfWidth))
            elif d == Direction.East:
                self.body.append((x1+self.bodyHalfWidth+1, y1+self.bodyHalfWidth,
                                  x1+self.bodyHalfWidth+inc_len+1, y1+self.bodyHalfWidth))
        elif self.curDir == Direction.South:
            if d == Direction.West:
                self.body.append((x2-self.bodyHalfWidth-inc_len-1, y2-self.bodyHalfWidth,
                                  x2-self.bodyHalfWidth-1, y2-self.bodyHalfWidth))
            elif d == Direction.East:
                self.body.append((x2+self.bodyHalfWidth+1, y2-self.bodyHalfWidth,
                                  x2+self.bodyHalfWidth+inc_len+1, y2-self.bodyHalfWidth))
        elif self.curDir == Direction.West:
            if d == Direction.North:
                self.body.append((x1+self.bodyHalfWidth, y1-self.bodyHalfWidth-inc_len-1,
                                  x1+self.bodyHalfWidth, y1-self.bodyHalfWidth-1))
            elif d == Direction.South:
                self.body.append((x1+self.bodyHalfWidth, y1+self.bodyHalfWidth+1,
                                  x1+self.bodyHalfWidth, y1+self.bodyHalfWidth+inc_len+1))
        elif self.curDir == Direction.East:
            if d == Direction.North:
                self.body.append((x2-self.bodyHalfWidth, y2-self.bodyHalfWidth-inc_len-1,
                                  x2-self.bodyHalfWidth, y2-self.bodyHalfWidth-1))
            elif d == Direction.South:
                self.body.append((x2-self.bodyHalfWidth, y2+self.bodyHalfWidth+1,
                                  x2-self.bodyHalfWidth, y2+self.bodyHalfWidth+inc_len+1))
        # change current direction
        if d != Direction.Stop and ReverseDir(d) != self.curDir:
            self.curDir = d

    def GoDirection(self, d, dec_len=1, inc_len=1):
        self._MoveBody(d, dec_len, inc_len)

    def Reset(self):
        self.curDir = Direction.East
        self.body = [(10, 50, 100, 50)]     # line from west to east, from north to south

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
        return newSnake


