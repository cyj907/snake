

class Direction:
    East = "East"
    South = "South"
    North = "North"
    West = "West"
    Stop = "Stop"

    @staticmethod
    def ReverseDir(d):
        if d == Direction.East:
            return Direction.West
        elif d == Direction.West:
            return Direction.East
        elif d == Direction.South:
            return Direction.North
        elif d == Direction.North:
            return Direction.South
        else:
            return Direction.Stop

def ReverseDir(d):
    if d == Direction.East:
        return Direction.West
    elif d == Direction.West:
        return Direction.East
    elif d == Direction.South:
        return Direction.North
    elif d == Direction.North:
        return Direction.South
    else:
        return Direction.Stop

def LeftDir(d):
    if d == Direction.East:
        return Direction.North
    elif d == Direction.West:
        return Direction.South
    elif d == Direction.North:
        return Direction.West
    elif d == Direction.South:
        return Direction.East
    else:
        return Direction.Stop

def RightDir(d):
    if d == Direction.East:
        return Direction.South
    elif d == Direction.West:
        return Direction.North
    elif d == Direction.North:
        return Direction.East
    elif d == Direction.South:
        return Direction.West
    else:
        return Direction.Stop

