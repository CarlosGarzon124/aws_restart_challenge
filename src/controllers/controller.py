from src.controllers.productController import ProductController
from src.vista.consoleDisplay import ConsoleDisplay

class MainController():

    def __init__(self, JSON_DATA_FILE, DEBUG):
        self.debug = DEBUG
        self.json_path = JSON_DATA_FILE


    def display_test_table(self, json_path):
        productList = ProductController.load_products_from_file(json_path)
        ConsoleDisplay.display_product_table("Test Products", productList)

    def run(self):
        self.display_test_table(self.json_path)
