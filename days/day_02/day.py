from days.base import Day


class Day02(Day):

    def __init__(self):
        super().__init__('days/day_02/input.txt')

    def part_one(self):
        horizontal = 0
        depth = 0
        for line in self.input_lines:
            line = line.split()
            line[1] = int(line[1])
            if line[0] == 'forward':
                horizontal += line[1]
            elif line[0] == 'up':
                depth -= line[1]
            elif line[0] == 'down':
                depth += line[1]
        return depth * horizontal

    def part_two(self):
        horizontal = 0
        depth = 0
        aim = 0
        for line in self.input_lines:
            line = line.split()
            line[1] = int(line[1])
            if line[0] == 'forward':
                horizontal += line[1]
                depth += aim * line[1]
            elif line[0] == 'up':
                aim -= line[1]
            elif line[0] == 'down':
                aim += line[1]
        return depth * horizontal


if __name__ == '__main__':
    day = Day02()
    print(day.part_one())
    print(day.part_two())
