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

x, y = 0, 0
gifts_per_house = defaultdict(int)

gifts_per_house[(x, y)] += 1

for direction in directions:
    x, y = position_changes[direction](x, y)
    gifts_per_house[(x, y)] += 1

print(len(gifts_per_house))
