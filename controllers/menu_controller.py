from controllers.base_controller import BaseController
from helpers.helper import Helper


class MenuController(BaseController):
    def __init__(self, view):
        super().__init__(view)
        self.accessible_menus = (Helper.get_start_tournament_menu(),
                                 Helper.get_tournament_menu(),
                                 Helper.get_players_menu(),
                                 Helper.get_generate_reports_menu(),
                                 Helper.get_quit())