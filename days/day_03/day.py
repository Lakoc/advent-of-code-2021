from days.base import Day


class Day03(Day):

    def __init__(self):
        super().__init__('days/day_03/input.txt')
        self.chars = [list(line.strip()) for line in self.input_lines]
        self.code_len = len(self.input_lines[0].strip())
        self.lines_len = len(self.input_lines)
        self.thr = self.lines_len / 2
        self.reduced_chars = self.chars

    @staticmethod
    def convert_from_binary_string(string):
        return int(string, 2)

    def count_ones(self):
        one_counts = [0 for _ in range(self.code_len)]
        for line in self.chars:
            for index, char in enumerate(line):
                one_counts[index] += int(char)
        return one_counts

    def part_one(self):
        one_counts = self.count_ones()
        gamma_vec = [str(int(item >= self.thr)) for item in one_counts]
        epsilon_vec = [str(1 - int(char)) for char in gamma_vec]
        gamma = self.convert_from_binary_string(''.join(gamma_vec))
        epsilon = self.convert_from_binary_string(''.join(epsilon_vec))
        return gamma * epsilon

    def filter(self, index, char):
        arr = []
        for line in self.reduced_chars:
            if line[index] == char:
                arr.append(line)
        self.reduced_chars = arr

    def reduce_vec(self, index, num_to_find):
        arr_len = len(self.reduced_chars)
        zero_counts = 0
        for line in self.reduced_chars:
            zero_counts += int(line[index])
        condition_met = int(zero_counts >= arr_len / 2)
        bin_val_to_filter = str(1 - condition_met if num_to_find == 1 else condition_met)
        self.filter(index, bin_val_to_filter)

    def part_two(self):
        index = 0
        while len(self.reduced_chars) > 1:
            self.reduce_vec(index, 0)
            index += 1
        oxygen = self.convert_from_binary_string(''.join(self.reduced_chars[0]))
        index = 0
        self.reduced_chars = self.chars
        while len(self.reduced_chars) > 1:
            self.reduce_vec(index, 1)
            index += 1
        co2 = self.convert_from_binary_string(''.join(self.reduced_chars[0]))

        return oxygen * co2


if __name__ == '__main__':
    day = Day03()
    print(day.part_one())
    print(day.part_two())
