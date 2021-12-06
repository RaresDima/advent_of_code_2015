import os
import sys


def get_ribbon_needed_for_box(l: int, w: int, h: int) -> int:
    side1_perimeter = 2 * (l + w)
    side2_perimeter = 2 * (w + h)
    side3_perimeter = 2 * (h + l)
    smallest_side_perimeter = min(side1_perimeter, side2_perimeter, side3_perimeter)
    volume = l * w * h
    return smallest_side_perimeter + volume


INPUT_FILE = os.path.splitext(os.path.split(sys.argv[0])[1])[0] + '_input.txt'

with open(INPUT_FILE) as f:
    raw_data = f.read()

gift_sizes = [list(map(int, row.split('x')))
              for row in raw_data.split('\n')]

ribbon_needs = list(map(get_ribbon_needed_for_box, *zip(*gift_sizes)))

print(sum(ribbon_needs))
