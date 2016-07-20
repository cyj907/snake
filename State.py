from Snake import Snake
from Apple import Apple
from Const import *

class State:
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()
        self.addedWidth = 0
        self.snakeMovSpeed = 2*SNAKE_WITH_HALH+1 # min = 2
        self.eatenAppleCount = 0
        self.GenNewApple()

    def _IsAppleHitSnake(self):
        appleRect = self.apple.getRect()
        snakeRects = self.snake.GetBodyRects()

        for rect in snakeRects:
            if RectIntersect(rect, appleRect):
                return True

        return False

    def IncreaseMovSpeed(self):
        if self.eatenAppleCount % 10 == 0:
            #self.snakeMovSpeed += 2*SNAKE_WITH_HALH+1
            pass

    def IsAppleEaten(self):
        appleRect = self.apple.getRect()
        snakeRects = self.snake.GetBodyRects()
        if RectIntersect(snakeRects[-1], appleRect):
            self.eatenAppleCount += 1
            return True
        return False

    def GenNewApple(self):
        self.apple.SetApple()
        while self._IsAppleHitSnake():
            self.apple.SetApple()

    def AddSnakeLen(self):
        self.addedWidth += APPLE_WIDTH

    def ResetSnake(self):
        self.snake.Reset()
        self.snakeMovSpeed = 2*SNAKE_WITH_HALH+1

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
            nextState.snake.GoDirection(d, nextState.snakeMovSpeed-nextState.addedWidth, nextState.snakeMovSpeed)
            nextState.addedWidth = 0
        else:
            nextState.snake.GoDirection(d, self.snakeMovSpeed, self.snakeMovSpeed)

        return nextState

