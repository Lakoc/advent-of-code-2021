from days.base import Day
import numpy as np


class Day01(Day):

    def __init__(self):
        super().__init__('days/day_01/input.txt')

    def part_one(self):
        depths = self.lines_to_np_arr(int)
        increases = np.sum(depths[1:] > depths[:-1])
        return increases

    def part_two(self):
        depths = self.lines_to_np_arr(int)
        windows = np.lib.stride_tricks.sliding_window_view(depths, 3)
        windows_sum = np.sum(windows, axis=1)
        increases = np.sum(windows_sum[1:] > windows_sum[:-1])
        return increases


if __name__ == '__main__':
    day = Day01()
    print(day.part_one())
    print(day.part_two())
