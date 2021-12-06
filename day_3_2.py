import os
import sys
from collections import defaultdict



position_changes = {'^': lambda x, y: (x, y+1),
                    '>': lambda x, y: (x+1, y),
                    '<': lambda x, y: (x-1, y),
                    'v': lambda x, y: (x, y-1)}


INPUT_FILE = os.path.splitext(os.path.split(sys.argv[0])[1])[0] + '_input.txt'

with open(INPUT_FILE) as f:
    raw_data = f.read()

directions = raw_data

santa_x, santa_y = robo_santa_x, robo_santa_y = 0, 0

gifts_per_house = defaultdict(int)

gifts_per_house[(santa_x, santa_y)] += 1
gifts_per_house[(robo_santa_x, robo_santa_y)] += 1

for santa_direction, robo_santa_direction in zip(directions[::2], directions[1::2]):
    santa_x, santa_y = position_changes[santa_direction](santa_x, santa_y)
    robo_santa_x, robo_santa_y = position_changes[robo_santa_direction](robo_santa_x, robo_santa_y)
    gifts_per_house[(santa_x, santa_y)] += 1
    gifts_per_house[(robo_santa_x, robo_santa_y)] += 1

print(len(gifts_per_house))
