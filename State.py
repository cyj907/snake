from Snake import Snake
from Apple import Apple
from Const import *

class State:
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()
        self.addedWidth = 0
        self.snakeMovSpeed = 1
        self.eatenAppleCount = 0

    def _IsAppleHitSnake(self):
        appleRect = self.apple.getRect()
        snakeRects = self.snake.GetBodyRects()

        for rect in snakeRects:
            if RectIntersect(rect, appleRect):
                return True

        return False

    def IncreaseMovSpeed(self):
        if self.eatenAppleCount == 5:
            self.snakeMovSpeed += 1
            self.eatenAppleCount = 0

    def IsAppleEaten(self):
        appleRect = self.apple.getRect()
        snakeRects = self.snake.GetBodyRects()
        if RectIntersect(snakeRects[-1], appleRect):
            self.eatenAppleCount += 1
            return True
        return False

    def ResetSnake(self):
        self.snake.Reset()
        self.snakeMovSpeed = 1

    def IsSnakeDead(self, state):
        return state.snake.IsDead()

    def __deepcopy__(self, memo):
        newState = copy.copy(self)
        newState.snake = copy.deepcopy(self.snake)
        newState.apple = copy.deepcopy(self.apple)
        return newState

    def GetNextState(self, d):
        nextState = copy.deepcopy(self)
        if nextState.IsAppleEaten():
            nextState.addedWidth += APPLE_WIDTH
            nextState.snake.GoDirection(d, self.snakeMovSpeed, self.snakeMovSpeed+1)
            nextState.addedWidth -= 1
            nextState.apple.SetApple()
            while nextState._IsAppleHitSnake():
                nextState.apple.SetApple()
        elif nextState.addedWidth > 0:
            nextState.addedWidth -= 1
            nextState.snake.GoDirection(d, self.snakeMovSpeed, self.snakeMovSpeed+1)
        else:
            nextState.snake.GoDirection(d, self.snakeMovSpeed, self.snakeMovSpeed)

        return nextState

