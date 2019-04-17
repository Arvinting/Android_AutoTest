import os

import yaml


class ReadYaml(object):
    yaml.warnings({'YAMLLoadWarning': False})

    def __init__(self, filename):
        self.file_path = os.getcwd() + os.sep + 'data' + os.sep + filename + '.yaml'

    def read_data(self):
        with open(self.file_path, 'r') as f:
            yaml_data = yaml.load(f)
            return yaml_data


if __name__ == '__main__':
    rd = ReadYaml("login_data")
    data = rd.read_data()
    print(data)
