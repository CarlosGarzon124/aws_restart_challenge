from rich import print as rprint

class MainMenu:
    def __init__(self, function1, function2, function3, function4, function5):

        self.functions = {
            "1": function1,
            "2": function2,
            "3": function3,
            "4": function4,
            "5": function5
        }

        self.options = {
            "1": "Show all products",
            "2": "Show a product by",
            "3": "Create product",
            "4": "Update product",
            "5": "Delete product",
            "q": "Exit"
        }

    def display_menu(self):
        while True:
            rprint("====== Stock Menu ======")
            for key, value in self.options.items():
                rprint(f"{key}. {value}")

            sel = input("Chose an option: ").strip().lower()

            if sel == "q":
                rprint("Exiting program")
                break
            elif sel in self.options:
                aFunction = self.functions[sel]
                aFunction()
            else:
                rprint("Option is not valid, select a real option")



