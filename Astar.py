from Direction import Direction
from PriorityQueue import PriorityQueue
from Const import *

class AStar:
    def __init__(self):
        self.directions = []

    def FindDirections(self, curState):
        pq = PriorityQueue(["dist", "changeDir"])
        pq.add({"state": curState, "prev": None, "dist": 0 + self.heuristics(curState), "changeDir": 0, "step": 0})
        cnt = 0
        while True:
            elem = pq.pop()
            #print("Dir:", elem["state"].snake.curDir, "step:", elem["step"], "cnt: ", cnt)

            ok_dirs = self._get_ok_dirs_(elem["state"])
            #print ok_dirs
            for d in ok_dirs:
                nextState = elem["state"].GetNextState(d)

                step = elem["step"] + 1
                changeDir = 0
                if d != elem["state"].snake.curDir:
                    changeDir = 1
                dist = step + self.heuristics(nextState)

                pq.add({"state": nextState, "prev": elem, "dist": dist, "changeDir":changeDir, "step": step} )

            #if elem["step"] % 10 == 0:
            #    print elem["step"]
            if pq.IsEmpty():
                print "EMPTY!!!!", elem["step"]
                if len(pq.storage) > 0:
                    elem = pq.storage.pop(0)
                    pq.add(elem)
                """
                while len(pq.storage) > 0:
                    other = pq.storage.pop()
                    print other["step"], elem["step"]
                    if abs(other["step"] - elem["step"]) < elem["step"] * 0.1:
                        break
                        """
                print elem["state"].IsAppleEaten(), elem["state"].apple.GetApplePos()
                #pq.add(other)

            cnt += 1
            if cnt >= 2000 or self._is_goal(elem["state"]) and elem["step"] > 0:
                #print("step:", elem["step"], "cnt:", cnt, "empty:", pq.IsEmpty())
                pq.clean()
                while True:
                    self.directions.append(elem["state"].snake.curDir)
                    elem = elem["prev"]
                    if elem is None:
                        break
                self.directions.pop() # remove the first direction (the state that already take a step)

                return self.directions


    def GetDirection(self, curState):
        if len(self.directions) == 0:
            #print ("Find Directions!")
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

    def _is_goal(self, state):
        return state.IsAppleEaten()