import math
import sys


while True:
    bulbs = 0
    try:
        bulbs = int(sys.stdin.readline())
    except EOFError:
        pass
    if bulbs == 0:
        break
    else:
        square = math.floor(math.sqrt(bulbs))
        if square * square == bulbs:
            print('yes')
        else:
            print('no')