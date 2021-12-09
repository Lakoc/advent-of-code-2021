from days.base import Day
import numpy as np
from scipy.ndimage.measurements import label
import math


class Day09(Day):

    def __init__(self):
        super().__init__('days/day_09/input.txt')
        self.heights = np.array([[i for i in line.strip()] for line in self.input_lines], dtype=int)
        self.heights_padded_max = np.pad(self.heights, (1, 1), 'constant', constant_values=10)

    def part_one(self):
        top_mask = (self.heights_padded_max[1:] - self.heights_padded_max[:-1] < 0)[0:-1, 1:-1]
        bottom_mask = (self.heights_padded_max[:-1] - self.heights_padded_max[1:] < 0)[1:, 1:-1]
        left_mask = (self.heights_padded_max[:, 1:] - self.heights_padded_max[:, :-1] < 0)[1:-1, 0:-1]
        right_mask = (self.heights_padded_max[:, :-1] - self.heights_padded_max[:, 1:] < 0)[1:-1, 1:]
        horizontal_mask = np.logical_and(top_mask, bottom_mask)
        vertical_mask = np.logical_and(left_mask, right_mask)
        mask = np.logical_and(horizontal_mask, vertical_mask)
        numbers = self.heights[mask] + 1
        return np.sum(numbers)

    @staticmethod
    def count_occurrences(arr, labels):
        counts = [np.sum(arr == group) for group in range(1, labels + 1)]
        return counts

    def part_two(self):
        not_nine_mask = self.heights != 9
        labeled_array, max_labels = label(not_nine_mask)
        counts = self.count_occurrences(labeled_array, max_labels)
        three_highest = sorted(counts, reverse=True)[:3]
        return math.prod(three_highest)


if __name__ == '__main__':
    day = Day09()
    print(day.part_one())
    print(day.part_two())
