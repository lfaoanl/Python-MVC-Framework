import json


class ConfigLoader:

    def __init__(self):
        print("loading config")
        with open("config.json", 'r') as file:
            self.data = json.load(file)
            print(self.data)
            file.close()


_config = ConfigLoader()
config = _config.data

