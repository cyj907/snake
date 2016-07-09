from Direction import Direction
from random import randint

class AIDFS:

    def __init__(self):
        self.directions = []

    def _arange_dirs_(self, state, dirs):
        elems = []
        for d in dirs:
            elems.append((d, self.heuristics(state.GetNextState(d))))

        for i in range(len(elems) - 1):
            for j in range(len(elems)):
                if elems[i][1] < elems[j][1]:
                    tmp = elems[i]
                    elems[i] = elems[j]
                    elems[j] = tmp

        res_dirs = []
        for elem in elems:
            res_dirs.append(elem[0])
        return res_dirs

    def FindDirections(self, curState):
        print(curState.apple.GetApplePos())
        self.directions = []
        stack = []
        elem = (curState, None, 0)
        stack.append(elem)
        cnt = 0
        while True:
            if len(stack) == 0:
                self.directions.append(Direction.Stop)
                return
            elem = stack.pop()
            state = elem[0]
            cnt += 1
            if cnt > 1000:
                print curState.snake.GetBodyRects()
                print curState.apple.GetApplePos()
                print curState.IsAppleEaten()
                print "WTF"
                cntRemoved = randint(int(len(stack) * 0.9), len(stack))
                if len(stack) - cntRemoved >= 1 and len(stack) > 1:
                    for i in range(cntRemoved):
                        stack.pop()
                print "len of stack", len(stack)
                cnt = 0
                continue

            if state.IsAppleEaten():
                print "cnt = ", cnt
                while elem is not None:
                    self.directions.append(elem[0].snake.curDir)
                    elem = elem[1]
                self.directions.pop()
                return

            ok_dirs = self._arange_dirs_(state, self._get_ok_dirs_(state))

            for d in ok_dirs:
                nextState = state.GetNextState(d)
                nextElem = (nextState, elem)

                stack.append(nextElem)

    def GetDirection(self, curState):
        if len(self.directions) == 0:
            print "Find Directions"
            self.FindDirections(curState)
        return self.directions.pop()

    def _get_ok_dirs_(self, state):
        directions = []
        allDirs = [Direction.North, Direction.South, Direction.West, Direction.East]
        for d in allDirs:
            if d == Direction.ReverseDir(state.snake.curDir):
                continue
            nextState = state.GetNextState(d)
            if not nextState.snake.IsDead():
                directions.append(d)
        return directions


    def heuristics(self, state):
        # TODO: take snake body into consideration
        # the manhattan distance between snake head and the closest edge of apple
        apple_pos = state.apple.getRect()
        snake_head = state.snake.body[-1]
        snake_dir = state.snake.curDir
        dist = 0
        if snake_dir == Direction.North:
            snake_x1 = snake_head[0] - state.snake.bodyHalfWidth
            snake_x2 = snake_head[0] + state.snake.bodyHalfWidth
            if snake_x1 > apple_pos[2]:
                dist += snake_x1 - apple_pos[2]
            elif snake_x2 < apple_pos[0]:
                dist += apple_pos[0] - snake_x2

            # take the body width into consideration
            snake_y1 = snake_head[1]
            snake_y2 = snake_head[1] + state.snake.bodyHalfWidth * 2
            if apple_pos[3] < snake_y1:
                dist += snake_y1 - apple_pos[3]
            elif apple_pos[1] > snake_y2:
                dist += apple_pos[1] - snake_y2

            """
            if snake_y1 > apple_pos[3]:
                if snake_x1 < apple_pos[2]:
                    rect = snake_x1, apple_pos[3], apple_pos[2], snake_y1
                    bodyRects = state.snake.GetBodyRects()
                    addedLen = 0
                    for i in range(len(bodyRects)):
                        if RectIntersect(rect, bodyRects[i]):
                            tmp = max(bodyRects[i][3]-bodyRects[i][1], bodyRects[i][2]-bodyRects[0])
                            addedLen = max(addedLen, tmp)
                    dist += addedLen
                elif snake_x2 > apple_pos[0]:
                    rect = apple_pos[0], apple_pos[3], snake_y2, snake_y1
                    bodyRects = state.snake.GetBodyRects()
                    addedLen = 0
                    for i in range(len(bodyRects)):
                        if RectIntersect(rect, bodyRects[i]):
                            tmp = max(bodyRects[i][3]-bodyRects[i][1], bodyRects[i][2]-bodyRects[0])
                            addedLen = max(addedLen, tmp)
                    dist += addedLen
            """
            """
            if apple_pos[3] < snake_head[1]:
                dist += snake_head[1] - apple_pos[3]
            elif apple_pos[1] > snake_head[1]:
                dist += apple_pos[1] - snake_head[1]
            """
        elif snake_dir == Direction.South:
            snake_x1 = snake_head[2] - state.snake.bodyHalfWidth
            snake_x2 = snake_head[2] + state.snake.bodyHalfWidth
            if snake_x1 > apple_pos[2]:
                dist += snake_x1 - apple_pos[2]
            elif snake_x2 < apple_pos[0]:
                dist += apple_pos[0] - snake_x2

            # take the body width into consideration
            snake_y1 = snake_head[3] - state.snake.bodyHalfWidth * 2
            snake_y2 = snake_head[3]
            if apple_pos[3] < snake_y1:
                dist += snake_y1 - apple_pos[3]
            elif apple_pos[1] > snake_y2:
                dist += apple_pos[1] - snake_y2

            """
            if apple_pos[3] < snake_head[3]:
                dist += snake_head[3] - apple_pos[3]
            elif apple_pos[1] > snake_head[3]:
                dist += apple_pos[1] - snake_head[3]
            """

        elif snake_dir == Direction.West:
            snake_y1 = snake_head[1] - state.snake.bodyHalfWidth
            snake_y2 = snake_head[1] + state.snake.bodyHalfWidth
            if snake_y1 > apple_pos[3]:
                dist += snake_y1 - apple_pos[3]
            elif snake_y2 < apple_pos[1]:
                dist += apple_pos[1] - snake_y2

            snake_x1 = snake_head[0]
            snake_x2 = snake_head[0] + state.snake.bodyHalfWidth * 2
            if apple_pos[2] < snake_x1:
                dist += snake_x1 - apple_pos[2]
            elif apple_pos[0] > snake_x2:
                dist += apple_pos[0] - snake_x2
            """
            if apple_pos[2] < snake_head[0]:
                dist += snake_head[0] - apple_pos[2]
            elif apple_pos[0] > snake_head[0]:
                dist += apple_pos[0] - snake_head[0]
            """
        elif snake_dir == Direction.East:
            snake_y1 = snake_head[3] - state.snake.bodyHalfWidth
            snake_y2 = snake_head[3] + state.snake.bodyHalfWidth
            if snake_y1 > apple_pos[3]:
                dist += snake_y1 - apple_pos[3]
            elif snake_y2 < apple_pos[1]:
                dist += apple_pos[1] - snake_y2

            snake_x1 = snake_head[2] - state.snake.bodyHalfWidth * 2
            snake_x2 = snake_head[2]
            if apple_pos[2] < snake_x1:
                dist += snake_x1 - apple_pos[2]
            elif apple_pos[0] > snake_x2:
                dist += apple_pos[0] - snake_x2
            """
            if apple_pos[2] < snake_head[2]:
                dist += snake_head[2] - apple_pos[2]
            elif apple_pos[0] > snake_head[2]:
                dist += apple_pos[0] - snake_head[2]
            """

        return dist
