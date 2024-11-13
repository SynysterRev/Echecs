from controllers.base_controller import BaseController
from helpers.helper import Helper
from views.menu_view import MenuView
from custom_exception import OutOfRangeValueException


class MenuController(BaseController):
    def __init__(self, view):
        """Construct a main menu controller

         accessible_menus: id of all the menus that we can access from here
        """
        super().__init__(view)
        self.accessible_menus = (Helper.get_new_tournament_menu(),
                                 Helper.get_launch_tournament_menu(),
                                 Helper.get_add_players_menu(),
                                 Helper.get_generate_reports_menu(),
                                 Helper.get_identification_menu(),
                                 Helper.get_quit())

    def run(self):
        self.view.accessible_menus = self.accessible_menus
        choice = self.get_user_choice()
        return self.accessible_menus[choice]
