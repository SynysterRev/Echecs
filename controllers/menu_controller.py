from views.menu_view import MenuView
from views.base import OutOfRangeValueException


class MenuController:
    def __init__(self):
        """Construct a menu main controller

         accessible_menus: id of all the menus that we can access from here
        """
        self.view = MenuView()
        self.accessible_menus = ("new_tournament", "launch_tournament", "add_players", "generate_reports",
                                 "identification_menu", "quit")

    def run(self):
        self.view.accessible_menus = self.accessible_menus
        while True:
            try:
                choice = self.view.show_menu()
            except ValueError as ve:
                self.view.show_type_int_error()
            except OutOfRangeValueException as exception:
                self.view.show_custom_error(exception)
            else:
                return self.accessible_menus[choice]