import os
import sys


def get_paper_needed_for_box(l: int, w: int, h: int) -> int:
    side1_area = l * w
    side2_area = w * h
    side3_area = h * l
    smallest_side_area = min(side1_area, side2_area, side3_area)
    return 2 * (side1_area + side2_area + side3_area) + smallest_side_area


INPUT_FILE = os.path.splitext(os.path.split(sys.argv[0])[1])[0] + '_input.txt'

with open(INPUT_FILE) as f:
    raw_data = f.read()

gift_sizes = [list(map(int, row.split('x')))
              for row in raw_data.split('\n')]

paper_needs = list(map(get_paper_needed_for_box, *zip(*gift_sizes)))

print(sum(paper_needs))
