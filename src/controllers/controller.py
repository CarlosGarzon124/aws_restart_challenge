from src.controllers.productController import ProductController
from src.vista.consoleDisplay import ConsoleDisplay

class MainController():

    def __init__(self, JSON_DATA_FILE, DEBUG):
        self.debug = DEBUG
        self.json_path = JSON_DATA_FILE
        self.pController = ProductController(self.json_path)
        self.dController = ConsoleDisplay()


    def show_product_by(self, identify):
        #to do
        #tomar el identificador del usuario
        product = self.pController.get_product_by(identify)
        if product is None:
            self.dController.print_r("!!Product not Found¡¡")
            return
        self.dController.display_product_table("Product Found", product)

    def show_all_products(self):
        products = self.pController.get_all_products()
        self.dController.display_product_table(self.json_path, products)

    def create_product(self):
        inputs = self.dController.display_get_product_data()
        product = self.pController.create_product(inputs)
        self.dController.display_product_table("New product", product)

    def update_product(self, identify):
        self.show_product_by(identify)
        inputs = self.dController.display_get_product_data()
        product = self.pController.update_product_by(identify, inputs)
        self.dController.display_product_table("Updated product", product)


    def run(self):
        #self.create_product()
        self.update_product("pd-f4218632-7684-4a62-9e69-037f7d6a3ae7")
        self.show_all_products()


