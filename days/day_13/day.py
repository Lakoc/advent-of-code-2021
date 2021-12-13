from days.base import Day
import numpy as np


class Day13(Day):

    def __init__(self):
        super().__init__('days/day_13/input.txt')
        empty_line_index = self.input_lines.index('\n')
        indexes = np.array(
            [[int(char) for char in line.strip().split(',')] for line in self.input_lines[:empty_line_index]])
        self.folds = [[char for char in line.split()[-1].split('=')] for line in
                      self.input_lines[empty_line_index + 1:]]
        max_val = np.max(indexes + 1, axis=0)
        self.mask = np.zeros(max_val, dtype=bool)
        self.mask[indexes[:, 0], indexes[:, 1]] = True

    def simulate_single_fold(self, axis, position):
        position = int(position)
        if axis == 'x':
            static = self.mask[:position, :]
            folded = self.mask[position + 1:, :]
            rotated = folded[::-1, :]
        else:
            static = self.mask[:, :position]
            folded = self.mask[:, position + 1:]
            rotated = folded[:, ::-1]

        self.mask = np.logical_or(static, rotated)

    def part_one(self):
        first_fold = self.folds[0]
        original_mask = self.mask
        self.simulate_single_fold(first_fold[0], first_fold[1])
        visible = np.count_nonzero(self.mask)
        self.mask = original_mask
        return visible

    def part_two(self):
        for fold in self.folds:
            self.simulate_single_fold(fold[0], fold[1])
        return '\n'.join([''.join(['#' if item else ' ' for item in row])
                         for row in self.mask.T])


if __name__ == '__main__':
    day = Day13()
    print(day.part_one())
    print(day.part_two())
