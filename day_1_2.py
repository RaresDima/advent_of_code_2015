import os
import sys


INPUT_FILE = os.path.splitext(os.path.split(sys.argv[0])[1])[0] + '_input.txt'

with open(INPUT_FILE) as f:
    raw_data = f.read()

floor_changes = [+1 if char == '(' else -1
                 for char in raw_data]

pos = 0
for i, floor_change in enumerate(floor_changes, 1):
    pos += floor_change
    if pos < 0:
        print(i)
        break
