from rich.align import Align
from rich.console import Group
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from views.basic_view import BasicView


class TournamentView(BasicView):
    """Menu where user can manage tournaments"""
    def __init__(self, console):
        super().__init__(console)
        self.name = "Gestion de tournoi"
        self.tournaments = {}
        self.new_tournament_information = ["Nom : ", "Lieu : ", "Date début : ",
                                           "Description : ", "Nombre de rounds : "]
        self.index_field = 0
        self.current_input = ""

    def render(self, current_selection):
        table = Table(show_lines=True)
        table.add_column("Nom", justify="center")
        table.add_column("Lieu", justify="center")
        table.add_column("Date début", justify="center")
        table.add_column("Date fin", justify="center")
        table.add_column("ID Joueurs", justify="center")
        table.add_column("Description", justify="center")
        table.add_column("Nombre de rounds", justify="center")

        for tournament in self.tournaments:
            id_list = ""
            for index, player in enumerate(tournament.players):
                if index != 0 and index % 4 == 0 :
                    id_list += "\n"
                id_list += f"{player.player_id}, " if index < len(tournament.players) - 1 else f"{player.player_id}"
            row = [tournament.name, tournament.place, tournament.date_start, tournament.date_end,
                   id_list, tournament.description, str(tournament.number_rounds)]
            table.add_row(*row)

        padded_table = Padding(table, (1, 0, 0, 0))

        menu_options = Align.center(self.get_table_menu(current_selection))
        panel_menu_options = Panel(menu_options, title="Menu options",
                                   border_style="blue", padding=(1, 0),
                                   expand=False)
        padded_menu_options = Padding(panel_menu_options, 1)

        panel_title = f"[bold magenta]{self.name}[/bold magenta]"
        layout = Group(Align.center(padded_table),
                       Align.center(padded_menu_options))
        panel = Panel(layout, title=panel_title)
        self.console.print(panel)

    def render_new_tournament(self, error_to_display=""):
        table = Table.grid(padding=1)
        table.add_column(justify="center")
        for index, information in enumerate(self.new_tournament_information):
            table.add_row(self.get_input_display(information, self.current_input, index == self.index_field))
            if error_to_display != "" and index == self.index_field:
                table.add_row(Text(str(error_to_display), style="bold red"))

        panel_title = f"[bold magenta]{"Nouveau tournoi"}[/bold magenta]"
        panel = Panel(Align.center(table), title=panel_title)
        self.console.print(panel)

    def get_input_display(self, tournament_information, current_input, is_current_field):
        if is_current_field:
            tournament_information += current_input
            text = Text("> ", style="blue")
            text.append(tournament_information)
            text.append("<", style="blue")
            return text
        else:
            return Text(tournament_information)

    def validate_information(self, final_input, field_index):
        if field_index < len(self.new_tournament_information):
            self.new_tournament_information[field_index] += final_input

    def change_information_input_index(self, new_field_index):
        self.index_field = new_field_index

    def clear_tournament_informations(self):
        self.index_field = 0
        self.current_input = ""
        self.new_tournament_information = ["Nom : ", "Lieu : ", "Date début : ",
                                           "Description : ", "Nombre de rounds : "]
