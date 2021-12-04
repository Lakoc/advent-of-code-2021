from days.base import Day
import numpy as np


class Day04(Day):

    def __init__(self):
        super().__init__('days/day_04/input.txt')
        self.numbers_drawn = self.input_lines[0].split(',')
        boards = [[]]
        index = 0

        # Split input to boards
        for line in self.input_lines[2:]:
            if line == '\n':
                index += 1
                boards.append([])
            else:
                boards[index].append(line.strip().split())

        self.boards = np.array(boards, dtype=int)
        self.masks = np.zeros_like(boards, dtype=bool)
        self.row_max = self.masks.shape[2]
        self.col_max = self.masks.shape[1]
        self.winners = []

    @staticmethod
    def calculate_score(number_drawn, winning_board, mask):
        winning_board *= ~mask
        return number_drawn * np.sum(winning_board)

    def save_board_to_cache(self, number_drawn, winner_board):
        self.winners.append((number_drawn, np.copy(self.boards[winner_board]), np.copy(self.masks[winner_board])))
        self.boards[winner_board] = -1
        self.masks[winner_board] = False

    def process_single_round(self, number_drawn):
        indexes = self.boards == number_drawn
        self.masks = np.logical_or(self.masks, indexes)
        cols = np.sum(self.masks, axis=1)
        rows = np.sum(self.masks, axis=2)
        return rows, cols

    def part_one(self):
        for number in self.numbers_drawn:
            rows, cols = self.process_single_round(number)
            if np.any(cols == self.col_max):
                winner = np.where(cols == self.col_max)
                return self.calculate_score(number, self.boards[winner[0]], self.masks[winner[0]])

            if np.any(rows == self.row_max):
                winner = np.where(rows == self.row_max)
                return self.calculate_score(number, self.boards[winner[0]], self.masks[winner[0]])

    def part_two(self):
        # Clean mask
        self.masks = np.logical_and(self.masks, False)

        for number in self.numbers_drawn:
            rows, cols = self.process_single_round(number)
            if np.any(cols == self.col_max):
                winner = np.where(cols == self.col_max)
                self.save_board_to_cache(number, winner[0])
            if np.any(rows == self.row_max):
                winner = np.where(rows == self.row_max)
                self.save_board_to_cache(number, winner[0])

        return self.calculate_score(*self.winners[-1])


if __name__ == '__main__':
    day = Day04()
    print(day.part_one())
    print(day.part_two())
