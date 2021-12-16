from days.base import Day
import math


class Day16(Day):

    def __init__(self):
        super().__init__('days/day_16/input.txt')
        n_bits = 4 * len(self.input_lines[0])
        self.data = bin(int(self.input_lines[0], 16))[2:].zfill(n_bits)
        self.sum_of_versions = 0

    @staticmethod
    def find_higher_multiplier(x, base=4):
        return int(base * math.ceil(float(x) / base))

    @staticmethod
    def process_operation(inputs, operation):
        if operation == 0:
            return sum(inputs)
        if operation == 1:
            return math.prod(inputs)
        if operation == 2:
            return min(inputs)
        if operation == 3:
            return max(inputs)
        if operation == 5:
            return inputs[0] > inputs[1]
        if operation == 6:
            return inputs[0] < inputs[1]
        if operation == 7:
            return inputs[0] == inputs[1]

    def parse_packets(self, string_to_parse):
        version = int(string_to_parse[:3], 2)
        self.sum_of_versions += version
        type_id = int(string_to_parse[3:6], 2)
        body_start = 6
        if type_id == 4:
            max_groups = len(string_to_parse[body_start:]) // 5
            val_string = ''
            for group in range(max_groups):
                group_start = body_start + (group * 5)
                start_bit = string_to_parse[group_start]
                val_string += string_to_parse[group_start + 1: group_start + 5]
                if start_bit == '0':
                    value = int(val_string, 2)
                    position = group_start + 5
                    offset = position
                    return offset, value
        else:
            length_type_id = string_to_parse[6]
            values = []

            if length_type_id == '0':
                start_pos = 22
                sub_len = int(string_to_parse[7:start_pos], 2)
                while True:
                    offset, value = self.parse_packets(string_to_parse[start_pos:])
                    values.append(value)
                    sub_len -= offset
                    start_pos += offset
                    if sub_len == 0:
                        break
            else:
                start_pos = 18
                num_of_packets = int(string_to_parse[7:start_pos], 2)

                for packet in range(num_of_packets):
                    offset, value = self.parse_packets(string_to_parse[start_pos:])
                    values.append(value)
                    start_pos += offset

            result = self.process_operation(values, type_id)
            return start_pos, result

    def part_one(self):
        self.parse_packets(self.data)
        return self.sum_of_versions

    def part_two(self):
        _, result = self.parse_packets(self.data)
        return result


if __name__ == '__main__':
    day = Day16()
    print(day.part_one())
    print(day.part_two())
