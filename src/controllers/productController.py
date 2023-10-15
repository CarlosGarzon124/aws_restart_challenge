from src.handlers.jsonUtility import JsonUtility
from src.model.product import Product


class ProductController():

    def __init__(self, fileDir):
        self.fileDir = fileDir

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


    def get_product_by(self, identifier):

        products = list(self.load_products_from_file(self.fileDir))
        product = None
        for p in products:
            if p.name == identifier or p.uId == identifier:
                product = p
        
        return product

    def get_all_products(self):
        return self.load_products_from_file(self.fileDir)


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

    def validate_product_data(self, data):
        if type(data["name"]) is not str or type(data["price"]) is not float or type(data["stock"]) is not int \
            or type(data["description"]) is not str:
            return False

        return True

    @staticmethod
    def serialize_json_products(products):
        productList = []
        for p in products:
            productList.append(p.serialize_product())


        return productList
        

        

    