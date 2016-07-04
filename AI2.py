from Const import *
from Direction import Direction

class AI2:
    def __AppleIsUp(self, snake_pos, apple_pos):
        return apple_pos[1]+APPLE_HEIGHT-1< snake_pos[1]

    def __AppleIsUpWithHalf(self, snake_pos, apple_pos):
        return apple_pos[1]+APPLE_HEIGHT-1<snake_pos[1]-SNAKE_WITH_HALH

    def __AppleIsDown(self, snake_pos, apple_pos):
        return apple_pos[1]>snake_pos[1]

    def __AppleIsDownWithHalf(self, snake_pos, apple_pos):
        return apple_pos[1]>snake_pos[1]+SNAKE_WITH_HALH

    def __AppleIsLeft(self, snake_pos, apple_pos):
        return apple_pos[0]+APPLE_WIDTH-1<snake_pos[0]

    def __AppleIsLeftWithHalf(self, snake_pos, apple_pos):
        return apple_pos[0]+APPLE_WIDTH-1<snake_pos[0]-SNAKE_WITH_HALH

    def __AppleIsRight(self, snake_pos, apple_pos):
        return apple_pos[0]>snake_pos[0]

    def __AppleIsRightWithHalf(self, snake_pos, apple_pos):
        return apple_pos[0]>snake_pos[0]+SNAKE_WITH_HALH

    def GetDirection(self, curState):
        snake = curState.snake
        apple = curState.apple
        snake_dir = snake.curDir
        x1, y1, x2, y2 = snake.body[-1]
        if snake_dir == Direction.North or snake_dir == Direction.West:
            snake_pos = (x1, y1)
        elif snake_dir == Direction.South or snake_dir == Direction.East:
            snake_pos = (x2, y2)
        else:
            snake_pos = (0, 0)
        apple_pos = apple.GetApplePos()
        directions = []
        if snake_dir == Direction.North or snake_dir == Direction.South:
            if snake_dir == Direction.North:
                if self.__AppleIsUp(snake_pos, apple_pos):
                    directions.append(Direction.North)
            else:
                if self.__AppleIsDown(snake_pos, apple_pos):
                    directions.append(Direction.South)

            if self.__AppleIsLeftWithHalf(snake_pos, apple_pos):
                directions.append(Direction.West)
            elif self.__AppleIsRightWithHalf(snake_pos, apple_pos):
                directions.append(Direction.East)

            directions.append(snake_dir)
        else:
            if snake_dir == Direction.West:
                if self.__AppleIsLeft(snake_pos, apple_pos):
                    directions.append(Direction.West)
            else:
                if self.__AppleIsRight(snake_pos, apple_pos):
                    directions.append(Direction.East)

            if self.__AppleIsUpWithHalf(snake_pos, apple_pos):
                directions.append(Direction.North)
            elif self.__AppleIsDownWithHalf(snake_pos, apple_pos):
                directions.append(Direction.South)

            directions.append(snake_dir)

        for d in directions:
            if not snake.IsDead():
                return d

        for d in set([Direction.North,Direction.South,Direction.West,Direction.East])-set(directions):
            if not snake.IsDead():
                return d

        return None
