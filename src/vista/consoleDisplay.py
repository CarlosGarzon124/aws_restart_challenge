from src.vista.table import ProductTable


class ConsoleDisplay:

    def display_main_menu(self):
        while True:
            pass

    @staticmethod
    def display_product_table(tableName, data):
        table = ProductTable(tableName)
        table.generate_table(data)

