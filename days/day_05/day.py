import numpy as np

from days.base import Day
import re


class Day05(Day):

    def __init__(self):
        super().__init__('days/day_05/input.txt')
        regex = r'(\d+),(\d+) -> (\d+),(\d+)'

        self.lines = np.array([[int(num) for num in re.split(regex, line)[1:5]] for line in self.input_lines])
        mask_shape = np.max(self.lines) + 1
        self.mask = np.zeros((mask_shape, mask_shape), dtype=int)

    @staticmethod
    def parse_simple_line_coordinates(line):
        start_x = min(line[0], line[2])
        stop_x = max(line[0], line[2]) + 1
        start_y = min(line[1], line[3])
        stop_y = max(line[1], line[3]) + 1
        return start_x, stop_x, start_y, stop_y

    @staticmethod
    def check_line_cond(line):
        return line[0] == line[2] or line[1] == line[3]

    @staticmethod
    def check_diagonal_cond(line):
        diff_x = abs(line[0] - line[2])
        diff_y = abs(line[1] - line[3])
        return diff_x == diff_y

    @staticmethod
    def generate_diagonal_indexes(start_x, start_y, stop_x, stop_y):
        iteration_dir_x = 1 if stop_x > start_x else - 1
        iteration_dir_y = 1 if stop_y > start_y else - 1
        return range(start_x, stop_x + iteration_dir_x, iteration_dir_x), range(start_y, stop_y + iteration_dir_y,
                                                                                iteration_dir_y)

    def calculate_dangerous_areas(self):
        dangerous_areas = np.where(self.mask > 1)
        return len(dangerous_areas[0])

    def fill_simple_line(self, line):
        if self.check_line_cond(line):
            start_x, stop_x, start_y, stop_y = self.parse_simple_line_coordinates(line)
            self.mask[start_x:stop_x, start_y: stop_y] += 1

    def part_one(self):
        for line in self.lines:
            self.fill_simple_line(line)
        return self.calculate_dangerous_areas()

    def part_two(self):
        self.mask[:] = 0
        for line in self.lines:
            self.fill_simple_line(line)
            if self.check_diagonal_cond(line):
                x_s, y_s = self.generate_diagonal_indexes(*line)
                for position in zip(x_s, y_s):
                    self.mask[position] += 1
        return self.calculate_dangerous_areas()


if __name__ == '__main__':
    day = Day05()
    print(day.part_one())
    print(day.part_two())
