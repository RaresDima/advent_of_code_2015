import os
import sys
from string import ascii_lowercase
from operator import mul
from functools import partial


vowels = {'a', 'e', 'i', 'o', 'u'}
double_letters = set(map(partial(mul, 2), ascii_lowercase))
naughty_pairs = {'ab', 'cd', 'pq', 'xy'}


def is_nice_string(s: str) -> bool:
    global vowels
    global double_letters
    global naughty_pairs
    num_vowels = int(s[-1] in vowels)
    vowels_ok = False
    double_letters_ok = False
    for char, next_char in zip(s[:-1], s[1:]):
        if not vowels_ok and char in vowels:
            num_vowels += 1
            if num_vowels >= 3:
                vowels_ok = True
        if not double_letters_ok and char == next_char:
            double_letters_ok = True
        if char + next_char in naughty_pairs:
            return False
    return vowels_ok and double_letters_ok


INPUT_FILE = os.path.splitext(os.path.split(sys.argv[0])[1])[0] + '_input.txt'

with open(INPUT_FILE) as f:
    raw_data = f.read()

strings = raw_data.split('\n')

print(f'Nice strings: {sum(map(is_nice_string, strings))}/{len(strings)}')
