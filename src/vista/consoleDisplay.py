from src.vista.table import ProductTable
from src.vista.mainMenu import MainMenu
from collections.abc import Iterable
from rich import print as rprint
import re


#Se encarga de la logica de la vista y funciona gestionando los objetos de ProductTable y MainMenu
#Controla las entradas proporcionadas por el usuario y la logica de validacion de datos y confirmacion por parte del usuario
#las funciones definidas se encargan de desplegar elementos en consola y luego devolver las entradas del usuario
class ConsoleDisplay:

    #se encarga de instanciar el objeto mainMenu y ejecuta la funcion que muestra el menu
    #sirve como punto de entrada en la clase contoller
    #recibe como argumentos las funciones de la clase controller
    def display_main_menu(self, function1, function2, function3, function4, function5):
        menu = MainMenu(function1, function2, function3, function4, function5)
        menu.display_menu()

    #mustra el formulario para recibir los datos del producto por parte del usuario
    #implementa las funciones de validacion de datos
    #retorna un diccionario con los datos suministrados o None en caso de cancelar el proceso
    def display_get_product_data(self):
        inputs = {}
        while True:
            name = input("Introduce the new Product Name: ").strip()
            inputs["name"] = name
            price = self.get_price()
            if price is None:
                rprint("Repeat the process please")
                continue
            inputs["price"] = price
            stock = self.get_stock()
            if stock is None:
                rprint("Repeat the process please")
                continue
            inputs["stock"] = stock
            description = input("Introduce the new Product Description: ").strip()
            inputs["description"] = description
            rprint(inputs)
            decision = self.confirm_data_input()
            if decision:
                return inputs
            elif decision is None:
                return None

    #despliega el formulario para obtener el identificador del producto a buscar
    #retorna una tupla con el valor del identificador en la posicion 0 y el seleccionador en la posicion 1
    #el seleccionador puede estar entre N para nombre o I para uId
    def display_get_product_identifier(self):
        while True:
            selection = self.get_find_type()
            if selection is None:
                rprint("Repeat the process please")
                continue
            if selection == "I":
                identifier = self.get_identifier_uId()
                if identifier is None:
                    rprint("Repeat the process please")
                    continue
                decision = self.confirm_data_input()
                if decision:
                    return (identifier, selection)
                elif decision is None:
                    return None
            identifier = input("Introduce the product Name: ").strip()
            decision = self.confirm_data_input()
            if decision:
                return (identifier, selection)
            elif decision is None:
                return None

    #valida si el usuario esta de acuerdo con los datos que agrego, en caso contrario devuelve False y si cancela la
    #operacion devuelve None
    @staticmethod
    def confirm_data_input():
        isOk = None
        while isOk == None:
            isOk = input("Are you sure about this data Y/N: ").upper()
            if isOk == "Y":
                return True
            if isOk == "N":
                cancel = input(
                    "Do you want to cancel this operation (Y/N) if 'No' you will restart process: ").upper()
                if cancel == "Y":
                    return None
                if cancel == "N":
                    return False
                else:
                    rprint("Incorrect answer")
                    isOk = None
            else:
                rprint("Incorrect answer")
                isOk = None

    #valida si el usuario esta de acuerdo con la accion de eliminar el producto devuelve true o false
    @staticmethod
    def display_confirmation():
        while True:
            isOk = input("Are you sure about this action (Y/N): ").upper()
            if isOk == "Y":
                return True
            if isOk == "N":
                return False
            rprint("Invalid answer, try again")

    #utiliza los metodos de la clase ProductTable para mostrar la tabla segun los datos que se le pasen como parametro
    #   si es una lista usa la funcion para muchos objetos devuelve True ,
    #   si es un producto solo usa la funcion para mostrar un solo objeto devuelve True,
    #   si es None devuelve false
    @staticmethod
    def display_product_table(tableName, data):
        table = ProductTable(tableName)
        if isinstance(data, Iterable):
            table.generate_table_many(data)
            return True

        if data is not None:
            table.generate_table_single(data)
            return True
        return False

    #valida la informacion de el identificador uId usa regex para validar que el uId proporcionado posea el string "pd-" al inicio
    #devuelve el identificador o None
    @staticmethod
    def get_identifier_uId():
        pattern = r"^pd-"
        identifier = input("Introduce the product uId: ").strip()
        if re.search(pattern, identifier):
            return identifier
        else:
            rprint("this is not a valid uId")
            return None

    #valida la informacion del metodo de busqueda
    #devuelve el seleccionador o None
    @staticmethod
    def get_find_type():
        select = input("Introduce a find method, product 'Name' or 'uId' (N/I) : ").strip().upper()
        if select == "N" or select == "I":
            return select
        else:
            rprint("this is not a valid selector")
            return None

    #valida el valor de price proporcionado por el usuario
    #el bloque try/except se encarga de devolver None en caso de que el valor que el usuario proporciono no pueda
    #   ser casteado a tipo float en caso de que si devuelve el valor de price
    @staticmethod
    def get_price():
        try:
            price = float(input("Introduce the new Product Price: "))
            return price
        except ValueError:
            print("this is not a valid value for price.")
            return None

    # valida el valor de stock proporcionado por el usuario
    # el bloque try/except se encarga de devolver None en caso de que el valor que el usuario proporciono no pueda
    #   ser casteado a tipo integer en caso de que si devuelve el valor de stock
    @staticmethod
    def get_stock():
        try:
            stock = int(input("Introduce the new Product Stock: "))
            return stock
        except ValueError:
            print("this is not a valid value for stock.")
            return None

    #permite usar el metodo rprint de rich en el controlador principal
    @staticmethod
    def print_r(message):
        rprint(message)

