import os
import sys
from string import ascii_lowercase
from operator import mul
from functools import partial


def has_non_verlapping_repeated_pairs(s: str) -> bool:
    pair_set = set()
    pair_to_add_next_loop = None
    pair_to_add_this_loop = None

    for char1, char2 in zip(s[:-1], s[1:]):
        pair = char1 + char2

        pair_set.add(pair_to_add_this_loop)
        pair_to_add_this_loop = pair_to_add_next_loop
        pair_to_add_next_loop = pair

        if pair in pair_set:
            return True

    return False


def has_triple_with_same_edges(s: str) -> bool:
    for char1, _, char3 in zip(s[:-2], s[1:-1], s[2:]):
        if char1 == char3:
            return True
    return False


def is_nice_string(s: str) -> bool:
    return has_non_verlapping_repeated_pairs(s) and has_triple_with_same_edges(s)


INPUT_FILE = os.path.splitext(os.path.split(sys.argv[0])[1])[0] + '_input.txt'

with open(INPUT_FILE) as f:
    raw_data = f.read()

strings = raw_data.split('\n')

print(f'Nice strings: {sum(map(is_nice_string, strings))}/{len(strings)}')
