import json
from rich import print as rprint

class JsonUtility:

    @staticmethod
    def load_data(filePath):
        try:
            with open(filePath, 'r') as file:
                data = json.load(file)
                if len(data) == 0:
                    data = None
                return data
        except FileNotFoundError:
            rprint(f"The file {filePath} was not found in the specified route")
            return None

    @staticmethod
    def save_data(filePath, data):
        try:
            with open(filePath, 'w') as file:
                json.dump(data, file)
        except FileNotFoundError:
            rprint(f"The file {filePath} was not found in the specified route")
            return None
        
        