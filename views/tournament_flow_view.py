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
        self.tournaments = []
        self.current_round_index = None
        self.matches = []
        self.matches_not_played = []
        self.current_match = None
        self.tournament_finals_scores = {}

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
        table = Padding(table, (1, 0, 1, 0))
        panel = Panel(Align.center(table), title=panel_title)
        self.console.print(panel)

    def render_start_round(self, current_selection):
        table = Table.grid(padding=1)
        table.add_column(justify="center")
        if current_selection == 0:
            option_style = "bold white on blue"
        else:
            option_style = "white"

        option_text = Text(f"Commencer le round", style=option_style)
        table.add_row(Align.center(option_text))

        if current_selection == 1:
            option_style = "bold white on blue"
        else:
            option_style = "white"

        option_text = Text("Retour", style=option_style)
        table.add_row(Align.center(option_text))

        panel_title = f"[bold magenta]Round {self.current_round_index}[/bold magenta]"
        table = Padding(table, (1, 0, 1, 0))
        panel = Panel(Align.center(table), title=panel_title)
        self.console.print(panel)

    def render_select_match(self, current_selection):
        table = Table.grid(padding=1)
        table.add_column(justify="center")
        for index, match in enumerate(self.matches_not_played):
            if not match.is_finished:
                if index == current_selection:
                    option_style = "bold white on blue"
                else:
                    option_style = "white"

                option_text = Text(str(match), style=option_style)
                table.add_row(option_text)

        if current_selection == len(self.matches_not_played):
            option_style = "bold white on blue"
        else:
            option_style = "white"

        option_text = Text("Retour", style=option_style)
        table.add_row(option_text)

        padded_table = Padding(self.get_table_match(), (1, 0, 0, 0))

        table = Padding(table, (0, 1, 0, 1))
        panel_menu_options = Panel(table, title="Menu options",
                                   border_style="blue", padding=(1, 0),
                                   expand=False)
        padded_menu_options = Padding(panel_menu_options, 1)

        panel_title = f"[bold magenta]{"Matchs"}[/bold magenta]"
        layout = Group(Align.center(padded_table),
                       Align.center(padded_menu_options))
        panel = Panel(layout, title=panel_title)
        self.console.print(panel)

    def get_table_match(self):
        table_result = Table(show_lines=True)
        table_result.add_column("Joueur 1", justify="center")
        table_result.add_column("Joueur 2", justify="center")
        table_result.add_column("Résultat", justify="center")

        for index, match in enumerate(self.matches):
            table_result.add_row(str(match.get_player_one()), str(match.get_player_two()),
                                 match.winner)
        return table_result

    def render_all_matches_played(self, current_selection):
        table = Table.grid(padding=1)
        table.add_column(justify="center")

        if current_selection == 0:
            option_style = "bold white on blue"
        else:
            option_style = "white"

        option_text = Align.center(Text("Round suivant", style=option_style))
        table.add_row(option_text)

        if current_selection == 1:
            option_style = "bold white on blue"
        else:
            option_style = "white"

        option_text = Text("Retour", style=option_style)
        table.add_row(option_text)

        panel_menu_options = Panel(table, title="Menu options",
                                   border_style="blue", padding=(1, 1),
                                   expand=False)
        padded_menu_options = Padding(panel_menu_options, 1)

        panel_title = f"[bold magenta]{"Matchs"}[/bold magenta]"
        padded_table = Padding(self.get_table_match(), (1, 0, 0, 0))
        layout = Group(Align.center(padded_table),
                       Align.center(padded_menu_options))
        panel = Panel(layout, title=panel_title)
        self.console.print(panel)

    def render_match_result(self, current_selection):
        options = [self.current_match.players_score[0][0], self.current_match.players_score[1][0],
                   "Match nul", "Retour"]
        table = Table.grid(padding=1)
        table.add_column(justify="center")
        for index, option in enumerate(options):
            if index == current_selection:
                option_style = "bold white on blue"
            else:
                option_style = "white"
            option_text = Text(str(option), style=option_style)
            table.add_row(option_text)


        panel_title = f"[bold magenta]{"Résultat"}[/bold magenta]"
        table = Padding(table, (1, 0, 1, 0))
        panel = Panel(Align.center(table), title=panel_title)
        self.console.print(panel)

    def render_end_tournament(self, current_selection):
        table_result = Table(show_lines=True)
        table_result.add_column("Joueur", justify="center")
        table_result.add_column("Résultat", justify="center")

        for player,score in self.tournament_finals_scores.items():
            table_result.add_row(str(player), str(score))

        if current_selection == 0:
            option_style = "bold white on blue"
        else:
            option_style = "white"

        table = Table.grid(padding=1)
        table.add_column(justify="center")
        option_text = Text("OK", style=option_style)
        table.add_row(option_text)

        padded_table = Padding(table_result, (1, 0, 0, 0))

        panel_menu_options = Panel(Align.center(table), title="Menu options",
                                   border_style="blue", padding=(1, 0),
                                   expand=False)
        padded_menu_options = Padding(panel_menu_options, 1)

        panel_title = f"[bold magenta]{"Résultat"}[/bold magenta]"
        layout = Group(Align.center(padded_table),
                       Align.center(padded_menu_options))
        panel = Panel(layout, title=panel_title)
        self.console.print(panel)