from src.vista.table import ProductTable
from collections.abc import Iterable
from rich import print as rprint

class ConsoleDisplay:

    def display_main_menu(self):
        while True:
            pass

    def display_get_product_data(self):
        inputs = {}
        ok = False
        cancel = None
        while ok is False:
            name = input("Introduce the new Product Name: ")
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
            description = input("Introduce the new Product Description: ")
            inputs["description"] = description
            rprint(inputs)
            isOk = input("are you sure about this data Y/N: ")
            if isOk == "Y":
                return inputs
            if isOk == "N":
                cancel = input("Do you want to cancel this operation (Y/N) if 'No' you will continue to modify the product fields: ")
            if cancel == "Y":
                return None


    def display_product_table(self, tableName, data):
        table = ProductTable(tableName)
        if isinstance(data, Iterable):
            table.generate_table_many(data)
            return

        if data is not None:
            table.generate_table_single(data)
            return

        rprint("!!No data added¡¡")


    def get_price(self):
        try:
            price = float(input("Introduce the new Product Price: "))
            return price
        except ValueError:
            print("this is not a valid value for price.")
            return None

    def get_stock(self):
        try:
            stock = int(input("Introduce the new Product Stock: "))
            return stock
        except ValueError:
            print("this is not a valid value for stock.")
            return None



    @staticmethod
    def print_r(message):
        rprint(message)

