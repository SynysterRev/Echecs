from rich.console import Console

from custom_exception import ViewException
from helpers.helper import Helper
from views.menu_view import MenuView
from views.player_view import PlayerView
from views.tournament_flow_view import TournamentFlowView
from views.tournament_view import TournamentView


class ViewManager:
    def __init__(self):
        self.console = Console()
        self.active_view = MenuView(self.console)
        self.views = {Helper.get_main_menu(): MenuView,
                      Helper.get_players_menu(): PlayerView,
                      Helper.get_tournament_menu(): TournamentView,
                      Helper.get_start_tournament_menu(): TournamentFlowView}
                      # Helper.get_generate_reports_menu(): ReportView(),

    def get_view(self, view_name):
        if view_name == Helper.get_quit():
            return None
        try:
            if view_name not in self.views:
                raise ViewException(view_name)
        except ViewException as view_exception:
            print(view_exception)
            return None
        return self.views[view_name](self.console)