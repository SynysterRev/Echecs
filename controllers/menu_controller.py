from views.menu_view import MenuView


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
        choice = self.view.show_menu()
        return self.accessible_menus[choice]