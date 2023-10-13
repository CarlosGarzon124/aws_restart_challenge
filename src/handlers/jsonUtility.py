import json
from rich import print as rprint

class JsonUtility:
    #to do 
    #crear la logica para agregar y leer los datos desde el 
    #archivo json
    @staticmethod
    def load_data(filePath):
        try:
            with open(filePath, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            rprint(f"El archivo {filePath} no fue encontrado en la ruta especificada")
            return None
        
        