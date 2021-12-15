from days.base import Day
import numpy as np
import sys


class Node:
    def __init__(self, position, cost):
        self.position = position
        self.cost = cost

    @staticmethod
    def is_valid_position(position, max_pos):
        return (position >= 0).all() and (position <= max_pos).all()

    def equals(self, node):
        return node.position[0] == self.position[0] and node.position[1] == self.position[1]


class Day15(Day):

    def __init__(self):
        super().__init__('days/day_15/input.txt')
        self.risk = np.array([[i for i in line.strip()] for line in self.input_lines], dtype=int)
        self.buffer = [Node(np.array([0, 0]), 0)]
        self.closed = []
        self.offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.max_pos = np.array((self.risk.shape[0] - 1, self.risk.shape[0] - 1))

    def find_min_node(self):
        cost = sys.maxsize
        min_node = None
        for node in self.buffer:
            val = node.cost
            if val < cost:
                cost = val
                min_node = node
        return min_node

    def update_buffer(self, new_node):
        for node in self.buffer:
            if node.equals(new_node):
                min_cost = min(node.cost, new_node.cost)
                node.cost = min_cost
                return
        self.buffer.append(new_node)

    def generate_siblings(self, node):
        position = node.position
        cost = node.cost
        siblings = [Node(pos, cost + self.risk[pos[0], pos[1]]) for pos in
                    (position + offset for offset in self.offsets) if
                    Node.is_valid_position(pos, self.max_pos) and (pos[0], pos[1]) not in self.closed]
        for sibling in siblings:
            self.update_buffer(sibling)

    def part_one(self):
        while True:
            min_node = self.find_min_node()
            pos = min_node.position
            if pos[0] == self.risk.shape[0] - 1 and pos[1] == self.risk.shape[1] - 1:
                break
            self.generate_siblings(min_node)
            self.buffer.remove(min_node)
            self.closed.append((min_node.position[0],min_node.position[1]))
        return min_node.cost

    def part_two(self):
        arr = np.tile(self.risk,(5,5))
        x = np.tile(np.arange(0, arr.shape[0]) // self.risk.shape[0], ( arr.shape[1], 1))
        y = np.arange(0, arr.shape[1]) // self.risk.shape[1]
        offsets = x+y[:, np.newaxis]
        arr += offsets
        arr = arr % 9
        self.risk = arr
        self.buffer = [Node(np.array([0, 0]), 0)]
        self.closed = []
        self.max_pos = np.array((self.risk.shape[0] - 1, self.risk.shape[0] - 1))
        return day.part_one()


if __name__ == '__main__':
    day = Day15()
    print(day.part_one())
    print(day.part_two())
