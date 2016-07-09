from Direction import Direction
from PriorityQueue import PriorityQueue
from Const import *

class AIBDFS:

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

    def _is_possible_dead_(self, state):
        bodyLen = 0
        for x1, y1, x2, y2 in state.snake.body:
            if x1 == x2:
                bodyLen += y2 - y1 + 1
            else:
                bodyLen += x2 - x1 + 1

        steps = bodyLen / state.snakeMovSpeed + 1
        stack = []
        stack.append({"state": state, "depth": 0})
        while len(stack) > 0:
            elem = stack.pop()
            if elem["depth"] >= steps:
                return False

            ok_dirs = self._get_ok_dirs_(elem["state"])
            for d in ok_dirs:
                stack.append({"state": elem["state"].GetNextState(d), "depth": elem["depth"]+1})
        return True

    def FindDirections(self, curState):
        print(curState.apple.GetApplePos())
        self.directions = []
        pq = PriorityQueue(["dist"])
        maxDepth = 5
        pq.add({"state": curState, "dist": self.heuristics(curState), "step": 0, "prev": None})
        cnt = 0
        while not pq.IsEmpty():
            elem = pq.pop()
            state = elem["state"]
            stack = []
            stack.append({"state": state, "step": 0, "prev": elem["prev"]})

            if cnt >= SCREEN_WITH + SCREEN_HEIGHT - 4 * SNAKE_WITH_HALH - 2:
                print cnt
                cnt = 0
                pq.pop()
                continue

            while len(stack) > 0:
                el = stack.pop()
                stat = el["state"]
                cnt += 1

                if el["step"] == maxDepth:
                    pq.add({"state": stat, "dist": self.heuristics(stat), "step": el["step"], "prev": el["prev"]})
                    continue

                if stat.IsAppleEaten():
                    # guess if the snake can be dead by instinct
                    if self._is_possible_dead_(stat):
                        continue
                    while el is not None:
                        self.directions.append(el["state"].snake.curDir)
                        el = el["prev"]
                    self.directions.pop()
                    return

                ok_dirs = self._arange_dirs_(stat, self._get_ok_dirs_(stat))
                for d in ok_dirs:
                    nextStat = stat.GetNextState(d)
                    nextEl = {"state": nextStat, "step": el["step"]+1, "prev": el}
                    stack.append(nextEl)

        self.directions.append(Direction.Stop)

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