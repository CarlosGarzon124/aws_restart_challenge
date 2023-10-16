from src.controllers.productController import ProductController
from src.vista.consoleDisplay import ConsoleDisplay

#Controlador principal del proyecto
#orquesta las clases ProductController y ConsoleDisplay
#implementa metodos usando los propios de los controladores
#recibe como parametros los valores del archivo settings
#instancia en el constructor los controladores pController y cControler
class MainController:

    def __init__(self, JSON_DATA_FILE, DEBUG):
        self.debug = DEBUG
        self.json_path = JSON_DATA_FILE
        self.pController = ProductController(self.json_path)
        self.cController = ConsoleDisplay()

    #pide al usuario el identificador y luego mustra el resultado
    def show_product_by(self):
        identifier = self.cController.display_get_product_identifier()
        product = self.pController.get_product_by_id(identifier)
        if self.cController.display_product_table("Selected product", product):
            return
        else:
            ConsoleDisplay.print_r("!!No Products found or process canceled¡¡")

    #muestra todos los productos
    def show_all_products(self):
        products = self.pController.get_all_products()
        self.cController.display_product_table("All products", products)

    #crea el producto nuevo
    def create_product(self):
        inputs = self.cController.display_get_product_data()
        product = self.pController.create_product(inputs)
        self.cController.display_product_table("New product", product)

    #pide al usuario el identificador y luego mustra el resultado
    #actualiza un producto por uid
    def update_product(self):
        identifier = self.cController.display_get_product_identifier()
        product = self.pController.get_product_by_id(identifier)
        if self.cController.display_product_table("Selected product", product):
            inputs = self.cController.display_get_product_data()
            if inputs is None:
                ConsoleDisplay.print_r("Canceled")
                return
            product = self.pController.update_product_by(identifier, inputs)
            self.cController.display_product_table("Product updated correctly", product)
        else:
            ConsoleDisplay.print_r("!!No Products found or process canceled¡¡")

    #pide al usuario el identificador y luego mustra el resultado
    #borra el producto de la lista
    def delete_product(self):
        identifier = self.cController.display_get_product_identifier()
        product = self.pController.get_product_by_id(identifier)
        if self.cController.display_product_table("Selected product" ,product):
            if ConsoleDisplay.display_confirmation():
                delProduct = self.pController.delete_product_by(identifier)
                self.cController.display_product_table("Product Deleted correctly",delProduct)
                return
            ConsoleDisplay.print_r("Canceled")
            return
        else:
            ConsoleDisplay.print_r("!!No Products found or process canceled¡¡")

    #punto de ejecucion de la aplicacion
    #usa la funcion para mostrar el menu de la clase ConsoleDisplay y le pasa como argumentos las funciones propias
    def run(self):
        self.cController.display_main_menu(
            self.show_all_products,
            self.show_product_by,
            self.create_product,
            self.update_product,
            self.delete_product
        )




