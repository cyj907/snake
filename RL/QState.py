from collections import defaultdict
from Direction import Direction
from Const import *


class QFunc:
    def __init__(self):
        self.QMat = defaultdict(float)
        self.learning_rate = 0.6
        self.discount = 0.9

    def ExtractQState(self, state):
        snake = state.snake
        apple = state.apple

        snake_body = snake.GetBodyRects()
        snake_head = list(snake_body[-1])
        snake_head[0] /= APPLE_WIDTH
        snake_head[1] /= APPLE_HEIGHT
        snake_head[2] /= APPLE_WIDTH
        snake_head[3] /= APPLE_HEIGHT

        apple_pos = list(apple.GetApplePos())
        apple_pos[0] /= APPLE_WIDTH
        apple_pos[1] /= APPLE_HEIGHT

        head_orient = snake.orientation[-1]
        dist = [1000,1000,1000]
        for i in range(len(snake_body)-1):
            x1, y1, x2, y2 = snake_body[i]
            x1 /= APPLE_WIDTH
            y1 /= APPLE_HEIGHT
            x2 /= APPLE_WIDTH
            y2 /= APPLE_HEIGHT
            tail_orient = snake.orientation[i]
            if head_orient == Direction.North:
                if tail_orient == Direction.North or tail_orient == Direction.South:
                    if x1 == snake_head[0] and y2 <= snake_head[1]:
                        dist[0] = min(snake_head[1] - y2, dist[0])
                    elif y1 <= snake_head[1] <= y2:
                        if x1 <= snake_head[0]:
                            dist[1] = min(snake_head[0]-x1, dist[1])
                        elif x1 >= snake_head[0]:
                            dist[2] = min(x1 - snake_head[0], dist[2])
                else:
                    if x1 <= snake_head[0] <= x2 and y2 <= snake_head[1]:
                        dist[0] = min(snake_head[1]-y2, dist[0])
                    elif y1 == snake_head[1]:
                        if x2 <= snake_head[0]:
                            dist[1] = min(snake_head[0]-x2, dist[1])
                        elif x1 >= snake_head[0]:
                            dist[2] = min(x1 - snake_head[0], dist[2])
            elif head_orient == Direction.South:
                if tail_orient == Direction.North or tail_orient == Direction.South:
                    if x1 == snake_head[2] and y2 >= snake_head[3]:
                        dist[0] = min(y2 - snake_head[3], dist[0])
                    elif y1 <= snake_head[3] <= y2:
                        if x1 >= snake_head[2]:
                            dist[1] = min(x1-snake_head[2], dist[1])
                        elif x2 <= snake_head[2]:
                            dist[2] = min(snake_head[2]-x2, dist[2])
                else:
                    if x1 <= snake_head[2] <= x2 and y2 <= snake_head[3]:
                        dist[0] = min(snake_head[3]-y2, dist[0])
                    elif y1 == snake_head[3]:
                        if x1 >= snake_head[2]:
                            dist[1] = min(x1-snake_head[2], dist[1])
                        elif x2 <= snake_head[2]:
                            dist[2] = min(snake_head[2]-x2, dist[2])
            elif head_orient == Direction.West:
                if tail_orient == Direction.North or tail_orient == Direction.South:
                    if y1 <= snake_head[1] <= y2:
                        if x2 <= snake_head[0]:
                            dist[0] = min(snake_head[0]-x2,dist[0])
                    elif x1 == snake_head[0]:
                        if y1 >= snake_head[1]:
                            dist[1] = min(y1 - snake_head[1], dist[1])
                        elif y2 <= snake_head[1]:
                            dist[2] = min(snake_head[1]-y2, dist[2])
                else:
                    if y1 == snake_head[1]:
                        if x2 <= snake_head[0]:
                            dist[0] = min(snake_head[0]-x2, dist[0])
                    elif x1 <= snake_head[0] <= x2:
                        if y1 >= snake_head[1]:
                            dist[1] = min(y1 - snake_head[1], dist[1])
                        elif y2 <= snake_head[1]:
                            dist[2] = min(snake_head[1]-y2, dist[2])
            else:
                if tail_orient == Direction.North or tail_orient == Direction.South:
                    if y1 <= snake_head[3] <= y2:
                        if x1 >= snake_head[2]:
                            dist[0] = min(x1-snake_head[2],dist[0])
                    elif x1 == snake_head[2]:
                        if y2 <= snake_head[3]:
                            dist[1] = min(snake_head[3]-y2, dist[1])
                        elif y1 >= snake_head[3]:
                            dist[2] = min(y1-snake_head[3], dist[2])
                else:
                    if y1 == snake_head[3]:
                        if x1 >= snake_head[2]:
                            dist[0] = min(x1-snake_head[2], dist[0])
                    elif x1 <= snake_head[2] <= x2:
                        if y2 <= snake_head[3]:
                            dist[1] = min(snake_head[3]-y2, dist[1])
                        elif y1 >= snake_head[3]:
                            dist[2] = min(y1-snake_head[3], dist[2])

        if head_orient == Direction.North:
            dist[0] = min(snake_head[1] - (-1), dist[0])
            dist[1] = min(snake_head[0] - (-1), dist[1])
            dist[2] = min(Grid_X-snake_head[0], dist[2])

            d_ver = -dist[0]
            if dist[1] <= dist[2]:
                d_hor = -dist[1]
            else:
                d_hor = dist[2]

            apple_dist = (snake_head[0]-apple_pos[0],snake_head[1]-apple_pos[1])
        elif head_orient == Direction.South:
            dist[0] = min(Grid_Y-snake_head[3], dist[0])
            dist[1] = min(Grid_X-snake_head[2], dist[1])
            dist[2] = min(snake_head[2]-(-1), dist[2])

            d_ver = dist[0]
            if dist[1] <= dist[2]:
                d_hor = dist[1]
            else:
                d_hor = -dist[2]
            apple_dist = (snake_head[2]-apple_pos[0],snake_head[3]-apple_pos[1])
        elif head_orient == Direction.West:
            dist[0] = min(snake_head[0]-(-1), dist[0])
            dist[1] = min(Grid_Y-snake_head[1],dist[1])
            dist[2] = min(snake_head[1]-(-1),dist[2])

            d_hor = -dist[0]
            if dist[1] <= dist[2]:
                d_ver = dist[1]
            else:
                d_ver = -dist[2]
            apple_dist = (snake_head[0]-apple_pos[0],snake_head[1]-apple_pos[1])
        else:
            dist[0] = min(Grid_X-snake_head[2],dist[0])
            dist[1] = min(snake_head[3]-(-1),dist[1])
            dist[2] = min(Grid_Y-snake_head[3],dist[2])

            d_hor = dist[0]
            if dist[1] <= dist[2]:
                d_ver = -dist[1]
            else:
                d_ver = dist[2]
            apple_dist = (snake_head[2]-apple_pos[0],snake_head[3]-apple_pos[1])

        qstate = (apple_dist, (d_hor, d_ver))
        return qstate

    def UpdateQValue(self, state, d):
        qstate = self.ExtractQState(state)
        s_qstate = self.qstate2str(qstate)
        if state.snake.IsDead():
            for a in [Direction.North, Direction.South, Direction.West, Direction.East]:
                self.QMat[(s_qstate, a)] = -Grid_Y * Grid_X
            return None

        if state.IsAppleEaten():
            for a in [Direction.North, Direction.South, Direction.West, Direction.East]:
                self.QMat[(s_qstate, a)] = Grid_Y * Grid_X
            state.GenNewApple()
            newState = state.GetNextState(d)
            return newState

        newState = state.GetNextState(d)
        newqState = self.ExtractQState(newState)
        s_newqState = self.qstate2str(newqState)

        reward = -5
        best_q = 0
        for a in [Direction.East, Direction.North, Direction.South, Direction.West]:
            q = self.QMat.get((s_newqState, a), 0)
            if q >= best_q:
                best_q = q

        self.QMat[(s_qstate, d)] = self.QMat.get((s_qstate,d),0) + \
                                 self.learning_rate * (reward+self.discount*best_q-self.QMat.get((s_qstate,d),0))
        return newState

    def GetBestDir(self, state):
        qstate = self.ExtractQState(state)
        s_qstate = self.qstate2str(qstate)
        best_q = -100
        best_a = Direction.North
        for a in [Direction.North, Direction.South, Direction.West, Direction.East]:
            q = self.QMat.get((s_qstate, a),0)
            print q
            if q > best_q:
                best_a = a
                best_q = q
        return best_a

    def qstate2str(self, qstate):
        s = ""
        s += str(qstate[0][0]) + "\t" + str(qstate[0][1]) + "\t"
        s += str(qstate[1][0]) + "\t" + str(qstate[1][1])
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
            s_qstate = "\t".join([words[0], words[1], words[2], words[3]])
            d = words[4]
            val = float(words[5])
            self.QMat[(s_qstate,d)] = val
        fileHandle.close()