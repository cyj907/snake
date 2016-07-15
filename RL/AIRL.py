# head direction
# distance between head and apple (2-d)
# distance between head and the closest barrier, including wall and body segment (2-d)
# distance between head and the closest body segment (3-d), whether this segment is perpendicular or parallel
# the length of the snake

# discount factor
# reward? eat apple: 100
# reward? hit wall: -100
# reward? hit body: -100
# i.e. dead -100

# 400, 400, 400, 2, 4
# two large
# hashing


import traceback
try:
    1/0
except Exception,e:
    print(traceback.format_exc())
