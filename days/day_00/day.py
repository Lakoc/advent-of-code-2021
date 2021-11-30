from days.base import Day


class Day00(Day):
    """
    Day 0 is used only for template generation testing.
    """

    def __init__(self):
        super().__init__('days/day_00/input.txt')

    def part_one(self):
        pass

    def part_two(self):
        pass


if __name__ == '__main__':
    day = Day00()
    print(day.part_one())
    print(day.part_two())
