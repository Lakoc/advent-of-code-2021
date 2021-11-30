import os
from string import Template


class Generator:

    def __init__(self):
        self.days_count = 24
        self.days = range(1, self.days_count + 1)
        self.days_dir = 'days'

    def generate_day_folders(self):
        self._generate_root_folder()
        for i in self.days:
            day_dir_path = self._get_day_dir_path(i)
            if not os.path.exists(day_dir_path):
                os.mkdir(day_dir_path)

    def _generate_root_folder(self):
        if not os.path.exists(self.days_dir):
            os.mkdir(self.days_dir)

    def _get_day_dir_path(self, day_num):
        day_dir_path = os.path.join(self.days_dir, F"day_{day_num:02d}")
        return day_dir_path

    def generate_day_source_files(self):
        with open('day.template', 'r') as template_file:
            template_content = template_file.read()
        template = Template(template_content)

        for i in self.days:
            day_dir_path = self._get_day_dir_path(i)
            substitute_dict = {'dayNum': F"{i:02d}"}
            templated_day = template.substitute(substitute_dict)

            source_file_path = os.path.join(day_dir_path, 'day.py')
            if not os.path.exists(source_file_path):
                with open(source_file_path, 'w') as day_source_file:
                    day_source_file.write(templated_day)

    def generate_day_input_files(self):
        for i in self.days:
            day_dir_path = self._get_day_dir_path(i)
            input_path = os.path.join(day_dir_path, 'input.txt')
            if not os.path.exists(input_path):
                with open(input_path, 'w'):
                    pass


if __name__ == "__main__":
    gen = Generator()
    gen.generate_day_folders()
    gen.generate_day_input_files()
    gen.generate_day_source_files()
