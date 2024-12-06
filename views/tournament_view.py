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
        self.tournaments = []
        self.new_tournament_information = ["Nom : ", "Lieu : ", "Date début : ",
                                           "Description : ", "Nombre de rounds : "]
        self.index_field = 0
        self.current_input = ""
        self.new_player_informations = ["ID joueur : ", "Nom : ",
                                        "Prénom : ", "Date de naissance (ex : 01/01/2000) : "]
        self.players_list = []

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
                if index != 0 and index % 4 == 0:
                    id_list += "\n"
                id_list += f"{player.player_id}, " if index < len(tournament.players) - 1 else f"{player.player_id}"
            row = [tournament.name, tournament.place, tournament.date_start, tournament.date_end,
                   id_list, tournament.description, str(tournament.number_rounds)]
            table.add_row(*row)

        padded_table = Padding(table, (1, 0, 0, 0))

        padded_menu_options = self.get_menu_options(current_selection)

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

    def render_players_to_add(self, current_selection, error_to_display=""):
        table = Table(show_lines=True)
        table.add_column("ID", justify="center")
        table.add_column("Prénom", justify="center")
        table.add_column("Nom", justify="center")
        table.add_column("Date de naissance", justify="center")

        for player in self.players_list:
            row = [player.player_id, player.first_name, player.name, player.birth_date]
            table.add_row(*row)

        padded_table = Padding(table, (1, 0, 0, 0))

        padded_menu_options = self.get_menu_options(current_selection)

        panel_title = f"[bold magenta]{self.name}[/bold magenta]"
        error = Text(str(error_to_display), style="bold red") if error_to_display != "" else ""
        layout = Group(Align.center(padded_table),
                       Align.center(error),
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

    def validate_player_information(self, final_input, field_index):
        if field_index < len(self.new_player_informations):
            self.new_player_informations[field_index] += final_input

    def change_information_player_input_index(self, new_field_index):
        self.index_field = new_field_index

    def clear_player_informations(self):
        self.index_field = 0
        self.current_input = ""
        self.new_player_informations = ["ID joueur : ", "Nom : ",
                                        "Prénom : ", "Date de naissance (ex : 01/01/2000) : "]

    def render_selection_player(self, error_to_display=""):
        search = Table.grid(padding=1)
        search.add_column(justify="center")
        search.add_row(self.get_input_display("ID du joueur (entrée pour valider): ",
                                              self.current_input, True))
        if error_to_display != "":
            search.add_row(Text(str(error_to_display), style="bold red"))

        panel_title = "[bold magenta]Sélection de joueur[/bold magenta]"
        search = Padding(search, (1, 0, 1, 0))
        panel = Panel(Align.center(search), title=panel_title)
        self.console.print(panel)

    def render_validate_player(self, player_name, current_selection):
        search = Table.grid(padding=1)
        search.add_column(justify="center")
        search.add_row(Text(f"ID du joueur : {self.current_input}"))
        search.add_row(Text(f"Joueur trouvé : {player_name}"))

        padded_table = Padding(search, (1, 0, 0, 0))

        padded_menu_options = self.get_menu_options(current_selection)

        panel_title = f"[bold magenta]{self.name}[/bold magenta]"
        layout = Group(Align.center(padded_table),
                       Align.center(padded_menu_options))
        panel = Panel(layout, title=panel_title)
        self.console.print(panel)
