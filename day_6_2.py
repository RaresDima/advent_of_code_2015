import os
import sys
from enum import Enum

import numpy as np

from typing import *


class Instruction:

    class Type(Enum):
        TURN_ON = 1
        TURN_OFF = 2
        TOGGLE = 3

    type: 'Instruction.Type'
    start_x: int
    start_y: int
    end_x: int
    end_y: int

    def __init__(self,
                 type_: 'Instruction.Type',
                 start_x: int, start_y: int,
                 end_x: int, end_y: int):
        self.type = type_
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

    @staticmethod
    def from_string(s: str) -> 'Instruction':

        if s.startswith('turn on'):
            instruction_type = Instruction.Type.TURN_ON
            s = s[8:]
        elif s.startswith('turn off'):
            instruction_type = Instruction.Type.TURN_OFF
            s = s[9:]
        else:
            instruction_type = Instruction.Type.TOGGLE
            s = s[7:]

        start_point, end_point = s.split(' through ')
        start_x, start_y = map(int, start_point.split(','))
        end_x, end_y = map(int, end_point.split(','))

        return Instruction(instruction_type, start_x, start_y, end_x, end_y)

    def __str__(self) -> str:
        return (f'Instruction['
                f'{self.type} '
                f'({self.start_x},{self.start_y}) -> '
                f'({self.end_x},{self.end_y})]')

    __repr__ = __str__

    def apply_to_grid(self, grid: np.ndarray):
        if self.type == Instruction.Type.TURN_ON:
            grid[self.start_y:self.end_y+1, self.start_x: self.end_x+1] += 1
        elif self.type == Instruction.Type.TURN_OFF:
            grid[self.start_y:self.end_y+1, self.start_x: self.end_x+1] -= 1
        else:
            grid[self.start_y:self.end_y+1, self.start_x: self.end_x+1] += 2
        grid[grid < 0] = 0





INPUT_FILE = os.path.splitext(os.path.split(sys.argv[0])[1])[0] + '_input.txt'

with open(INPUT_FILE) as f:
    raw_data = f.read()

instructions = list(map(Instruction.from_string, raw_data.split('\n')))

grid = np.zeros((1000, 1000), dtype=np.int)

for instruction in instructions:
    print(instruction)
    instruction.apply_to_grid(grid)

print(grid.sum())
