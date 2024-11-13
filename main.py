from controllers.main_controller import MainController
from controllers.identification_controller import IdentificationController
from controllers.menu_controller import MenuController

from controllers.player_controller import PlayerController
from views.view_manager import ViewManager


def main():
    view_manager = ViewManager()
    main_controller = MainController(view_manager)
    main_controller.run()

if __name__ == "__main__":
    main()