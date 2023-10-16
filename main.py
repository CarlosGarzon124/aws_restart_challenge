from src.settings import complete_path, DEBUG
from src.controllers.controller import MainController

#punto de entrada de la aplicacion
#instancia el controlador principal MainController
#importa los argumentos del archivo settings
#corre la aplicacion mediante el methodo run del controlador principal
if __name__ == "__main__":
    controller = MainController(complete_path, DEBUG)
    controller.run()


