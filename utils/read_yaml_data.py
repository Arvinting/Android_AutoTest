import os

import yaml

"""
读取yaml中的数据，返回字典格式
"""


class ReadYaml(object):
    yaml.warnings({'YAMLLoadWarning': False})

    def __init__(self, filename):
        self.file_path = os.getcwd() + os.sep + 'data' + os.sep + filename + '.yaml'

    def read_data(self):
        with open(self.file_path, 'r') as f:
            yaml_data = yaml.load(f)
            return yaml_data

