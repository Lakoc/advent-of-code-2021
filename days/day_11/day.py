from days.base import Day
import numpy as np


class Day11(Day):

    def __init__(self):
        super().__init__('days/day_11/input.txt')
        self.energies = np.array([[i for i in line.strip()] for line in self.input_lines], dtype=int)
        self.moore_offsets = [(1, 1), (1, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]

    def increase_neighbors(self, flash_mask):
        indexes = np.where(flash_mask)
        for index in zip(indexes[0], indexes[1]):
            row = index[0]
            col = index[1]
            for neighbor in self.moore_offsets:
                dr, dc = neighbor
                if 0 <= row + dr < 10 and 0 <= col + dc < 10:
                    self.energies[row + dr][col + dc] += 1

    def simulate_single_step(self):
        self.energies += 1
        flash_mask = self.energies > 9
        flashes_processed = np.zeros_like(flash_mask)
        new_flashes = np.sum(flash_mask)
        while new_flashes > 0:
            self.increase_neighbors(flash_mask)
            flashes_processed = np.logical_or(flashes_processed, flash_mask)
            flash_mask = np.logical_and(self.energies > 9, ~flashes_processed)
            new_flashes = np.sum(flash_mask)

        overall_processed = np.sum(self.energies > 9)
        self.energies[self.energies > 9] = 0
        return np.sum(overall_processed)

    def part_one(self):
        steps = 100
        flashes = 0
        for step in range(steps):
            flashes += self.simulate_single_step()
        return flashes

    def part_two(self):
        flashes = 0
        self.energies = np.array([[i for i in line.strip()] for line in self.input_lines], dtype=int)
        max_brightness = self.energies.shape
        step = 0
        while flashes != max_brightness[0] * max_brightness[1]:
            step += 1
            flashes = self.simulate_single_step()
        return step


if __name__ == '__main__':
    day = Day11()
    print(day.part_one())
    print(day.part_two())
