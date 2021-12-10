import numpy as np

from days.base import Day


class Day10(Day):

    def __init__(self):
        super().__init__('days/day_10/input.txt')
        self.score_table1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
        self.score_table2 = {')': 1, ']': 2, '}': 3, '>': 4}
        self.reverse_table_left = {')': '(', ']': '[', '}': '{', '>': '<'}
        self.reverse_table_right = {value: key for key, value in self.reverse_table_left.items()}
        self.stack = []

    def try_to_reduce_stack(self, char):
        reversed_char = self.reverse_table_left[char]
        return (char == ')' and self.stack.pop(-1) == reversed_char) or (
                char == ']' and self.stack.pop(-1) == reversed_char) or (
                       char == '}' and self.stack.pop(-1) == reversed_char) or (
                       char == '>' and self.stack.pop(-1) == reversed_char)

    @staticmethod
    def can_append_to_stack(char):
        return char in ['(', '[', '{', '<']

    def revert_stack_content(self):
        return [self.reverse_table_right[item] for item in reversed(self.stack)]

    def compute_missing_err(self):
        local_err = 0
        stack_reverted = self.revert_stack_content()
        for item in stack_reverted:
            local_err *= 5
            local_err += self.score_table2[item]
        return local_err

    def part_one(self):
        error = 0
        for line in self.input_lines:
            line = line.strip()
            self.stack = []
            for char in line:
                if self.can_append_to_stack(char):
                    self.stack.append(char)
                elif self.try_to_reduce_stack(char):
                    continue
                else:
                    error += self.score_table1[char]
        return error

    def part_two(self):
        errors = []
        for line in self.input_lines:
            line = line.strip()
            self.stack = []
            found_err = False
            for char in line:
                if self.can_append_to_stack(char):
                    self.stack.append(char)
                elif self.try_to_reduce_stack(char):
                    continue
                else:
                    found_err = True
                    break
            if not found_err and len(self.stack) > 0:
                errors.append(self.compute_missing_err())

        return int(np.median(errors))


if __name__ == '__main__':
    day = Day10()
    print(day.part_one())
    print(day.part_two())
