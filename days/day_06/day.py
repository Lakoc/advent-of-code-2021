from days.base import Day
from operator import add
from functools import reduce
import numpy as np


class Day06(Day):

    def __init__(self):
        super().__init__('days/day_06/input.txt')
        self.lanternfishes = list(map(int, self.input_lines[0].split(',')))

        fish_age_classes = 9

        self.population_gen_mat = np.eye(fish_age_classes, k=1, dtype=int)
        self.population_gen_mat[(6, 8), (0, 0)] = 1

    def simulate_lifecycle(self, days):
        lifecycle_matrix = np.linalg.matrix_power(self.population_gen_mat, days)
        fishes_generate_classes = lifecycle_matrix.sum(axis=0)
        population = reduce(add, [fishes_generate_classes[fish] for fish in self.lanternfishes])
        return population

    def part_one(self):
        return self.simulate_lifecycle(80)

    def part_two(self):
        return self.simulate_lifecycle(256)


if __name__ == '__main__':
    day = Day06()
    print(day.part_one())
    print(day.part_two())
