from collections import defaultdict
from Direction import Direction
from Const import *
from random import randint

class QFunc:
    def __init__(self):
        self.QMat = defaultdict(float)
        self.learning_rate = 0.4
        self.discount = 0.8

    def __is_wall__(self, x, y):
        if x < 0 or y < 0 or x >= Grid_X or y >= Grid_Y:
            return True
        return False

    def __is_body__(self, x, y, body):
        for x1, y1, x2, y2 in body:
            x1 = x1 / APPLE_WIDTH
            y1 = y1 / APPLE_HEIGHT
            x2 = x2 / APPLE_WIDTH
            y2 = y2 / APPLE_HEIGHT
            if x1 <= x <= x2 and y1 <= y <= y2:
                return True
        return False

    def __is_apple__(self, x, y, apple_pos):
        if x == apple_pos[0] / APPLE_WIDTH and y == apple_pos[1] / APPLE_HEIGHT:
            return True
        return False

    def ExtractQState(self, state):
        snake = state.snake
        apple = state.apple

        snake_body = snake.GetBodyRects()
        snake_head = list(snake_body[-1])
        head_x = snake_head[0] / APPLE_WIDTH
        head_y = snake_head[1] / APPLE_HEIGHT
        apple_pos = list(apple.GetApplePos())

        qstate = [0 for i in range(9)]
        # 0: blank, 1: body, 2: wall, 3: apple
        ii = 0
        for x in [head_x-1,head_x,head_x+1]:
            for y in [head_y-1,head_y,head_y+1]:
                if self.__is_body__(x, y, snake_body):
                    qstate[ii] = 1
                elif self.__is_apple__(x, y, apple_pos):
                    qstate[ii] = 3
                elif self.__is_wall__(x, y):
                    qstate[ii] = 2
                ii += 1
        return qstate

    def UpdateQValue(self, state, d):
        qstate = self.ExtractQState(state)
        s_qstate = self.qstate2str(qstate)
        if state.snake.IsDead():
            for a in [Direction.North, Direction.South, Direction.West, Direction.East]:
                self.QMat[(s_qstate, a)] = -500
            return None

        reward = -10
        if state.IsAppleEaten():
            state.GenNewApple()
            newState = state.GetNextState(d)
            reward = 500
        else:
            newState = state.GetNextState(d)

        newqState = self.ExtractQState(newState)
        s_newqState = self.qstate2str(newqState)

        best_q = float("-inf")
        for a in [Direction.East, Direction.North, Direction.South, Direction.West]:
            q = self.QMat.get((s_newqState, a), 0)
            if q > best_q:
                best_q = q

        self.QMat[(s_qstate, d)] = self.QMat.get((s_qstate,d),0) + \
                                 self.learning_rate * (reward+self.discount*best_q-self.QMat.get((s_qstate,d),0))
        if self.QMat[(s_qstate, d)] > 500:
            self.QMat[(s_qstate, d)] = 500
        return newState

    def GetBestDir(self, state):
        qstate = self.ExtractQState(state)
        s_qstate = self.qstate2str(qstate)
        directions = [Direction.North, Direction.South, Direction.West, Direction.East]
        best_q = -100
        best_a = directions[randint(0,3)]
        for a in directions:
            q = self.QMat.get((s_qstate, a),0)
            #print q
            if q > best_q:
                best_a = a
                best_q = q
        return best_a

    def qstate2str(self, qstate):
        s = ""
        for i in range(len(qstate)):
            s += str(qstate[i])
        return s

    def Save2File(self, filename): # save q value matrix
        fileHandle = open(filename, 'w')
        for s_qstate, d in self.QMat:
            val = self.QMat[(s_qstate, d)]
            fileHandle.write(s_qstate + "\t" + d + "\t" + str(val) + "\n")
        fileHandle.close()

    def LoadFile(self, filename): # load q value matrix
        self.QMat = {}
        fileHandle = open(filename, 'r')
        lines = [line.rstrip('\n') for line in fileHandle]
        for line in lines:
            words = line.split("\t")
            s_qstate = words[0]
            d = words[1]
            val = float(words[2])
            self.QMat[(s_qstate,d)] = val
        fileHandle.close()