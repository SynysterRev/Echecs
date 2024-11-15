import sys

from controllers.identification_controller import IdentificationController
from controllers.menu_controller import MenuController
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.tournament_flow_controller import TournamentFlowController
from helpers.helper import Helper
from custom_exception import MenuException


class MainController:
    """Main controller"""

    def __init__(self, view_manager):
        starting_view = view_manager.views[Helper.get_identification_menu()]()
        id_controller = IdentificationController(starting_view)
        all_controllers = {Helper.get_main_menu(): MenuController, Helper.get_identification_menu(): IdentificationController,
                           Helper.get_players_menu(): PlayerController, Helper.get_tournament_menu():
                               TournamentController, Helper.get_start_tournament_menu(): TournamentFlowController}
        self.active_controller = id_controller
        self.controllers = all_controllers
        self.view_manager = view_manager

    def run(self):
        running = True
        while running:
            next_menu_id = self.active_controller.run()
            controller_class = self.get_next_menu(next_menu_id)
            if controller_class is not None:
                requested_view = self.view_manager.get_view(next_menu_id)()
                new_controller = controller_class(requested_view)
                self.active_controller = new_controller
            else:
                running = False

    def get_next_menu(self, next_menu_id):
        try:
            if next_menu_id not in self.controllers:
                if next_menu_id == Helper.get_quit():
                    return None
                raise MenuException(f"Menu {next_menu_id} n'existe pas. Fermeture du programme")
        except MenuException as menu_exception:
            print(menu_exception)
            sys.exit(1)
        return self.controllers[next_menu_id]
