from days.base import Day


class Day08(Day):

    def __init__(self):
        super().__init__('days/day_08/input.txt')
        self.sizes = {2: 1, 3: 7, 4: 4, 7: 8}
        self.sizes_all = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}
        self.size_keys = self.sizes.keys()
        self.display_positions = ['top', 'top_left', 'top_right', 'middle', 'bottom_left', 'bottom_right', 'bottom']

    def part_one(self):
        counter = 0
        for line in self.input_lines:
            output = line.split('|')[1].split()
            for output_digit in output:
                signal_size = len(output_digit)
                if signal_size in self.size_keys:
                    counter += 1
        return counter

    @staticmethod
    def strings_difference(string1, string2):
        result = ''
        for char in string1:
            if char not in string2:
                result += char
        return result

    @staticmethod
    def strings_intersection(string1, string2):
        result = ''
        for char in string1:
            if char in string2:
                result += char
        return result

    @staticmethod
    def divide_strings_into_categories(strings):
        categories = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
        for string in strings:
            categories[len(string)].append(string)
        return categories

    @staticmethod
    def apply_operation_to_multiple_strings(strings, operation):
        result = strings[0]
        for string in strings[1:]:
            result = operation(result, string)
        return result

    @staticmethod
    def find_six(strings, bottom_left, middle):
        for string in strings:
            if bottom_left in string and middle in string:
                return string

    def process_single_line_signals(self, signals):
        display = {position: None for position in self.display_positions}
        categories = self.divide_strings_into_categories(signals)

        display['top'] = self.strings_difference(categories[3][0], categories[2][0])

        right_strings = categories[2][0]

        center_strings = self.apply_operation_to_multiple_strings(categories[5],
                                                                  self.strings_intersection)
        display['middle'] = self.apply_operation_to_multiple_strings([center_strings, *categories[4]],
                                                                     self.strings_intersection)
        display['bottom'] = self.apply_operation_to_multiple_strings(
            [center_strings, display['top'], display['middle']],
            self.strings_difference)
        left_strings = self.apply_operation_to_multiple_strings([categories[7][0], center_strings, right_strings],
                                                                self.strings_difference)
        display['top_left'] = self.strings_intersection(left_strings, categories[4][0])
        display['bottom_left'] = self.strings_difference(left_strings, display['top_left'])
        display['top_right'] = self.strings_difference(categories[7][0],
                                                       self.find_six(categories[6], display['bottom_left'],
                                                                     display['middle']))
        display['bottom_right'] = self.strings_difference(right_strings, display['top_right'])
        return display

    @staticmethod
    def decode_number_by_signals(signals):
        if len(signals) == 7:
            return 8
        elif len(signals) == 6:
            if 'middle' not in signals:
                return 0
            elif 'top_right' not in signals:
                return 6
            else:
                return 9
        elif len(signals) == 5:
            if 'bottom_left' in signals:
                return 2
            elif 'top_left' in signals:
                return 5
            else:
                return 3
        elif len(signals) == 4:
            return 4
        elif len(signals) == 3:
            return 7
        elif len(signals) == 2:
            return 1
        else:
            raise ValueError

    def decode_numbers(self, strings, display):
        key_list = list(display.keys())
        val_list = list(display.values())

        value = ''
        for string in strings:
            string_diodes = []
            for char in string:
                string_diodes.append(key_list[val_list.index(char)])
            number = self.decode_number_by_signals(string_diodes)
            value += f'{number}'
        return int(value)

    def part_two(self):
        sum_of_outputs = 0
        for line in self.input_lines:
            signals, output = line.split('|')
            display = self.process_single_line_signals(signals.split())
            sum_of_outputs += self.decode_numbers(output.split(), display)
        return sum_of_outputs


if __name__ == '__main__':
    day = Day08()
    print(day.part_one())
    print(day.part_two())
