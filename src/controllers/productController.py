from src.handlers.jsonUtility import JsonUtility
from src.model.product import Product

#se encarga de manejar la logica de los productos implementa las funciones de crud maneja la clase Product
#usa el handler JsonUtility para escribir y leer el contenido del archivo
#recibe el path del archivo json como parametro
class ProductController:

    def __init__(self, fileDir):
        self.fileDir = fileDir

    #logica para crear un producto
    #recibe los datos del producto como parametro
    #devuelve el producto para mostrar el resultado al usuario en caso de que el proceso funcione correctamente
    #devuelve None en caso de que los datos no sean validos o sean None
    def create_product(self, data):
        if data is None:
            return None
        if self.validate_product_data(data):
            products = self.load_products_from_file(self.fileDir)
            product = Product(name=data["name"],
                              price=data["price"],
                              stock=data["stock"],
                              description=data["description"])
            products.append(product)
            productDict = self.serialize_json_products(products)
            JsonUtility.save_data(self.fileDir, productDict)
            return product
        return None

    # logica para buscar un producto por un identificador
    # recibe la tupla (identificador, seleccionador) como argumento
    # devuelve None en caso de que no exista el producto
    # puede buscar por uId para devolver un unico producto
    # puede buscar por nombre y devolver una lista de productos en caso de que exista mas de un producto haga match con el identificador
    def get_product_by_id(self, identifier):
        products = list(self.load_products_from_file(self.fileDir))
        if identifier[1] == "I":
            product = None
            for p in products:
                if p.uId == identifier[0]:
                    product = p
            return product
        foundProducts = []
        for p in products:
            if identifier[0].lower() in p.name.lower():
                foundProducts.append(p)
        return foundProducts

    #devuevle todos los productos
    def get_all_products(self):
        return self.load_products_from_file(self.fileDir)

    #logica para actualizar un producto
    #recibe como parametro el identificador uid y el diccionario con los datos
    #devuelve None en caso de que los datos sean None
    #devuelve el producto modificado en caso de que se complete correctamente
    #devuelve None en caso de que los datos no sean correctos
    def update_product_by(self, identifier, newData):
        if newData is None:
            return None
        if self.validate_product_data(newData):
            products = list(self.load_products_from_file(self.fileDir))
            for p in products:
                if p.name == identifier or p.uId == identifier:
                    p.name = newData["name"]
                    p.price = newData["price"]
                    p.stock = newData["stock"]
                    p.description = newData["description"]
                    product = p
                    productDict = self.serialize_json_products(products)
                    JsonUtility.save_data(self.fileDir, productDict)
                    return product
        return None

    #maneja la logica para eliminar un producto
    #recibe el identificador uid como parametro
    #devuelve el producto borrado en caso de que el proceso sea correcto
    #devuelve none en caso de que no se encuentre el producto
    def delete_product_by(self, identifier):
        products = list(self.load_products_from_file(self.fileDir))
        product = None
        for p in products:
            if p.uId == identifier:
                products.remove(p)
                product = p
                break
        productDict = self.serialize_json_products(products)
        JsonUtility.save_data(self.fileDir, productDict)
        return product

    #trae los datos del archivo json y los transforma para crear una lista de productos
    #recibe el path del archivo json
    #devuelve la lista de productos en caso de que tenga
    #devuelve una lista vacia en caso de que no existan productos o no se encuentre el archivo
    @staticmethod
    def load_products_from_file(fileDir):
        products = []
        rawData = JsonUtility.load_data(fileDir)
        if rawData is None:
            return products
        for item in rawData:
            product = Product(
                item["id"],
                item["uId"],
                item["name"], 
                item["price"], 
                item["stock"], 
                item["description"]
            )
            products.append(product)
        return products

    #valida que los datos esten correctos, solo funciona con los datos de create y update
    #devuelve false en caso que no esten correctos
    #devuelve true en caso de que esten correctos
    @staticmethod
    def validate_product_data(data):
        if type(data["name"]) is not str or type(data["price"]) is not float or type(data["stock"]) is not int \
            or type(data["description"]) is not str:
            return False
        return True

    #utiliza el metodo serialize de la clase Product para transformar los datos en formato compatible con json dump
    #recive la lista de productos como parametro
    #devuelve una lista de productos serializados en caso de que la lista argumento tenga datos en caso contrario devuelve una lista vacia
    @staticmethod
    def serialize_json_products(products):
        productList = []
        for p in products:
            productList.append(p.serialize_product())
        return productList
        

        

    