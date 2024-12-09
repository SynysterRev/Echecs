from rich.align import Align
from rich.console import Group
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from views.basic_view import BasicView


class PlayerView(BasicView):
    """Menu where user can add new players to the database"""

    def __init__(self, console):
        super().__init__(console)
        self.name = "Joueurs enregistrés"
        self.players_list = []
        self.new_player_informations = ["ID joueur : ", "Nom : ",
                                        "Prénom : ", "Date de naissance (ex : 01/01/2000) : "]
        self.index_field = 0
        self.current_input = ""

    def render(self, current_selection):
        table = self.get_players_table(self.players_list)

        padded_table = Padding(table, (1, 0, 0, 0))

        padded_menu_options = self.get_menu_options(current_selection)

        panel_title = f"[bold magenta]{self.name}[/bold magenta]"
        layout = Group(Align.center(padded_table),
                       Align.center(padded_menu_options))
        panel = Panel(layout, title=panel_title)
        self.console.print(panel)

    def render_new_player(self, error_to_display=""):
        table = Table.grid(padding=1)
        table.add_column(justify="center")
        for index, information in enumerate(self.new_player_informations):
            table.add_row(self.get_input_display(information, self.current_input, index == self.index_field))
            if error_to_display != "" and index == self.index_field:
                table.add_row(Text(str(error_to_display), style="bold red"))

        panel_title = f"[bold magenta]{"Nouveau joueur"}[/bold magenta]"
        panel = Panel(Align.center(table), title=panel_title)
        self.console.print(panel)

    def get_input_display(self, player_information, current_input, is_current_field):
        if is_current_field:
            player_information += current_input
            text = Text("> ", style="blue")
            text.append(player_information, style="default")
            text.append("<", style="blue")
            return text
        else:
            return Text(player_information)

    def validate_information(self, final_input, field_index):
        if field_index < len(self.new_player_informations):
            self.new_player_informations[field_index] += final_input

    def change_information_input_index(self, new_field_index):
        self.index_field = new_field_index

    def clear_player_informations(self):
        self.index_field = 0
        self.current_input = ""
        self.new_player_informations = ["ID joueur : ", "Nom : ",
                                        "Prénom : ", "Date de naissance (ex : 01/01/2000) : "]
