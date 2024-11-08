from controllers.base import Controller
from controllers.identification_controller import IdentificationController
from controllers.menu_controller import MenuController
import json

from controllers.player_controller import PlayerController


def main():
    # MenuController.run()
    id_controller = IdentificationController()
    menu_controller = MenuController()
    player_controller = PlayerController()
    all_controllers = {"main_menu": menu_controller, "identification_menu": id_controller, "add_players": player_controller}
    controller = Controller(id_controller, all_controllers)
    controller.run()

if __name__ == "__main__":
    main()