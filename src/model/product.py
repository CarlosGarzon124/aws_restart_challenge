import uuid

#mapea los datos en al chivo json
#genera los ids y uid de forma aleatoria cuando se crea por primera vez el objeto, usa la lib uuid para este proceso
#si el valor de id y uid son None que implica que el producto esta siendo leido de la base de datos utiliza estos valores
#   en vez de generarlos nuevos
#se encarga de serializar el objeto en formato json para luego poderlo subir al archivo de bd
class Product():
    def __init__(self, id=None, uId=None, name=None, price=None, stock=None, description=None):

            # genera id random
            self.id = id if id is not None else str(uuid.uuid4())
            self.uId = uId if uId is not None else "pd-" + str(uuid.uuid4())
            self.name = name
            self.price = price
            self.stock = stock
            self.description = description

    #serializa el objeto en diccionario y devuelve el diccionario
    #no recibe parametros pero trabaja con los argumentos del objeto en cuestion
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


        

    
    