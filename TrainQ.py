from State import State
from RL import QState, QState2
from Direction import Direction
from random import randint


def TrainQ():
    directions = [Direction.North, Direction.South, Direction.West, Direction.East]
    qfunc = QState2.QFunc()

    qfunc.LoadFile("qvalue.txt")
    curIter = 0
    while True:
        try:
            state = State()
            curIter += 1
            if curIter % 10000 == 0:
                print(curIter)

            while True:
                id = randint(0,3)
                d = directions[id]
                nextState = qfunc.UpdateQValue(state, d)
                if nextState == None:
                    break
                state = nextState
        except KeyboardInterrupt:
            qfunc.Save2File("qvalue.txt")
            break


TrainQ()