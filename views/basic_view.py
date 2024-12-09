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

    def get_tournament_table(self, tournaments_list):
        table = Table(show_lines=True)
        table.add_column("Nom", justify="center", vertical="middle")
        table.add_column("Lieu", justify="center", vertical="middle")
        table.add_column("Date début", justify="center", vertical="middle")
        table.add_column("Date fin", justify="center", vertical="middle")
        table.add_column("ID Joueurs", justify="center", vertical="middle")
        table.add_column("Description", justify="center", max_width=100, vertical="middle")
        table.add_column("Nombre de rounds", justify="center", vertical="middle")

        for tournament in tournaments_list:
            id_list = ""
            for index, player in enumerate(tournament.players):
                if index != 0 and index % 4 == 0:
                    id_list += "\n"
                id_list += f"{player.player_id}, " if index < len(tournament.players) - 1 else f"{player.player_id}"
            row = [tournament.name, tournament.place, tournament.date_start, tournament.date_end,
                   id_list, tournament.description, str(tournament.number_rounds)]
            table.add_row(*row)
        return table

    def get_players_table(self, players_list):
        table = Table(show_lines=True)
        table.add_column("ID", justify="center")
        table.add_column("Prénom", justify="center")
        table.add_column("Nom", justify="center")
        table.add_column("Date de naissance", justify="center")

        for player in players_list:
            row = [player.player_id, player.first_name, player.name, player.birth_date]
            table.add_row(*row)

        return table