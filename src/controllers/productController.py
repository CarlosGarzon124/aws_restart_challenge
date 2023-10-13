from src.handlers.jsonUtility import JsonUtility
from src.model.product import Product
import uuid


class ProductController():

    def create_product(self, data):
        product = Product(data["name"], 
                          data["price"],
                          data["stock"],
                          data["descritption"])
        
        return product


    def get_product_by(self, identifier):

        product = None
        try:
            identifier = uuid.UUID(identifier)
            product = self.products.get(identifier)

        except ValueError:
            product = None
            for p in self.products.values():
                if p.name == identifier:
                    product = p
        
        return product

    def show_products(self):
        #todo 
        #adicionar el metodo para buscar los productos y devolverlos
        #como una lista de objetos
        pass

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
        

        

    