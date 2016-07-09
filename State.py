from Snake import Snake
from Apple import Apple
from Const import *

class State:
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()
        self.addedWidth = 0
        self.snakeMovSpeed = 2 * SNAKE_WITH_HALH + 1 # min = 2
        self.eatenAppleCount = 0

    def _IsAppleHitSnake(self):
        appleRect = self.apple.getRect()
        snakeRects = self.snake.GetBodyRects()

        for rect in snakeRects:
            if RectIntersect(rect, appleRect):
                return True

        return False

    def IncreaseMovSpeed(self):
        if self.eatenAppleCount % 10 == 0 and self.snakeMovSpeed <= SNAKE_WITH_HALH * 2 + 1:
            self.snakeMovSpeed += 1

    def IsAppleEaten(self):
        appleRect = self.apple.getRect()
        snakeRects = self.snake.GetBodyRects()
        if RectIntersect(snakeRects[-1], appleRect):
            self.eatenAppleCount += 1
            return True
        return False

    @staticmethod
    def GenNewApple(state):
        state.apple.SetApple()
        while state._IsAppleHitSnake():
            state.apple.SetApple()

    def ResetSnake(self):
        self.snake.Reset()
        self.snakeMovSpeed = 2 * SNAKE_WITH_HALH + 1

    def IsSnakeDead(self, state):
        return state.snake.IsDead()

    def __deepcopy__(self, memo):
        newState = copy.copy(self)
        newState.snake = copy.deepcopy(self.snake)
        newState.apple = copy.deepcopy(self.apple)
        return newState

    def GetNextState(self, d):
        nextState = copy.deepcopy(self)
        if nextState.addedWidth > 0:
            reducedWidth = min(nextState.snakeMovSpeed, APPLE_WIDTH)
            if nextState.addedWidth >= reducedWidth:
                nextState.snake.GoDirection(d, nextState.snakeMovSpeed, nextState.snakeMovSpeed+reducedWidth)
                nextState.addedWidth -= reducedWidth
            else:
                nextState.snake.GoDirection(d, nextState.addedWidth, nextState.addedWidth)
                nextState.addedWidth = 0
        else:
            nextState.snake.GoDirection(d, self.snakeMovSpeed, self.snakeMovSpeed)

        return nextState

