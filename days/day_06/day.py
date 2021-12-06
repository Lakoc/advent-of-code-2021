from days.base import Day
from operator import add
from functools import reduce


class Day06(Day):

    def __init__(self):
        super().__init__('days/day_06/input.txt')
        self.days = 0
        self.lanternfishes = self.input_lines[0].split(',')
        self.initialize_population()

    def initialize_population(self):
        self.fishes_count = {i: 0 for i in range(9)}
        for lanternfish in self.lanternfishes:
            self.fishes_count[int(lanternfish)] += 1

    def simulate_life_cycle(self, days):
        days_pop = [reduce(add, self.fishes_count.values())]
        for _ in range(days):
            new_fishes_count = {i: 0 for i in range(9)}
            for fish_age, count in self.fishes_count.items():
                if fish_age == 0:
                    new_fishes_count[6] += count
                    new_fishes_count[8] += count
                    new_fishes_count[0] = 0
                else:
                    new_fishes_count[fish_age - 1] += count

            self.fishes_count = new_fishes_count
            population = reduce(add, self.fishes_count.values())
            days_pop.append(population)

        return days_pop

    def part_one(self):
        self.days = 80
        population_per_day = self.simulate_life_cycle(self.days)

        return population_per_day[-1]

    def part_two(self):
        self.days = 256
        self.initialize_population()
        population_per_day = self.simulate_life_cycle(self.days)
        return population_per_day[-1]


if __name__ == '__main__':
    day = Day06()
    print(day.part_one())
    print(day.part_two())
