from days.base import Day
import re
import sys


def false_fun(_):
    return False


class Day17(Day):

    def __init__(self):
        super().__init__('days/day_17/input.txt')
        regex = re.compile(r'x=(-?\d*)..(-?\d*), y=(-?\d*)..(-?\d*)')
        values = [int(val) for val in regex.search(self.input_lines[0]).groups()]
        self.target_region = range(values[0], values[1]), range(values[2], values[3])
        self.possible_pairs = []
        self.min_val = min(self.target_region[1].start, self.target_region[1].stop)
        self.max_val = max(self.target_region[1].start, self.target_region[1].stop)
        self.max_high = -sys.maxsize.real

    def find_possible_xs(self):
        possible_xs = set()
        for i in range(self.target_region[0].stop + 1):
            n_sum = (i * (i + 1)) / 2
            if self.target_region[0].start <= n_sum <= self.target_region[0].stop:
                j = 1
                n_sum -= j
                while n_sum >= self.target_region[0].start:
                    possible_xs.add((i, i - j))
                    j += 1
                    n_sum -= j
                possible_xs.add((i, -1))
            else:
                n_sum = 0
                for j in range(i, 1, -1):
                    n_sum += j
                    if self.target_region[0].start <= n_sum <= self.target_region[0].stop:
                        possible_xs.add((i, i - j + 1))
        return possible_xs

    def fun1(self, x):
        return x > self.max_val

    def fun2(self, x):
        return x < self.min_val

    def try_to_shoot(self, steps, y_range, cond, x):
        for y in y_range:
            max_high = self.max_high
            n_sum = 0
            for step in range(steps):
                n_sum += y - step
                max_high = max(max_high, n_sum)
            if self.min_val <= n_sum <= self.max_val:
                self.possible_pairs.append((x, y))
                self.max_high = max(self.max_high, max_high)
            elif cond(n_sum) or (y > step and n_sum > self.max_val and not y_range.stop == 0):
                break

    def try_to_drop(self, x):
        for drop_rate in range(0, -self.min_val):
            drop = 0
            drop_rate_curr = drop_rate
            while True:
                drop_rate_curr += 1
                drop += drop_rate_curr
                if self.min_val <= -drop <= self.max_val:
                    self.possible_pairs.append((x, drop_rate))
                    self.max_high = max((drop_rate * (drop_rate + 1)) / 2, self.max_high)
                    break
                elif -drop < self.min_val:
                    break

    def part_one(self):
        return (self.min_val * (self.min_val + 1)) // 2

    def part_two(self):
        possible_xs = self.find_possible_xs()
        for x in possible_xs:
            steps = x[1]
            if steps != -1:
                self.try_to_shoot(steps, range(self.min_val, 0, 1), self.fun1, x[0])
                self.try_to_shoot(steps, range(0, sys.maxsize.real, 1), self.fun2, x[0])
            else:
                self.try_to_shoot(x[0], range(self.min_val, 0, 1), false_fun, x[0])
                self.try_to_drop(x[0])
        possible_pairs = set(self.possible_pairs)
        return len(possible_pairs)


if __name__ == '__main__':
    day = Day17()
    print(day.part_one())
    print(day.part_two())
