from src.settings import complete_path, DEBUG
from src.controllers.controller import MainController


if __name__ == "__main__":
    controller = MainController(complete_path, DEBUG)
    controller.run()


