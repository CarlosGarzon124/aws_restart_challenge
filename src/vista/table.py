from rich.table import Table
from rich.console import Console


class ProductTable():

    def __init__(self, name):
        self.tableName = name

    
    def generate_table_many(self, products):
        table = Table(title=self.tableName, header_style="bold magenta", show_header=True)
        table.add_column("ID", style="dim")
        table.add_column("NAME")
        table.add_column("PRICE", justify="right", width=12)
        table.add_column("STOCK", style="dim", width=12, justify="right")
        table.add_column("DESCRIPTION", width=20)

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

    def generate_table_single(self, product):
        table = Table(title=self.tableName, header_style="bold magenta", show_header=True)
        table.add_column("ID", style="dim")
        table.add_column("NAME")
        table.add_column("PRICE", justify="right", width=12)
        table.add_column("STOCK", style="dim", width=12, justify="right")
        table.add_column("DESCRIPTION", width=20)

        table.add_row(
            str(product.uId),
            str(product.name),
            str(product.price),
            str(product.stock),
            str(product.description)
        )
        console = Console()
        console.print(table)


