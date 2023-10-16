from rich.table import Table
from rich.console import Console

#Se encarga de la logica de las tablas en las que se muestran los productos
#recibe como argumento el nombre de la tabla a mostrar
#importa de rich la funcionalidad de las tablas y la consola para imprimir las tablas
class ProductTable:

    def __init__(self, name):
        self.tableName = name

    #se encarga de generar la tabla, con sus columnas definidas para el propocito del inventario
    #agrega los valores mediante la iteracion de los productos recibidos como parametro
    #se invoca cuando los productos estan en una lista
    #recibe como argumento una lista de objetos Product
    def generate_table_many(self, products):
        table = Table(title=self.tableName, header_style="bold magenta", show_header=True)
        table.add_column("ID")
        table.add_column("NAME")
        table.add_column("PRICE", justify="right")
        table.add_column("STOCK", justify="right")
        table.add_column("DESCRIPTION")

        for p in products:
            table.add_row(
                str(p.uId),
                str(p.name),
                str(p.price),
                str(p.stock),
                str(p.description),
            )
            table.add_section()
        console = Console()
        console.print(table)

    #se invoca cuando se recibe un unico producto
    #recibe como argumento un objeto Product
    def generate_table_single(self, product):
        table = Table(title=self.tableName, header_style="bold magenta", show_header=True)
        table.add_column("ID")
        table.add_column("NAME")
        table.add_column("PRICE", justify="right")
        table.add_column("STOCK", justify="right")
        table.add_column("DESCRIPTION")
        table.add_row(
            str(product.uId),
            str(product.name),
            str(product.price),
            str(product.stock),
            str(product.description)
        )
        console = Console()
        console.print(table)


