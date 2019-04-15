import os

import yaml


class ReadYaml:

    yaml.warnings({'YAMLLoadWarning': False})

    def __init__(self, filename):

        self.file_path = os.getcwd() + os.sep + 'data' + os.sep + filename + '.yaml'

    def read_data(self):

        with open(self.file_path, 'r') as f:
            data = yaml.load(f)
            return data

if __name__ == '__main__':

    data = ReadYaml('login_data').read_data()
    print(data)
