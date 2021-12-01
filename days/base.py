import re

import numpy as np


class Day:

    def __init__(self, input_file):
        with open(input_file, 'r') as file:
            self.input_lines = file.readlines()

    def lines_to_np_arr(self, d_type, regex=None):
        data = [re.split(regex, line) for line in self.input_lines] if regex else self.input_lines
        return np.array(data, dtype=d_type)
