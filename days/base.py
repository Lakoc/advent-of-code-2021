class Day:

    def __init__(self, input_file):
        with open(input_file, 'r') as file:
            self.input_content = file.read()
        self.input_lines = self.input_content.split('\n')
        self.input_lines = [line for line in self.input_lines if line != '']
