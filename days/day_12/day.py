from days.base import Day


class Day12(Day):

    def __init__(self):
        super().__init__('days/day_12/input.txt')
        self.graph = {}
        for line in self.input_lines:
            start, end = line.strip().split('-')
            if start in self.graph.keys():
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]
            if end in self.graph.keys():
                self.graph[end].append(start)
            else:
                self.graph[end] = [start]

    @staticmethod
    def is_small_area(node):
        return node.casefold() == node

    def find_all_paths_small_max1(self, start, end, path=None):
        if path is None:
            path = []

        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.graph.get(start, []):
            if not (self.is_small_area(node) and node in path):
                new_paths = self.find_all_paths_small_max1(node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    def find_all_correct_paths(self, start, end, path=None):
        if path is None:
            path = []

        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.graph.get(start, []):
            if not (self.is_small_area(node) and node in path):
                new_paths = self.find_all_correct_paths(node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
            elif self.is_small_area(node) and path.count(node) == 1 and node not in ['start', 'end']:
                new_paths = self.find_all_paths_small_max1(node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    def part_one(self):
        paths = self.find_all_paths_small_max1('start', 'end')
        return len(paths)

    def part_two(self):
        paths = self.find_all_correct_paths('start', 'end')
        return len(paths)


if __name__ == '__main__':
    day = Day12()
    print(day.part_one())
    print(day.part_two())
