from src.vista.table import ProductTable
from src.vista.mainMenu import MainMenu
from collections.abc import Iterable
from rich import print as rprint
import re

class ConsoleDisplay:


    def display_get_product_data(self):
        inputs = {}
        while True:
            name = input("Introduce the new Product Name: ").strip()
            inputs["name"] = name
            price = self.get_price()
            if price is None:
                rprint("Repeat the process please")
                continue
            inputs["price"] = price
            stock = self.get_stock()
            if stock is None:
                rprint("Repeat the process please")
                continue
            inputs["stock"] = stock
            description = input("Introduce the new Product Description: ").strip()
            inputs["description"] = description
            rprint(inputs)
            decision = self.confirm_data_input()
            if decision:
                return inputs
            elif decision is None:
                return None


    def display_get_product_identifier(self):
        while True:
            identifier = self.get_identifier()
            if identifier is None:
                rprint("Repeat the process please")
                continue
            decision = self.confirm_data_input()
            if decision:
                return identifier
            elif decision is None:
                return None


    def display_main_menu(self, function1, function2, function3, function4, function5):
        menu = MainMenu(function1, function2, function3, function4, function5)
        menu.display_menu()


    @staticmethod
    def confirm_data_input():
        isOk = None
        while isOk == None:
            isOk = input("are you sure about this data Y/N: ").upper()
            if isOk == "Y":
                return True
            if isOk == "N":
                cancel = input(
                    "Do you want to cancel this operation (Y/N) if 'No' you will restart process: ").upper()
                if cancel == "Y":
                    return None
                if cancel == "N":
                    return False
                else:
                    rprint("Incorrect answer")
                    isOk = None
            else:
                rprint("Incorrect answer")
                isOk = None


    @staticmethod
    def display_confirmation():
        while True:
            isOk = input("Are you sure about this action (Y/N): ").upper()
            if isOk == "Y":
                return True
            if isOk == "N":
                return False
            rprint("Invalid answer, try again")


    @staticmethod
    def display_product_table(tableName, data):
        table = ProductTable(tableName)
        if isinstance(data, Iterable):
            table.generate_table_many(data)
            return True

        if data is not None:
            table.generate_table_single(data)
            return True

        return False

    @staticmethod
    def get_identifier():
        pattern = r"pd-"
        identifier = input("Introduce the product uId: ").strip()
        if re.search(pattern, identifier):
            return identifier
        else:
            rprint("this is not a valid uId")
            return None

    @staticmethod
    def get_price():
        try:
            price = float(input("Introduce the new Product Price: "))
            return price
        except ValueError:
            print("this is not a valid value for price.")
            return None

    @staticmethod
    def get_stock():
        try:
            stock = int(input("Introduce the new Product Stock: "))
            return stock
        except ValueError:
            print("this is not a valid value for stock.")
            return None


    @staticmethod
    def print_r(message):
        rprint(message)

