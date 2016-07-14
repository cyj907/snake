from State import State
from RL import QState
from Direction import Direction
from random import randint


def TrainQ():
    directions = [Direction.North, Direction.South, Direction.West, Direction.East]
    qfunc = QState.QFunc()

    qfunc.LoadFile("qvalue.txt")
    maxIter = 1000000
    curIter = 0
    while curIter < maxIter:
        state = State()
        curIter += 1
        print(curIter)

        while True:
            id = randint(0,3)
            d = directions[id]
            nextState = qfunc.UpdateQValue(state, d)
            if nextState == None:
                break
            state = nextState

    qfunc.Save2File("qvalue.txt")


TrainQ()