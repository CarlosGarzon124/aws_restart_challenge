from src.controllers.productController import ProductController
from src.vista.consoleDisplay import ConsoleDisplay

class MainController:

    def __init__(self, JSON_DATA_FILE, DEBUG):
        self.debug = DEBUG
        self.json_path = JSON_DATA_FILE
        self.pController = ProductController(self.json_path)
        self.dController = ConsoleDisplay()

    def show_product_by(self):
        identifier = self.dController.display_get_product_identifier()
        product = self.pController.get_product_by_id(identifier)
        if self.dController.display_product_table("Selected product", product):
            return
        else:
            ConsoleDisplay.print_r("!!No Products found or process canceled¡¡")

    def show_all_products(self):
        products = self.pController.get_all_products()
        self.dController.display_product_table("All products", products)

    def create_product(self):
        inputs = self.dController.display_get_product_data()
        product = self.pController.create_product(inputs)
        self.dController.display_product_table("New product", product)

    def update_product(self):
        identifier = self.dController.display_get_product_identifier()
        product = self.pController.get_product_by_id(identifier)
        if self.dController.display_product_table("Selected product", product):
            inputs = self.dController.display_get_product_data()
            if inputs is None:
                ConsoleDisplay.print_r("Canceled")
                return
            product = self.pController.update_product_by(identifier, inputs)
            self.dController.display_product_table("Product updated correctly", product)
        else:
            ConsoleDisplay.print_r("!!No Products found or process canceled¡¡")

    def delete_product(self):
        identifier = self.dController.display_get_product_identifier()
        product = self.pController.get_product_by(identifier)
        if self.dController.display_product_table("Selected product" ,product):
            if ConsoleDisplay.display_confirmation():
                delProduct = self.pController.delete_product_by(identifier)
                self.dController.display_product_table("Product Deleted correctly",delProduct)
                return
            ConsoleDisplay.print_r("Canceled")
            return
        else:
            ConsoleDisplay.print_r("!!No Products found or process canceled¡¡")

    def run(self):
        self.dController.display_main_menu(
            self.show_all_products,
            self.show_product_by,
            self.create_product,
            self.update_product,
            self.delete_product
        )




