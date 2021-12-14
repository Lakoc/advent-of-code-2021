import math

from days.base import Day
from collections import Counter
from copy import copy


class Day14(Day):

    def __init__(self):
        super().__init__('days/day_14/input.txt')
        empty_line_index = self.input_lines.index('\n')
        self.rules = {rule[0].strip(): rule[0][0] + rule[1].strip() for rule in
                      (line.strip().split('->') for line in self.input_lines[empty_line_index + 1:])}

        self.empty_counts = {rule: 0 for rule in self.rules.keys()}
        self.counts = copy(self.empty_counts)
        self.rules_pairs = {rule[0].strip(): [rule[0][0] + rule[1].strip(), rule[1].strip() + rule[0][1]] for rule in
                            (line.strip().split('->') for line in self.input_lines[empty_line_index + 1:])}

        self.rule_keys = list(self.rules.keys())
        self.start_string = self.input_lines[0].strip()

    def single_step(self, string):
        chunk_size = 2
        result_string = ''
        for i in range(0, len(string)):
            chunk = string[i:i + chunk_size]
            if chunk in self.rule_keys:
                result_string += self.rules[chunk]
            else:
                result_string += chunk

        return result_string

    def part_one(self):
        steps = 10
        string = self.start_string
        for i in range(steps):
            string = self.single_step(string)
        counts = Counter(string)
        max_val = max(counts.values())
        min_val = min(counts.values())
        return max_val - min_val

    def count_classes(self, string):
        chunk_size = 2
        for i in range(0, len(string)):
            chunk = string[i:i + chunk_size]
            if chunk in self.rule_keys:
                self.counts[chunk] += 1

    def apply_rules(self):
        new_counts = copy(self.empty_counts)
        for rule_key, val in self.counts.items():
            pair = self.rules_pairs[rule_key]
            new_counts[pair[0]] += val
            new_counts[pair[1]] += val
        self.counts = new_counts

    def part_two(self):
        steps = 40
        self.count_classes(self.start_string)
        for i in range(steps):
            self.apply_rules()

        all_chars = set(list(''.join(self.counts.keys())))
        char_counts = {char: 0 for char in all_chars}
        for key, val in self.counts.items():
            char_counts[key[0]] += val
            char_counts[key[1]] += val
        max_val = max(char_counts.values())
        min_val = min(char_counts.values())
        return math.floor((max_val - min_val) / 2)


if __name__ == '__main__':
    day = Day14()
    print(day.part_one())
    print(day.part_two())
