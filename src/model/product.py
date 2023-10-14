import uuid


class Product():
    def __init__(self, id=None, uId=None, name=None, price=None, stock=None, description=None):

            # genera id random
            self.id = id if id is not None else str(uuid.uuid4())
            self.uId = uId if uId is not None else "pd-" + str(uuid.uuid4())
            self.name = name
            self.price = price
            self.stock = stock
            self.description = description


    def mod_name(self, name):
        self.name = str(name)

    def mod_name(self, price):
        self.price = float(price)

    def mod_name(self, stock):
        self.stock = int(stock)

    def mod_name(self, description):
        self.description = str(description)


    def serialize_product(self):
        dictProduct = {
            "id":          self.id,
            "uId":         self.uId,
            "name":        self.name,
            "price":       self.price,
            "stock":       self.stock,
            "description": self.description
        }

        return dictProduct


        

    
    