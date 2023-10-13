import uuid

class Product():
    def __init__(self, id=None, uId=None,  name=None, price=None, stock=None, description=None):
        #Genera un producto para mostrar o leer
        if name is not None and price is not None and stock is not None and description is not None and id is not None and uId is not None:
            self.id = id
            self.uId = uId
            self.name = name
            self.price = price
            self.stock = stock
            self.description = description
        #Genera un Producto para la creacion
        elif id is None and uId is None and name is not None and price is not None and stock is not None and description is not None:
            # genera id random
            self.id = uuid.uuid4
            self.uId = "pd-" + uuid.uuid4()
            self.name = str(name)
            self.price = float(price)
            self.stock = int(stock)
            self.description = str(description)



    def mod_name(self, name):
        self.name = str(name)

    def mod_name(self, price):
        self.price = float(price)

    def mod_name(self, stock):
        self.stock = int(stock)

    def mod_name(self, descrition):
        self.description = str(descrition)


        

    
    