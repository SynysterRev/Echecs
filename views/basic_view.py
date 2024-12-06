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

    def get_table_menu(self, current_selection):
        """Return a table with all accessible menus, current selected is highlighted in blue"""

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

    def get_menu_options(self, current_selection):
        menu_options = Align.center(self.get_table_menu(current_selection))
        panel_menu_options = Panel(menu_options, title="Menu options",
                                   border_style="blue", padding=(1, 1),
                                   expand=False)
        padded_menu_options = Padding(panel_menu_options, 1)
        return padded_menu_options