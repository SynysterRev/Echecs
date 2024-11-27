from rich.align import Align
from rich.console import Group
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from helpers.helper import Helper
from views.basic_view import BasicView


class TournamentFlowView(BasicView):
    def __init__(self, console):
        """Menu where user can play a tournament"""
        super().__init__(console)
        self.name = "Tournoi"
        self.tournaments = {}
        self.current_round_index = None
        self.matches = {}
        self.current_match = None

    def render_tournament_selection(self, current_selection):
        table = Table.grid(padding=1)
        table.add_column(justify="center")
        for index, tournament in enumerate(self.tournaments):
            if index == current_selection:
                option_style = "bold white on blue"
            else:
                option_style = "white"

            option_text = Text(tournament.name, style=option_style)
            table.add_row(option_text)

        if len(self.tournaments) == current_selection:
            option_style = "bold white on blue"
        else:
            option_style = "white"

        option_text = Text(Helper.text_menu[Helper.get_main_menu()], style=option_style)
        table.add_row(option_text)

        panel_title = f"[bold magenta]{self.name}[/bold magenta]"
        panel = Panel(Align.center(table), title=panel_title)
        self.console.print(panel)

    def render_start_round(self, current_selection):
        table = Table.grid(padding=1)
        table.add_column(justify="center")
        if current_selection == 0:
            option_style = "bold white on blue"
        else:
            option_style = "white"

        option_text = Text(f"Round {self.current_round_index}", style=option_style)
        table.add_row(option_text)

        if current_selection == 1:
            option_style = "bold white on blue"
        else:
            option_style = "white"

        option_text = Text("Retour", style=option_style)
        table.add_row(option_text)

        panel_title = f"[bold magenta]{self.name}[/bold magenta]"
        panel = Panel(Align.center(table), title=panel_title)
        self.console.print(panel)

    def ask_start_round(self):
        print("\nRound :")
        print("--------------------------")
        print(f"1. Démarrer le round {self.current_round_index}")
        print("2. Retour à la sélection")
        return self.ask_for_user_choice(2)

    def ask_continue_round(self):
        print("\nRound :")
        print("--------------------------")
        print(f"1. Continuer le round {self.current_round_index}")
        print("2. Retour à la sélection")
        return self.ask_for_user_choice(2)

    def matches_selection(self):
        print("\nMatchs :")
        print("--------------------------")
        for i in range(len(self.matches)):
            print(f"{i + 1}. {self.matches[i]}")
        print(f"{len(self.matches)}. Retour")
        return self.ask_for_user_choice(len(self.matches) + 1, "Tapez le numéro correspondant au match :")

    def ask_match_result(self):
        print("\nRésultat :")
        print("--------------------------")
        print(f"1. {self.current_match.players_score[0][0]}")
        print(f"2. {self.current_match.players_score[1][0]}")
        print(f"3. Match nul")
        return self.ask_for_user_choice(3, "Tapez le numéro correspondant au résultat du match :")

