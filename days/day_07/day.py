import numpy as np

from days.base import Day


class Day07(Day):

    def __init__(self):
        super().__init__('days/day_07/input.txt')
        self.crab_positions = np.array(self.input_lines[0].split(','), dtype=int)

    def calculate_distance(self, value):
        return np.abs(self.crab_positions - np.ones_like(self.crab_positions) * value)

    def get_min_max_vals(self):
        return np.min(self.crab_positions), np.max(self.crab_positions)

    def part_one(self):
        min_val, max_val = self.get_min_max_vals()
        fuel_consumptions = [np.sum(self.calculate_distance(val)) for val in
                             range(min_val, max_val + 1)]
        return min(fuel_consumptions)

    def part_two(self):
        min_val, max_val = self.get_min_max_vals()
        fuel_consumptions = [np.sum(value / 2 * (1 + value)) for value in
                             (self.calculate_distance(val) for val in
                              range(min_val, max_val + 1))]
        return int(min(fuel_consumptions))


if __name__ == '__main__':
    day = Day07()
    print(day.part_one())
    print(day.part_two())
