import json
import os


class JsonReader:
    dir = os.path.dirname(__file__)
    part = None
    full_json = None

    def __init__(self):
        part = self.part
        full_json = self.full_json

    def json_reader(self, path):
        # filename = os.path.join(self.dir, path)
        f = open(path, 'r')
        self.full_json = json.loads(f.read())
        return self.full_json

    def json_reader_get_part(self, path, number):
        self.json_reader(path)
        part = self.full_json[number - 1]
        return part

