import numpy as np

from days.base import Day


class Day07(Day):

    def __init__(self):
        super().__init__('days/day_07/input.txt')
        self.crab_positions = np.array(list(map(int, self.input_lines[0].split(','))))

    def part_one(self):
        min_val = np.min(self.crab_positions)
        max_val = np.max(self.crab_positions)
        fuel_consumptions = [np.sum(np.abs(self.crab_positions - np.ones_like(self.crab_positions) * val)) for val in
                             range(min_val, max_val + 1)]
        return min(fuel_consumptions)

    def part_two(self):
        min_val = np.min(self.crab_positions)
        max_val = np.max(self.crab_positions)
        fuel_consumptions = [np.sum(value / 2 * (1 + value)) for value in
                             (np.abs(self.crab_positions - np.ones_like(self.crab_positions) * val) for val in
                              range(min_val, max_val + 1))]

        return int(min(fuel_consumptions))


if __name__ == '__main__':
    day = Day07()
    print(day.part_one())
    print(day.part_two())
