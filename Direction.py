

class Direction:
    East = "East"
    South = "South"
    North = "North"
    West = "West"
    Stop = "Stop"

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
