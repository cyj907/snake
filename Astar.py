from Direction import Direction
from PriorityQueue import PriorityQueue
from Const import *

class AStar:
    def __init__(self):
        self.directions = []
        self.movStep = 1

    def FindDirections(self, curState):
        pq = PriorityQueue("dist")
        pq.add({"state": curState, "prev": None, "dist": 0 + self.heuristics(curState), "step": 0, "dir": curState.snake.curDir})

        while not pq.IsEmpty():
            elem = pq.pop()

            if self._is_goal(elem["state"]):
                while True:
                    for i in range(self.movStep):
                        self.directions.append(elem["dir"])
                    elem = elem["prev"]
                    if elem is None:
                        break
                return self.directions

            ok_dirs = self._get_ok_dirs_(elem["state"])
            for d in ok_dirs:
                nextState = elem["state"].GetNextState(d)
                for i in range(self.movStep - 1):
                    nextState = nextState.GetNextState(d)
                step = elem["step"] + 1
                dist = step + self.heuristics(nextState)
                pq.add({"state": nextState, "prev": elem, "dist": dist, "step": step, "dir": d})

    def GetDirection(self, curState):
        if len(self.directions) == 0:
            self.FindDirections(curState)
        return self.directions.pop()

    def _get_ok_dirs_(self, state):
        directions = []
        allDirs = [Direction.North, Direction.South, Direction.West, Direction.East]
        for d in allDirs:
            nextState = state.GetNextState(d)
            for i in range(self.movStep - 1):
                nextState = nextState.GetNextState(d)
            if not nextState.snake.IsDead():
                directions.append(d)
        return directions


    def heuristics(self, state):
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

        return dist

    def _is_goal(self, state):
        return state.IsAppleEaten()