from rich.align import Align
from rich.console import Group
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from custom_exception import OutOfRangeValueException
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

    def ask_tournament_number_rounds(self):
        return int(input("Nombre de rounds (4 par défaut) : ") or 4)

    def ask_tournament_description(self):
        return str(input("Description : "))

    def tournament_created(self):
        print("Le tournoi a été créé avec succès")

    def display_all_tournaments(self):
        print("\nTournois enregistrés :")
        print("--------------------------")
        for i in range(len(self.tournaments)):
            print(f"{i + 1}. Tournoi : {self.tournaments[i].name}")
        print(f"{len(self.tournaments) + 1}. Retour")

    def ask_tournament_selection(self):
        choice = int(input("Tapez le numéro correspondant au tournoi : "))
        # +1 cause we want to go back to previous menu
        number_max_to_enter = len(self.tournaments) + 1
        if not (1 <= choice <= number_max_to_enter):
            raise OutOfRangeValueException(number_max_to_enter)
        # Since tuples start at 0
        return choice - 1

    def tournament_selection(self):
        self.display_all_tournaments()
        return self.ask_tournament_selection()

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

    def render_new_tournament(self, current_input):
        table = Table.grid(padding=1)
        table.add_column(justify="center")
        for index, information in enumerate(self.new_tournament_information):
            table.add_row(self.get_input_display(information, current_input, index == self.index_field))

        panel_title = f"[bold magenta]{"Nouveau tournoi"}[/bold magenta]"
        panel = Panel(Align.center(table), title=panel_title)
        self.console.print(panel)

    def get_input_display(self, tournament_information, current_input, is_current_field):
        if is_current_field:
            tournament_information += current_input
            return Text(f"> {tournament_information}")
        else:
            return Text(tournament_information)

    def validate_information(self, final_input, field_index):
        if field_index < len(self.new_tournament_information):
            self.new_tournament_information[field_index] += final_input

    def change_information_input_index(self, new_field_index):
        self.index_field = new_field_index
