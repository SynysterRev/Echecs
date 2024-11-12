import sys


class MenuException(Exception):
    """Menu not created"""

    def __init__(self, message=""):
        message = message
        super().__init__(message)


class Controller:
    """Main controller"""

    def __init__(self, active_controller, controllers):
        self.active_controller = active_controller
        self.controllers = controllers

    def run(self):
        running = True
        while running:
            next_menu_id = self.active_controller.run()
            self.active_controller = self.get_next_menu(next_menu_id)
            if self.active_controller is None:
                running = False

    def get_next_menu(self, next_menu_id):
        try:
            if not next_menu_id in self.controllers:
                if next_menu_id == "quit":
                    return None
                else:
                    raise MenuException(f"Menu {next_menu_id} n'existe pas. Fermeture du programme")
        except MenuException as menu_exception:
            print(menu_exception)
            sys.exit(1)
        return self.controllers[next_menu_id]
