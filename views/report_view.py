from rich.align import Align
from rich.console import Group
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from helpers.helper import Helper
from views.basic_view import BasicView


class ReportView(BasicView):
    """Menu where user can generate some reports"""

    def __init__(self, console):
        super().__init__(console)
        self.name = "Rapports"
        self.players_list = []
        self.tournaments = []
        self.selected_tournament = None

    def render_menu(self, current_selection):
        self.console.print(self.get_main_menu(current_selection))

    def get_main_menu(self, current_selection):
        table = self.get_table_menu(current_selection)
        table = Padding(table, (1, 0, 1, 0))
        return Panel(Align.center(table), title=f"[bold magenta]{self.name}[/bold magenta]")

    def get_menu_options(self, current_selection):
        table = self.get_table_menu(current_selection)
        panel_option = Panel(table, title="Menu options", border_style="blue", padding=1)
        return Padding(panel_option, 1)

    def render_all_players(self, current_selection):
        table = Table(show_lines=True)
        table.add_column("ID", justify="center")
        table.add_column("Prénom", justify="center")
        table.add_column("Nom", justify="center")
        table.add_column("Date de naissance", justify="center")

        self.players_list.sort(key=lambda player: player.name.lower())
        for player in self.players_list:
            row = [player.player_id, player.first_name, player.name, player.birth_date]
            table.add_row(*row)

        padded_table = Padding(table, (1, 0, 0, 0))

        panel_option = self.get_menu_options(current_selection)

        panel_title = "[bold magenta]Joueurs[/bold magenta]"
        layout = Group(Align.center(padded_table),
                       Align.center(panel_option))
        panel = Panel(layout, title=panel_title)
        self.console.print(panel)

    def render_all_tournaments(self, current_selection):
        table = Table(show_lines=True)
        table.add_column("Nom", justify="center", vertical="middle")
        table.add_column("Lieu", justify="center", vertical="middle")
        table.add_column("Date début", justify="center", vertical="middle")
        table.add_column("Date fin", justify="center", vertical="middle")
        table.add_column("ID Joueurs", justify="center", vertical="middle")
        table.add_column("Description", justify="center", vertical="middle")
        table.add_column("Nombre de rounds", justify="center", vertical="middle")

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

        panel_option = self.get_menu_options(current_selection)

        panel_title = "[bold magenta]Tournois[/bold magenta]"
        layout = Group(Align.center(padded_table),
                       Align.center(panel_option))
        panel = Panel(layout, title=panel_title)
        self.console.print(panel)

    def render_tournaments_names(self, current_selection):
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
        table.add_row(Text(Helper.text_menu[Helper.get_back()], style=option_style))
        panel_title = "[bold magenta]Sélection tournoi[/bold magenta]"
        table = Padding(table, (1, 0, 1, 0))
        self.console.print(Panel(Align.center(table), title=panel_title))

    def render_tournament_players(self, current_selection):
        table = Table(show_lines=True)
        table.add_column("ID", justify="center")
        table.add_column("Prénom", justify="center")
        table.add_column("Nom", justify="center")
        table.add_column("Date de naissance", justify="center")

        self.selected_tournament.players.sort(key=lambda player: player.name.lower())
        players_tournament_list = self.selected_tournament.players
        for player in players_tournament_list:
            row = [player.player_id, player.first_name, player.name, player.birth_date]
            table.add_row(*row)

        padded_table = Padding(table, (1, 0, 0, 0))

        panel_option = self.get_menu_options(current_selection)

        panel_title = f"[bold magenta]Joueurs du tournoi {self.selected_tournament.name}[/bold magenta]"
        layout = Group(Align.center(padded_table),
                       Align.center(panel_option))
        panel = Panel(layout, title=panel_title)
        self.console.print(panel)

    def render_tournament_info(self, current_selection):
        table = Table(show_lines=True)
        table.add_column("Tours", justify="center", vertical="middle")
        table.add_column("Matchs", justify="center", vertical="middle")
        table.add_column("Vainqueur", justify="center", vertical="middle")

        for round in self.selected_tournament.rounds:
            row = [round.name]
            all_matches = ""
            winners = ""
            for index, match in enumerate(round.matches):
                all_matches += str(match)
                winners += match.winner
                if index != len(round.matches) - 1:
                    all_matches += "\n\n"
                    winners += "\n\n"
            row.append(all_matches)
            row.append(winners)
            table.add_row(*row)

        padded_table = Padding(table, (1, 0, 0, 0))

        panel_option = self.get_menu_options(current_selection)

        table_result = Table(show_lines=True)
        table_result.add_column("Joueur", justify="center")
        table_result.add_column("Résultat", justify="center")

        sorted_points = dict(sorted(self.selected_tournament.players_points.items(), key=lambda item: item[1],
                    reverse=True))
        for player, score in sorted_points.items():
            table_result.add_row(str(player), str(score))
        padded_table_result = Padding(table_result, (1, 0, 0, 0))

        panel_title = f"[bold magenta]Informations tournoi {self.selected_tournament.name}[/bold magenta]"
        layout = Group(Align.center(padded_table),
                       Align.center(padded_table_result),
                       Align.center(panel_option))
        panel = Panel(layout, title=panel_title)
        self.console.print(panel)
