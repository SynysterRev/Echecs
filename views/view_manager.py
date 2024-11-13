from custom_exception import ViewException
from helpers.helper import Helper
from views.identification_view import IdentificationView
from views.menu_view import MenuView
from views.player_view import PlayerView

class ViewManager:
    def __init__(self):
        self.active_view = IdentificationView()
        self.views = {Helper.get_identification_menu(): IdentificationView,
                      Helper.get_main_menu(): MenuView,
                      Helper.get_add_players_menu(): PlayerView}
                      # Helper.launch_tournament_menu(): TournamentView(),
                      # Helper.get_generate_reports_menu(): ReportView(),
                      # Helper.get_new_tournament_menu(): TournamentView()}

    def get_view(self, view_name):
        if view_name == Helper.get_quit():
            return None
        try:
            if view_name not in self.views:
                raise ViewException(view_name)
        except ViewException as view_exception:
            print(view_exception)
            return None
        return self.views[view_name]