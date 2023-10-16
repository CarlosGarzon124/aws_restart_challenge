import json
from rich import print as rprint

#se encarga de las funcionalidades necesarias para leer los archivos y traer datos o guardarlos

class JsonUtility:

    # usa el bloque try/except para validar si se abre o no el archivo en cuestion, devuelve None en caso de que no exista
    #lee el archivo, y devuelve los datos, devuelve None en caso de que el archivo este vacio
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

    # usa el bloque try/except para validar si se abre o no el archivo en cuestion, devuelve None en caso de que no exista
    #escribe los datos en el archivo
    @staticmethod
    def save_data(filePath, data):
        try:
            with open(filePath, 'w') as file:
                json.dump(data, file)
        except FileNotFoundError:
            rprint(f"The file {filePath} was not found in the specified route")
            return None
        
        