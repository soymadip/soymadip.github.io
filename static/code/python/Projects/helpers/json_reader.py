import json
import os
import sys


class jsonReader:
    def __init__(self, config_file) -> None:
        self.config_file = config_file

        # Create config file if doens't exist
        if not os.path.exists(self.config_file):
            try:
                with open(self.config_file, "w") as fconfig:
                    json.dump({}, fconfig)
            # except Json
            except Exception as e:
                print(f"Can't create config file: {e}")
                sys.exit(1)

    # Read config
    def load(self):
        if os.path.getsize(self.config_file) == 0:
            self.write({})

        try:
            with open(self.config_file, "r") as fconfig:
                config = json.load(fconfig)
        except Exception as e:
            print(f"Can't load config: {e}")
            sys.exit(1)

        return config

    def write(self, data):
        try:
            with open(self.config_file, "w") as fconfig:
                json.dump(data, fconfig, indent=2)
        except Exception as e:
            print(f"Error: {e}")
