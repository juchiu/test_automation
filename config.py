import os
import yaml

FILENAME = os.environ.get("CONFIG_FILE", "config.yml")
_data = {}
with open(FILENAME) as f:
    _data = yaml.load(f)

def __getattr__(name):
    return _data.get(name)

class Config(object):
    _data = {}
    def __init__(self, filename=FILENAME):
        with open(filename) as f:
            self._data = yaml.load(f)

    def __getattr__(self, name):
        return self._data.get(name)
