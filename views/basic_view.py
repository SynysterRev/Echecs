from helpers.helper import Helper
from rich.text import Text
from rich.table import Table
from rich.align import Align
from rich.panel import Panel
from rich.padding import Padding


class BasicView:
    def __init__(self, console):
        self.name = ""
        self.accessible_menus = ()
        self.console = console

    def render(self, current_selection):
        table = self.get_table_menu(current_selection)

        panel_title = f"[bold magenta]{self.name}[/bold magenta]"
        table = Padding(table, (1, 0, 1, 0))
        self.console.print(Panel(Align.center(table), title=panel_title))

    def clear_view(self):
        self.console.clear()
        # self.cls()

    def get_table_menu(self, current_selection):
        table = Table.grid(padding=1)
        table.add_column(justify="center")
        for index, menu in enumerate(self.accessible_menus):
            if index == current_selection:
                option_style = "bold white on blue"
            else:
                option_style = "white"

            option_text = Text(Helper.text_menu[menu], style=option_style)
            table.add_row(option_text)
        return table