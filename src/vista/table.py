from rich.table import Table
from rich.console import Console


class ProductTable():

    def __init__(self, name):
        self.table = Table(title=name)
        self.console = Console()
    
    def generate_table(self, products):
        table_ = self.table
        table_.add_column("ID", style="dim", width=12)
        table_.add_column("NAME")
        table_.add_column("PRICE", justify="right")
        table_.add_column("STOCK", style="dim", width=12, justify="right")
        table_.add_column("DESCRIPTION")

        for p in products:
            table_.add_row(
                str(p.id),
                str(p.name),
                str(p.price),
                str(p.stock),
                str(p.description),
            )

    def display_table(self):
        self.console.print(self.table)


